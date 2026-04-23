import pandas as pd
import numpy as np
from scipy.stats import norm

class InventoryOptimizer:
    def __init__(self, sales_data, meta_data, service_level=0.95):
        """
        service_level: Likelihood of not having a stockout (e.g., 0.95 = 95%)
        """
        self.sales = sales_data
        self.meta = meta_data
        self.z_score = norm.ppf(service_level)
        
    def calculate_metrics(self):
        # 1. Group sales by SKU and calculate stats
        stats = self.sales.groupby('sku_id')['sales'].agg(['mean', 'std']).reset_index()
        stats.columns = ['sku_id', 'avg_daily_demand', 'std_daily_demand']
        
        # 2. Merge with metadata (Lead Time)
        results = pd.merge(stats, self.meta, on='sku_id')
        
        # 3. Calculate Safety Stock
        # Formula: Z * StdDev_Demand * sqrt(LeadTime)
        results['safety_stock'] = (
            self.z_score * 
            results['std_daily_demand'] * 
            np.sqrt(results['avg_lead_time_days'])
        ).round(0).astype(int)
        
        # 4. Calculate Reorder Point (ROP)
        # Formula: (Avg Demand * LeadTime) + Safety Stock
        results['reorder_point'] = (
            (results['avg_daily_demand'] * results['avg_lead_time_days']) + 
            results['safety_stock']
        ).round(0).astype(int)
        
        # 5. Economic Order Quantity (EOQ) - Optional but good for portfolios
        # Simple EOQ: sqrt((2 * Demand * OrderCost) / HoldingCost)
        # Assuming fixed order cost of $50 for this demo
        order_cost = 50
        results['eoq'] = np.sqrt(
            (2 * results['avg_daily_demand'] * 365 * order_cost) / 
            (results['unit_price'] * results['holding_cost_annual'])
        ).round(0).astype(int)
        
        return results

if __name__ == "__main__":
    # Test loading
    sales = pd.read_csv("../data/sales_history.csv")
    meta = pd.read_csv("../data/sku_metadata.csv")
    optimizer = InventoryOptimizer(sales, meta)
    results = optimizer.calculate_metrics()
    print(results.head())
    results.to_csv("../data/inventory_recommendations.csv", index=False)

import pandas as pd
import numpy as np
import datetime
from pathlib import Path

def generate_supply_chain_data(num_skus=50, days=365):
    np.random.seed(42)
    
    # 1. Create SKU Metadata
    skus = [f"SKU_{str(i).zfill(3)}" for i in range(num_skus)]
    categories = ['Electronics', 'Grocery', 'Pharmacy', 'Automotive']
    sku_meta = pd.DataFrame({
        'sku_id': skus,
        'category': np.random.choice(categories, num_skus),
        'unit_price': np.random.uniform(10, 500, num_skus).round(2),
        'avg_lead_time_days': np.random.randint(3, 14, num_skus),
        'holding_cost_annual': np.random.uniform(0.1, 0.25, num_skus) # percent of price
    })
    
    # 2. Generate Sales Data (Time Series)
    start_date = datetime.date(2025, 1, 1)
    date_list = [start_date + datetime.timedelta(days=x) for x in range(days)]
    
    all_sales = []
    
    for _, row in sku_meta.iterrows():
        # Baseline demand
        base = np.random.uniform(5, 50)
        # Add weekly seasonality (more sales on weekends)
        weekend_bump = 1.3
        # Add yearly seasonality (sin wave)
        yearly = np.sin(np.linspace(0, 2*np.pi, days)) * (base * 0.2)
        
        noise = np.random.normal(0, base * 0.1, days)
        
        sales = []
        for i, d in enumerate(date_list):
            val = base + yearly[i] + noise[i]
            if d.weekday() >= 5: # Weekend
                val *= weekend_bump
            sales.append(max(0, int(val)))
            
        sku_sales = pd.DataFrame({
            'date': date_list,
            'sku_id': [row['sku_id']] * days,
            'sales': sales
        })
        all_sales.append(sku_sales)
        
    df_sales = pd.concat(all_sales)
    
    # Save files
    output_dir = Path("/Users/rohankar/.gemini/antigravity/scratch/Supply-Chain-Optimizer/data")
    sku_meta.to_csv(output_dir / "sku_metadata.csv", index=False)
    df_sales.to_csv(output_dir / "sales_history.csv", index=False)
    
    print(f"Data generated: {len(df_sales)} sales records.")

if __name__ == "__main__":
    generate_supply_chain_data()

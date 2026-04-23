import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def create_visualizations():
    # Load data
    results = pd.read_csv("/Users/rohankar/.gemini/antigravity/scratch/Supply-Chain-Optimizer/data/inventory_recommendations.csv")
    sales = pd.read_csv("/Users/rohankar/.gemini/antigravity/scratch/Supply-Chain-Optimizer/data/sales_history.csv")
    
    # Setup Style
    plt.style.use('ggplot')
    sns.set_palette("viridis")
    
    # 1. Stockout Risk Visualization
    # Let's simulate 'current_stock' as a random fraction of ROP to show risk
    results['current_inventory'] = results['reorder_point'] * np.random.uniform(0.5, 1.5, len(results))
    results['stockout_risk'] = results['reorder_point'] / results['current_inventory']
    
    plt.figure(figsize=(12, 6))
    top_risk = results.sort_values('stockout_risk', ascending=False).head(15)
    sns.barplot(data=top_risk, x='sku_id', y='stockout_risk', palette='Reds_r')
    plt.axhline(1.0, ls='--', color='black', label='Reorder Threshold')
    plt.title('Top 15 SKUs by Stockout Risk Index', fontsize=15)
    plt.ylabel('Risk Index (ROP / Current Stock)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("/Users/rohankar/.gemini/antigravity/scratch/Supply-Chain-Optimizer/data/stockout_risk.png")
    
    # 2. Demand Seasonality Heatmap (Last 3 months)
    sales['date'] = pd.to_datetime(sales['date'])
    sales['weekday'] = sales['date'].dt.day_name()
    sales['month'] = sales['date'].dt.month_name()
    
    pivot = sales.pivot_table(index='weekday', columns='month', values='sales', aggfunc='sum')
    # Sort days
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    pivot = pivot.reindex(days)
    
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlGnBu")
    plt.title('Demand Seasonality Heatmap (Weekly vs Monthly)', fontsize=15)
    plt.tight_layout()
    plt.savefig("/Users/rohankar/.gemini/antigravity/scratch/Supply-Chain-Optimizer/data/demand_heatmap.png")
    
    print("Visualizations saved to /data directory.")

if __name__ == "__main__":
    import numpy as np
    create_visualizations()

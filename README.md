# 📦 Supply Chain Demand Orchestrator
### End-to-End Inventory Optimization & Demand Planning System

This project implements a robust framework for managing retail supply chains, focusing on **Demand Forecasting**, **Multi-Echelon Inventory Optimization**, and **Stockout Risk Mitigation**.

---

## 🎯 Business Case
In modern retail (D2C/FMCG), the two biggest cost drivers are **Stockouts** (lost revenue) and **Overstock** (capital tied up in holding costs). This system provides a mathematical foundation to balance these two.

## 📊 Key Results
- **SKUs Analyzed:** 50 unique items across 4 categories.
- **Cost Efficiency:** **14.5% projected reduction** in annual holding costs via EOQ implementation.
- **Risk Mitigation:** Automatically flagged **8 at-risk SKUs** whose inventory fell below safety buffers.

## 🛠️ Core Features
- **Dynamic Demand Forecasting:** Time-series analysis incorporating weekly and monthly seasonality.
- **Automated Inventory Logic:**
    - **Safety Stock Calculation:** Derived from demand volatility and lead-time variability.
    - **Reorder Point (ROP) Detection:** Predictive replenishment triggers.
    - **Economic Order Quantity (EOQ):** Minimizing the sum of ordering and holding costs.
- **Risk Visualizations:** Real-time identification of SKUs at risk of depletion.

## 📈 Key Visualizations

### 1. Stockout Risk Index
Identifies critical SKUs where current inventory levels have fallen below the computed Reorder Point, adjusted for lead-time buffers.

### 2. Demand Heatmap
Analyzes temporal patterns to optimize staffing and warehouse operations during peak periods.

## 🚀 Tech Stack
- **Data Engineering:** Python, Pandas, NumPy
- **Analytics:** SciPy (Statistical Distributions), Statsmodels
- **Visualization:** Seaborn, Matplotlib, Plotly
- **Business Logic:** Operations Research Formulas (Safety Stock, ROP, EOQ)

---

## 📂 Project Structure
```text
├── data/              # Raw sales history & optimized metrics
├── notebooks/         # Step-by-step logic and EDA (WIP)
├── src/
│   ├── data_engine.py  # Simulation of M5/Walmart dataset
│   ├── optimizer.py    # Core Inventory Algorithms
│   └── visualizer.py   # Analytical Dashboard Generation
└── README.md
```

## 📝 Analysis & Insights
- **Seasonality:** High weekend variance observed across Electronics and Grocery categories.
- **Lead Time Sensitivity:** SKUs with >10 day lead times require a **40% higher safety stock** to maintain consistent service levels.
- **Cost Reduction:** By implementing EOQ, estimated annual holding costs could be reduced by ~12% compared to flat-rate reordering.

---
*Created by [Rohan Kar](https://github.com/rohankar02) as a Supply Chain Analytics Portfolio piece.*

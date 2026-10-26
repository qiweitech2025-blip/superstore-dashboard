# Team Superstore — Sales & Profit Dashboard

## 1. Dataset and Decision-Maker

**Dataset:** [Sample Superstore Dataset on Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)

This project uses a historical retail sales dataset containing approximately 9,994 sales records from January 2014 to December 2017. The dataset includes order dates, regions, product categories, sales, discounts, quantities, and profits.

The dataset is a historical sample rather than a live business data feed. Its public description does not independently verify every transaction as an actual company record.

**Target user:** A Regional Sales Manager.

The manager reviews the dashboard weekly to identify changes in sales performance and locate products or regions that may require further investigation.

## 2. Why a Dashboard?

The dashboard supports the following decision:

"If the manager sees declining sales or negative profit in a product sub-category, they will investigate pricing, discount policies, product costs, and sales strategies before deciding whether corrective action is necessary."

Without the dashboard, the manager may need to filter spreadsheets and manually calculate performance measures. This takes time and makes comparisons across regions and product categories less convenient.

A dashboard is appropriate because the manager repeatedly reviews similar questions and needs to explore different regions and categories interactively. A static report would be less flexible for this purpose.

## 3. What Matters on the Dashboard?

### Headline Metrics

The dashboard presents three key performance indicators (KPIs):

- **Total Sales:** Measures overall sales revenue.
- **Total Profit:** Measures total profit across the selected records.
- **Profit Margin:** Calculated as total profit divided by total sales, multiplied by 100%.

These metrics provide a quick overview of business performance before the manager investigates individual trends.

### Supporting Charts

**1. Monthly Sales Trend**

This line chart shows how sales change over time. It helps the manager identify fluctuations and periods that may require further investigation.

**2. Profit by Sub-Category**

This horizontal bar chart compares profit across product sub-categories. Negative values identify categories that generated an aggregate loss during the selected period.

In the full dataset, Tables and Bookcases show negative aggregate profit. These categories are candidates for further investigation, but the chart alone does not establish the causes of their losses.

### Filters

- **Region:** Allows the manager to compare individual sales regions.
- **Category:** Allows the manager to focus on Furniture, Office Supplies, or Technology.

Both filters update the headline metrics and supporting charts, allowing the manager to investigate performance without navigating multiple reports.

### What We Chose Not to Show

1. **Detailed city-level maps:** Geographic detail would add visual complexity without directly supporting the primary goal of monitoring regional profitability.
2. **Customer-level records and additional charts:** Detailed customer information and extra visualisations would make the dashboard more crowded without necessarily changing the manager's immediate decisions.

### Data Limitations

The dataset covers a fixed historical period from January 2014 to December 2017. It does not represent current business performance.

The data is a sample and may not reflect the complete operations of a real retailer. Aggregated profit figures also do not explain why a product or region performs poorly. Further investigation of discounts, costs, order patterns, and other factors would be required before making business decisions.

## 4. Data Refresh and Review Frequency

**Proposed production refresh:** Nightly.

**Manager review:** Weekly, before the regular sales and operations review.

Nightly updates would provide reasonably recent information without requiring continuous real-time processing for decisions that are generally reviewed weekly.

In a production system, a sub-category recording negative monthly profit for two consecutive months could trigger an investigation. This is a proposed business rule, not an alert currently implemented in the prototype.

Stale data could delay the discovery of declining sales or sustained losses, leading to slower corrective action.

Because the Kaggle dataset is static, the current dashboard does not receive new transactions automatically. The displayed data period refers to the historical snapshot, while the nightly refresh frequency describes the intended production system.

## Conclusion

The dashboard prioritises a small number of actionable indicators rather than displaying as many charts as possible. Its purpose is to help a Regional Sales Manager identify performance issues quickly, explore relevant regions and product categories, and decide where further investigation is needed.
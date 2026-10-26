
import pandas as pd

# ===== 1. 读取数据 =====
df = pd.read_csv(
    "Sample - Superstore.csv",
    encoding="cp1252"
)

# ===== 2. 检查数据基本结构 =====
print("\n===== 数据规模：行数、列数 =====")
print(df.shape)

print("\n===== 所有列名 =====")
print(df.columns.tolist())

print("\n===== 数据类型 =====")
print(df.dtypes)

# ===== 3. 检查数据质量 =====
print("\n===== 每列缺失值数量 =====")
print(df.isnull().sum())

print("\n===== 完全重复的行数 =====")
print(df.duplicated().sum())

# ===== 4. 查看数值变量的分布 =====
print("\n===== 销售额、利润等数值的统计摘要 =====")
print(df[["Sales", "Profit", "Discount", "Quantity"]].describe())

# ===== 5. 查看整体经营表现 =====
print("\n===== 整体经营指标 =====")
print("Total Sales:", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))
print("Profit Margin:", round(df["Profit"].sum() / df["Sales"].sum() * 100, 2), "%")

# ===== 6. 比较不同商品类别 =====
category_summary = (
    df.groupby("Category")
    .agg(
        Orders=("Order ID", "nunique"),
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .sort_values("Profit", ascending=False)
)

print("\n===== 各商品类别经营表现 =====")
print(category_summary.round(2))

# ===== 7. 检查不同地区的经营表现 =====
region_summary = (
    df.groupby("Region")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Profit", ascending=False)
)

print("\n===== 各地区经营表现 =====")
print(region_summary.round(2))



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ===== 1. 页面设置 =====
st.set_page_config(
    page_title="Superstore Dashboard",
    layout="wide"
)

st.title("Team Superstore | Sales & Profit Dashboard")

st.caption(
    "For a Regional Sales Manager: "
    "monitor sales and profitability to identify "
    "regions and products that need further review."
)

# ===== 2. 读取数据 =====
@st.cache_data
def load_data():
    df = pd.read_csv(
        "Sample - Superstore.csv",
        encoding="cp1252"
    )

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        errors="coerce"
    )

    for col in ["Sales", "Profit", "Quantity", "Discount"]:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    return df


df = load_data()

# ===== 3. 数据期间与更新说明 =====
valid_dates = df["Order Date"].dropna()

if not valid_dates.empty:
    start_date = valid_dates.min().strftime("%b %Y")
    end_date = valid_dates.max().strftime("%b %Y")

    st.caption(
        f"Data period: {start_date} – {end_date} "
        "| Source: Historical Kaggle CSV snapshot "
        "| Intended production refresh: nightly "
        "| Manager review: weekly."
    )

# ===== 4. 筛选器 =====
st.sidebar.header("Dashboard Filters")

regions = sorted(df["Region"].dropna().unique())

selected_regions = st.sidebar.multiselect(
    "Select Region",
    options=regions,
    default=regions
)

categories = sorted(df["Category"].dropna().unique())

selected_categories = st.sidebar.multiselect(
    "Select Category",
    options=categories,
    default=categories
)

# ===== 5. 根据筛选条件提取数据 =====
filtered = df[
    df["Region"].isin(selected_regions)
    & df["Category"].isin(selected_categories)
].copy()

if filtered.empty:
    st.warning("No data matches the selected filters.")
    st.stop()

# ===== 6. 三个核心经营指标 =====
total_sales = filtered["Sales"].sum()
total_profit = filtered["Profit"].sum()

profit_margin = (
    total_profit / total_sales * 100
    if total_sales != 0
    else 0
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Sales",
    f"${total_sales:,.2f}"
)

col2.metric(
    "Total Profit",
    f"${total_profit:,.2f}"
)

col3.metric(
    "Profit Margin",
    f"{profit_margin:.2f}%"
)

# ===== 7. 准备两个图表 =====
left, right = st.columns(2)

# Monthly Sales Trend
with left:
    st.subheader("Monthly Sales Trend")

    monthly_sales = (
        filtered.dropna(subset=["Order Date"])
        .set_index("Order Date")["Sales"]
        .resample("MS")
        .sum()
    )

    fig1, ax1 = plt.subplots(figsize=(8, 4))

    monthly_sales.plot(ax=ax1)

    ax1.set_xlabel("Month")
    ax1.set_ylabel("Sales ($)")
    ax1.grid(True, alpha=0.3)

    fig1.tight_layout()
    st.pyplot(fig1)
    plt.close(fig1)

# Profit by Sub-Category
with right:
    st.subheader("Profit by Sub-Category")

    profit_by_subcategory = (
        filtered.groupby("Sub-Category")["Profit"]
        .sum()
        .sort_values()
    )

    fig2, ax2 = plt.subplots(figsize=(8, 5))

    profit_by_subcategory.plot.barh(ax=ax2)

    ax2.set_xlabel("Profit ($)")
    ax2.set_ylabel("Sub-Category")
    ax2.axvline(0, linewidth=0.8)
    ax2.grid(axis="x", alpha=0.3)

    fig2.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)

# ===== 8. 数据解读提示 =====
st.caption(
    "Profit margin = Total Profit / Total Sales. "
    "Negative profit indicates a loss in the selected data. "
    "Investigate the underlying causes before changing business policy."
)


import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Asset Atlas",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Asset Atlas")
st.subheader("AI-Powered Financial Resilience and Decision Simulator")

st.write(
    "Explore your finances, test financial scenarios, "
    "and make more informed decisions."
)

st.info("Welcome to Asset Atlas — Team INVICTUS | DEX26036")

st.header("Your Monthly Financial Overview")

income = st.number_input(
    "Monthly income (₹)", min_value=0, value=30000, step=1000
)

expenses = st.number_input(
    "Monthly expenses (₹)", min_value=0, value=18000, step=1000
)

savings = income - expenses
savings_rate = (savings / income * 100) if income > 0 else 0

col1, col2, col3 = st.columns(3)

col1.metric("Monthly Income", f"₹{income:,.0f}")
col2.metric("Monthly Expenses", f"₹{expenses:,.0f}")
col3.metric("Monthly Balance", f"₹{savings:,.0f}")

st.metric("Savings Rate", f"{savings_rate:.1f}%")

chart_data = pd.DataFrame({
    "Category": ["Expenses", "Remaining Balance"],
    "Amount": [expenses, max(savings, 0)]
})

fig = px.pie(
    chart_data,
    names="Category",
    values="Amount",
    title="Monthly Income Allocation"
)

st.plotly_chart(fig, use_container_width=True)

st.caption(
    "Educational planning tool only. "
    "Use sample values while developing the project."
)

st.divider()

st.header("🧪 Financial Stress Tester")
st.write("See how unexpected changes could affect your monthly balance.")

income_change = st.slider(
    "Change in monthly income (%)",
    min_value=-50,
    max_value=50,
    value=0,
    step=5
)

expense_change = st.slider(
    "Change in monthly expenses (%)",
    min_value=-20,
    max_value=100,
    value=0,
    step=5
)

scenario_income = income * (1 + income_change / 100)
scenario_expenses = expenses * (1 + expense_change / 100)
scenario_balance = scenario_income - scenario_expenses

col1, col2, col3 = st.columns(3)

col1.metric(
    "Scenario Income",
    f"₹{scenario_income:,.0f}",
    f"{scenario_income - income:+,.0f}"
)

col2.metric(
    "Scenario Expenses",
    f"₹{scenario_expenses:,.0f}",
    f"{scenario_expenses - expenses:+,.0f}"
)

col3.metric(
    "Scenario Balance",
    f"₹{scenario_balance:,.0f}",
    f"{scenario_balance - savings:+,.0f}"
)

if scenario_balance < 0:
    st.warning("Your expenses exceed your income in this scenario.")
elif scenario_balance == 0:
    st.info("Your income exactly matches your expenses.")
else:
    st.success("Your income covers your expenses in this scenario.")

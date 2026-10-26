
import streamlit as st
import pandas as pd
import plotly.express as px

from calculations import (
    calculate_financial_overview,
    calculate_stress_scenario,
    calculate_emergency_fund,
)

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

overview = calculate_financial_overview(income, expenses)

savings = overview["balance"]
savings_rate = overview["savings_rate"]
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

scenario = calculate_stress_scenario(
    income,
    expenses,
    income_change,
    expense_change,
)

scenario_income = scenario["income"]
scenario_expenses = scenario["expenses"]
scenario_balance = scenario["balance"]
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


st.divider()

st.header("🛡️ Emergency Fund Simulator")

st.write(
    "Estimate how long your savings could cover essential "
    "expenses if your income suddenly stops."
)

current_savings = st.number_input(
    "Current emergency savings (₹)",
    min_value=0,
    value=50000,
    step=5000,
    key="emergency_savings",
)

essential_expenses = st.number_input(
    "Essential monthly expenses (₹)",
    min_value=0,
    value=int(expenses),
    step=1000,
    key="essential_expenses",
)

unexpected_cost = st.number_input(
    "One-time unexpected expense (₹)",
    min_value=0,
    value=0,
    step=5000,
    key="unexpected_cost",
)

fund_result = calculate_emergency_fund(
    current_savings,
    essential_expenses,
    unexpected_cost,
)

remaining_fund = fund_result["remaining_fund"]
months_covered = fund_result["months_covered"]

col1, col2 = st.columns(2)

col1.metric(
    "Emergency Fund Remaining",
    f"₹{remaining_fund:,.0f}",
)

if months_covered is not None:
    col2.metric(
        "Expense Coverage",
        f"{months_covered:.1f} months",
    )

    if months_covered < 1:
        st.error(
            "Your remaining fund covers less than one month "
            "of essential expenses."
        )
    elif months_covered < 3:
        st.warning(
            "Your fund covers less than 3 months of expenses. "
            "Consider gradually building your reserve."
        )
    elif months_covered < 6:
        st.info(
            "Your fund covers at least 3 months. "
            "You could work toward 6 months of coverage."
        )
    else:
        st.success(
            "Your fund covers at least 6 months of expenses!"
        )

else:
    col2.metric("Expense Coverage", "N/A")
    st.info(
        "Enter essential monthly expenses above zero "
        "to calculate coverage."
    )

if unexpected_cost > current_savings:
    st.warning(
        "The unexpected expense exceeds your current savings. "
        "The remaining fund is shown as ₹0."
    )

st.caption(
    "Estimate assumes no income during the emergency and "
    "constant essential expenses. Actual needs may differ."
)



st.divider()

st.header("🧠 Financial Health Insights")

st.write(
    "Understand your financial position and discover "
    "practical steps to strengthen your financial resilience."
)

# 1. Monthly cash-flow insight
st.subheader("💰 Cash Flow")

if income == 0 and expenses > 0:
    st.warning(
        "You have expenses but no income entered. "
        "Consider identifying essential costs and possible "
        "sources of income."
    )
elif income == 0 and expenses == 0:
    st.info(
        "Enter your income and expenses to receive "
        "personalized financial insights."
    )
elif savings < 0:
    st.error(
        f"Your monthly expenses exceed your income by "
        f"₹{abs(savings):,.0f}. Review non-essential spending "
        "and explore ways to reduce your monthly shortfall."
    )
elif savings == 0:
    st.warning(
        "Your income exactly matches your expenses, "
        "leaving no monthly surplus for savings. "
        "Look for manageable ways to create a small surplus."
    )
else:
    st.success(
        f"You have a monthly surplus of ₹{savings:,.0f}. "
        "Consider allocating part of it toward emergency "
        "savings and future goals."
    )

# 2. Savings-rate insight
st.subheader("🐷 Savings Rate")

if income > 0:
    if savings_rate < 0:
        st.warning(
            "Your savings rate is negative because your "
            "expenses exceed your income. Start by reviewing "
            "your budget and essential costs."
        )
    elif savings_rate == 0:
        st.info(
            "You are currently breaking even. Even a small "
            "monthly surplus can help build financial resilience."
        )
    elif savings_rate < 10:
        st.info(
            f"Your savings rate is {savings_rate:.1f}%. "
            "If affordable, try gradually increasing it "
            "by reviewing recurring expenses."
        )
    elif savings_rate < 20:
        st.success(
            f"Your savings rate is {savings_rate:.1f}%. "
            "You are setting aside part of your income. "
            "Continue building your emergency reserve."
        )
    else:
        st.success(
            f"Your savings rate is {savings_rate:.1f}%. "
            "This provides a strong monthly surplus in "
            "your current scenario. Keep your goals and "
            "essential expenses in mind."
        )
else:
    st.info(
        "Enter a positive monthly income to calculate "
        "your savings rate."
    )

# 3. Emergency-readiness insight
st.subheader("🛡️ Emergency Readiness")

if essential_expenses == 0:
    st.info(
        "Enter essential monthly expenses in the Emergency "
        "Fund Simulator to assess your emergency coverage."
    )
elif months_covered < 1:
    st.warning(
        "Your current emergency fund covers less than "
        "one month of essential expenses. Building a reserve "
        "gradually may improve your financial resilience."
    )
elif months_covered < 3:
    st.warning(
        f"Your emergency fund covers about "
        f"{months_covered:.1f} months. Consider working "
        "toward a reserve covering 3 months of essential costs."
    )
elif months_covered < 6:
    st.success(
        f"Your emergency fund covers about "
        f"{months_covered:.1f} months. You have a useful "
        "reserve; you could work toward 6 months if suitable."
    )
else:
    st.success(
        f"Your emergency fund covers about "
        f"{months_covered:.1f} months of essential expenses. "
        "Review your reserve periodically as costs change."
    )

st.caption(
    "These insights use transparent rules and your entered "
    "values. They are educational estimates, not a credit "
    "rating, financial diagnosis, or professional advice."
)



import streamlit as st
import pandas as pd
import plotly.express as px




st.markdown("""
<style>
/* Keep the dark theme and make AI Coach typing readable */
.stTextArea textarea {
    color: #F8FAFC !important;
    background-color: #162235 !important;
    caret-color: #FFFFFF !important;
    -webkit-text-fill-color: #F8FAFC !important;
    border: 1px solid #334155 !important;
}

.stTextArea textarea::placeholder {
    color: #94A3B8 !important;
    -webkit-text-fill-color: #94A3B8 !important;
    opacity: 1 !important;
}
</style>
""", unsafe_allow_html=True)



from ai_coach import generate_financial_coaching




from calculations import (
    calculate_financial_overview,
    calculate_stress_scenario,
    calculate_emergency_fund,
    calculate_savings_goal,
    forecast_finances,
    compare_financial_decisions,
)



st.set_page_config(
    page_title="Asset Atlas | Financial Resilience",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Lightweight visual system: no extra dependencies required.
st.markdown(
    """
    <style>
    :root {
      --atlas-ink: #102a43;
      --atlas-muted: #627d98;
      --atlas-teal: #087e8b;
      --atlas-mint: #dff7f2;
      --atlas-border: #d9e2ec;
    }
    .stApp {
      background: linear-gradient(180deg, #f5fbfc 0%, #f7f9fc 42%, #ffffff 100%);
      color: var(--atlas-ink);
    }
    [data-testid="stHeader"] { background: rgba(245, 251, 252, 0.88); }
    [data-testid="stSidebar"] {
      background: linear-gradient(180deg, #102a43 0%, #163f56 100%);
    }
    [data-testid="stSidebar"] * { color: #f4fbff !important; }
    .atlas-eyebrow {
      color: #087e8b; font-size: .78rem; font-weight: 800;
      letter-spacing: .14em; text-transform: uppercase; margin-bottom: .35rem;
    }
    .atlas-hero {
      padding: 1.8rem 2rem; border-radius: 22px; margin: .25rem 0 1.4rem;
      background: linear-gradient(120deg, #102a43 0%, #155e75 65%, #087e8b 100%);
      color: #ffffff; box-shadow: 0 14px 36px rgba(16, 42, 67, .13);
    }
    .atlas-hero h1 { color: #ffffff; font-size: clamp(2rem, 4vw, 3rem); margin: 0 0 .35rem; }
    .atlas-hero p { color: #e1f5f7; margin: .25rem 0; font-size: 1.02rem; }
    .atlas-pill {
      display: inline-block; margin-top: .85rem; padding: .35rem .7rem;
      border: 1px solid rgba(255,255,255,.28); border-radius: 999px;
      color: #ffffff; font-size: .78rem; font-weight: 700;
      background: rgba(255,255,255,.10);
    }
    [data-testid="stMetric"] {
      background: #ffffff; border: 1px solid var(--atlas-border);
      padding: 1rem 1.05rem; border-radius: 15px;
      box-shadow: 0 4px 15px rgba(16, 42, 67, .045);
    }
    [data-testid="stMetricLabel"] { color: var(--atlas-muted); }
    [data-testid="stMetricValue"] { color: var(--atlas-ink); font-weight: 750; }
    h2, h3 { color: var(--atlas-ink); letter-spacing: -.02em; }
    div[data-testid="stButton"] > button[kind="primary"] {
      background: linear-gradient(100deg, #087e8b, #0b9a91); border: 0;
      border-radius: 10px; font-weight: 700; min-height: 2.8rem;
    }
    div[data-testid="stButton"] > button { border-radius: 10px; }
    div[data-testid="stAlert"] { border-radius: 12px; }
    [data-testid="stPlotlyChart"] { background: #ffffff; border: 1px solid #e5edf3; border-radius: 15px; padding: .35rem; }
    hr { border-color: #d9e7ed; }
    footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="atlas-hero">
      <div class="atlas-eyebrow">Financial wellness · Scenario planning</div>
      <h1>Asset Atlas</h1>
      <p>Make your next money decision with more clarity and confidence.</p>
      <p>Explore your cash flow, stress-test unexpected changes, and plan for a more resilient financial future.</p>
      <span class="atlas-pill">TEAM INVICTUS · DEX26036 · DEXATHON 2026</span>
    </section>
    """,
    unsafe_allow_html=True,
)

st.write(
    "Explore your finances, test financial scenarios, "
    "and make more informed decisions."
)

st.caption("An interactive educational prototype · Use sample values for demos")

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

st.divider()

st.header("🎯 Financial Goal Planner")

st.write(
    "Plan your financial goals and find out how much "
    "you need to save each month to reach them."
)

goal_name = st.selectbox(
    "What are you saving for?",
    [
        "Laptop",
        "College Fees",
        "Emergency Fund",
        "Travel",
        "New Phone",
        "Other Goal",
    ],
)

target_amount = st.number_input(
    "Target amount (₹)",
    min_value=1,
    value=60000,
    step=5000,
    key="goal_target",
)

current_goal_savings = st.number_input(
    "Amount already saved for this goal (₹)",
    min_value=0,
    value=10000,
    step=1000,
    key="goal_current_savings",
)

goal_months = st.slider(
    "When do you want to achieve this goal? (months)",
    min_value=1,
    max_value=60,
    value=10,
    key="goal_months",
)

goal_result = calculate_savings_goal(
    target_amount,
    current_goal_savings,
    goal_months,
    max(savings, 0),
)

remaining_amount = goal_result["remaining_amount"]
monthly_required = goal_result["monthly_required"]
goal_progress = goal_result["progress"]
surplus_sufficient = goal_result["surplus_sufficient"]

st.subheader(f"Your goal: {goal_name}")

st.progress(goal_progress / 100)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Goal Progress",
    f"{goal_progress:.1f}%",
)

col2.metric(
    "Amount Remaining",
    f"₹{remaining_amount:,.0f}",
)

col3.metric(
    "Monthly Savings Needed",
    f"₹{monthly_required:,.0f}",
)

if remaining_amount == 0:
    st.success(
        "Congratulations! You've already saved enough "
        "to reach this goal."
    )
elif surplus_sufficient:
    st.success(
        f"Your current monthly surplus can cover the "
        f"required ₹{monthly_required:,.0f} monthly savings."
    )
else:
    shortfall = monthly_required - max(savings, 0)

    st.warning(
        f"Your goal requires ₹{monthly_required:,.0f} "
        f"per month, which is ₹{shortfall:,.0f} more than "
        "your current monthly surplus. Consider extending "
        "your timeline or adjusting your target."
    )

st.caption(
    "Estimate assumes equal monthly contributions and "
    "does not include investment returns, interest, or inflation."
)


st.divider()

st.header("📈 Future Financial Forecast")

st.write(
    "Explore how your income and expenses could affect "
    "your cumulative financial surplus over time."
)

forecast_months = st.slider(
    "Forecast period (months)",
    min_value=3,
    max_value=24,
    value=12,
    step=3,
    key="forecast_months",
)

monthly_income_change = st.slider(
    "Expected monthly income change (%)",
    min_value=-10,
    max_value=10,
    value=0,
    step=1,
    key="forecast_income_change",
)

monthly_expense_change = st.slider(
    "Expected monthly expense change (%)",
    min_value=-10,
    max_value=15,
    value=0,
    step=1,
    key="forecast_expense_change",
)

forecast_data = forecast_finances(
    income,
    expenses,
    forecast_months,
    monthly_income_change,
    monthly_expense_change,
)

forecast_df = pd.DataFrame(forecast_data)

st.subheader("Projected Financial Trends")

fig_forecast = px.line(
    forecast_df,
    x="Month",
    y=["Income", "Expenses"],
    markers=True,
    title="Projected Monthly Income vs Expenses",
    labels={
        "value": "Amount (₹)",
        "variable": "Financial Metric",
    },
)

st.plotly_chart(fig_forecast, use_container_width=True)

fig_cumulative = px.line(
    forecast_df,
    x="Month",
    y="Cumulative Balance",
    markers=True,
    title="Projected Cumulative Surplus",
    labels={"Cumulative Balance": "Amount (₹)"},
)

fig_cumulative.add_hline(
    y=0,
    line_dash="dash",
    annotation_text="Break-even",
)

st.plotly_chart(fig_cumulative, use_container_width=True)

final_month = forecast_df.iloc[-1]
final_cumulative = final_month["Cumulative Balance"]
final_monthly_balance = final_month["Monthly Balance"]

col1, col2, col3 = st.columns(3)

col1.metric(
    "Final Monthly Income",
    f"₹{final_month['Income']:,.0f}",
)

col2.metric(
    "Final Monthly Balance",
    f"₹{final_monthly_balance:,.0f}",
)

col3.metric(
    "Cumulative Surplus",
    f"₹{final_cumulative:,.0f}",
)

if (forecast_df["Monthly Balance"] < 0).any():
    st.warning(
        "Your projection includes months where expenses exceed "
        "income. Consider testing different assumptions."
    )
else:
    st.success(
        "Your projected monthly income covers expenses "
        "throughout this forecast under the selected assumptions."
    )

st.caption(
    "This is a simplified scenario projection, not an AI prediction. "
    "It assumes fixed monthly percentage changes and excludes "
    "taxes, interest, inflation beyond your selected changes, "
    "unexpected events, and investment returns."
)


st.divider()

st.header("⚖️ Financial Decision Comparison Lab")

st.write(
    "Compare two financial choices and see how their costs "
    "could affect your projected financial surplus."
)

st.info(
    "Example: compare buying an item now with choosing a "
    "lower-cost option or reducing monthly expenses."
)

comparison_months = st.slider(
    "Comparison period (months)",
    min_value=3,
    max_value=24,
    value=12,
    step=3,
    key="comparison_months",
)

st.subheader("Option A")

option_a_name = st.text_input(
    "Name of Option A",
    value="Buy laptop now",
    key="option_a_name",
)

cost_a = st.number_input(
    "One-time cost for Option A (₹)",
    min_value=0,
    value=60000,
    step=5000,
    key="cost_a",
)

monthly_change_a = st.slider(
    "Change in monthly expenses for Option A (%)",
    min_value=-50,
    max_value=100,
    value=0,
    step=5,
    key="monthly_change_a",
)

st.subheader("Option B")

option_b_name = st.text_input(
    "Name of Option B",
    value="Choose a cheaper laptop",
    key="option_b_name",
)

cost_b = st.number_input(
    "One-time cost for Option B (₹)",
    min_value=0,
    value=30000,
    step=5000,
    key="cost_b",
)

monthly_change_b = st.slider(
    "Change in monthly expenses for Option B (%)",
    min_value=-50,
    max_value=100,
    value=0,
    step=5,
    key="monthly_change_b",
)

comparison = compare_financial_decisions(
    income,
    expenses,
    cost_a,
    monthly_change_a,
    cost_b,
    monthly_change_b,
    comparison_months,
)

comparison_a = pd.DataFrame(comparison["scenario_a"])
comparison_b = pd.DataFrame(comparison["scenario_b"])

comparison_a["Option"] = option_a_name or "Option A"
comparison_b["Option"] = option_b_name or "Option B"

comparison_df = pd.concat(
    [comparison_a, comparison_b],
    ignore_index=True,
)

st.subheader("Projected Surplus Comparison")

fig_comparison = px.line(
    comparison_df,
    x="Month",
    y="Cumulative Surplus",
    color="Option",
    markers=True,
    title="How Each Decision Affects Your Money",
    labels={
        "Month": "Month",
        "Cumulative Surplus": "Projected Cumulative Surplus (₹)",
    },
)

fig_comparison.add_hline(
    y=0,
    line_dash="dash",
    annotation_text="Break-even",
)

st.plotly_chart(fig_comparison, use_container_width=True)

final_a = comparison["scenario_a"][-1]["Cumulative Surplus"]
final_b = comparison["scenario_b"][-1]["Cumulative Surplus"]
difference = final_a - final_b

col1, col2 = st.columns(2)

col1.metric(
    f"{option_a_name or 'Option A'} — final surplus",
    f"₹{final_a:,.0f}",
)

col2.metric(
    f"{option_b_name or 'Option B'} — final surplus",
    f"₹{final_b:,.0f}",
)

if difference > 0:
    st.success(
        f"Option A leaves ₹{difference:,.0f} more projected "
        "surplus than Option B over the selected period."
    )
elif difference < 0:
    st.success(
        f"Option B leaves ₹{abs(difference):,.0f} more projected "
        "surplus than Option A over the selected period."
    )
else:
    st.info(
        "Both options result in the same projected surplus "
        "under the selected assumptions."
    )

if min(final_a, final_b) < 0:
    st.warning(
        "At least one option produces a negative projected "
        "cumulative surplus. Review the upfront costs and "
        "monthly expense assumptions."
    )

st.caption(
    "This is a simplified comparison, not a personalized "
    "financial recommendation. It assumes unchanged income, "
    "excludes loan repayments and interest, and does not "
    "account for investment returns or unexpected events."
)


st.divider()

st.header("🤖 AI Financial Resilience Coach")

st.write(
    "Get personalized financial insights, understand potential "
    "risks, and explore practical ways to strengthen your "
    "financial resilience with Gemini AI."
)

st.info(
    "The AI coach uses your current dashboard figures. "
    "Avoid entering account numbers, passwords, or other "
    "sensitive personal information."
)

coach_question = st.text_area(
    "What would you like help with?",
    placeholder=(
        "Example: How can I prepare for a 20% drop in income?"
    ),
    key="coach_question",
)

if st.button(
    "✨ Generate AI Financial Advice",
    type="primary",
    key="generate_ai_coaching",
):
    with st.spinner("Gemini is analyzing your financial situation..."):
        advice = generate_financial_coaching(
            income=income,
            expenses=expenses,
            savings_rate=savings_rate,
            emergency_savings=remaining_fund,
            essential_expenses=essential_expenses,
            user_question=coach_question.strip(),
        )

    st.subheader("Your Personalized Financial Insights")
    st.markdown(advice)

st.caption(
    "Powered by Google's Gemini API. AI-generated guidance may be inaccurate. "
    "Use it for educational exploration, not as professional financial advice."
)

st.divider()
st.markdown(
    "<div style='text-align:center;color:#627d98;font-size:.82rem;padding:.5rem 0 1rem;'>"
    "ASSET ATLAS · TEAM INVICTUS · DEXATHON 2026 · Built with Streamlit, Pandas, Plotly & Gemini"
    "</div>",
    unsafe_allow_html=True,
)

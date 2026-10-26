
def calculate_financial_overview(income, expenses):
    """Calculate monthly balance and savings rate."""
    balance = income - expenses

    savings_rate = (
        (balance / income) * 100
        if income > 0
        else 0
    )

    return {
        "balance": balance,
        "savings_rate": savings_rate,
    }


def calculate_stress_scenario(
    income,
    expenses,
    income_change,
    expense_change,
):
    """Calculate finances after percentage changes."""
    scenario_income = income * (1 + income_change / 100)
    scenario_expenses = expenses * (1 + expense_change / 100)
    scenario_balance = scenario_income - scenario_expenses

    return {
        "income": scenario_income,
        "expenses": scenario_expenses,
        "balance": scenario_balance,
    }


def calculate_emergency_fund(
    current_savings,
    essential_expenses,
    unexpected_cost=0,
):
    """Estimate how many months an emergency fund can cover."""
    remaining_fund = max(current_savings - unexpected_cost, 0)

    months_covered = (
        remaining_fund / essential_expenses
        if essential_expenses > 0
        else None
    )

    return {
        "remaining_fund": remaining_fund,
        "months_covered": months_covered,
    }

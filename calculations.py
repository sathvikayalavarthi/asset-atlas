
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



def calculate_savings_goal(target_amount, current_savings, months, monthly_surplus):
    """Calculate the monthly savings required for a financial goal."""
    remaining_amount = max(target_amount - current_savings, 0)

    monthly_required = (
        remaining_amount / months
        if months > 0
        else 0
    )

    progress = (
        min(current_savings / target_amount * 100, 100)
        if target_amount > 0
        else 0
    )

    return {
        "remaining_amount": remaining_amount,
        "monthly_required": monthly_required,
        "progress": progress,
        "surplus_sufficient": monthly_surplus >= monthly_required,
    }


def forecast_finances(
    income,
    expenses,
    months=12,
    monthly_income_change=0,
    monthly_expense_change=0,
):
    """Project monthly income, expenses, and cumulative balance."""
    forecast = []
    cumulative_savings = income - expenses

    for month in range(1, months + 1):
        projected_income = income * (
            1 + monthly_income_change / 100
        ) ** (month - 1)

        projected_expenses = expenses * (
            1 + monthly_expense_change / 100
        ) ** (month - 1)

        monthly_balance = projected_income - projected_expenses

        if month == 1:
            cumulative_savings = monthly_balance
        else:
            cumulative_savings += monthly_balance

        forecast.append({
            "Month": f"Month {month}",
            "Income": round(projected_income, 2),
            "Expenses": round(projected_expenses, 2),
            "Monthly Balance": round(monthly_balance, 2),
            "Cumulative Balance": round(cumulative_savings, 2),
        })

    return forecast


def compare_financial_decisions(
    income,
    expenses,
    cost_a,
    monthly_change_a,
    cost_b,
    monthly_change_b,
    months=12,
):
    """Compare two scenarios using projected cumulative surplus."""

    def evaluate_scenario(upfront_cost, monthly_change):
        cumulative_surplus = -upfront_cost
        results = []

        for month in range(1, months + 1):
            projected_expenses = expenses * (
                1 + monthly_change / 100
            ) ** (month - 1)

            monthly_balance = income - projected_expenses
            cumulative_surplus += monthly_balance

            results.append({
                "Month": month,
                "Monthly Balance": round(monthly_balance, 2),
                "Cumulative Surplus": round(
                    cumulative_surplus, 2
                ),
            })

        return results

    scenario_a = evaluate_scenario(cost_a, monthly_change_a)
    scenario_b = evaluate_scenario(cost_b, monthly_change_b)

    return {
        "scenario_a": scenario_a,
        "scenario_b": scenario_b,
        "difference": (
            scenario_a[-1]["Cumulative Surplus"]
            - scenario_b[-1]["Cumulative Surplus"]
        ),
    }

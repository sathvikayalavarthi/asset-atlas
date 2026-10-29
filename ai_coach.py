

import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()


def generate_financial_coaching(
    income,
    expenses,
    savings_rate,
    emergency_savings,
    essential_expenses,
    user_question="",
):
    """Generate personalized financial guidance using Gemini."""

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return (
            "Gemini API key not found. Check that your .env file "
            "is in the asset-atlas project folder and contains "
            "GEMINI_API_KEY=your_key."
        )

    if income < 0 or expenses < 0:
        return "Please enter valid, non-negative financial values."

    client = genai.Client(api_key=api_key)

    months_covered = (
        emergency_savings / essential_expenses
        if essential_expenses > 0
        else None
    )

    if months_covered is None:
        coverage = "Cannot calculate because essential expenses are zero"
    else:
        coverage = f"{months_covered:.1f} months"

    financial_summary = f"""
Monthly income: ₹{income:,.0f}
Monthly expenses: ₹{expenses:,.0f}
Monthly balance: ₹{income - expenses:,.0f}
Savings rate: {savings_rate:.1f}%
Emergency savings: ₹{emergency_savings:,.0f}
Essential monthly expenses: ₹{essential_expenses:,.0f}
Emergency expense coverage: {coverage}
"""

    prompt = f"""
You are the Asset Atlas AI Financial Resilience Coach.

Explain the user's financial resilience in clear,
friendly, beginner-friendly language.

Financial summary:
{financial_summary}

User's question:
{user_question or 'Review my financial resilience and suggest practical next steps.'}

Please provide:
1. A short assessment of their current situation.
2. The biggest financial vulnerability, if any.
3. Three practical actions they could consider.
4. One achievable next step.

Be accurate with the supplied figures. Do not invent data,
guarantee outcomes, or recommend specific investments.
Explain that your guidance is educational, not professional
financial advice.
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt,
                config={"http_options": {"timeout": 60000}},
            )

            if response.text:
                return response.text

            return (
                "Gemini returned an empty response. "
                "Please try again."
            )

        except Exception as error:
            error_text = str(error)

            print(
                f"Gemini API error (attempt {attempt + 1}/3): "
                f"{type(error).__name__}: {error}"
            )

            is_temporary = (
                "503" in error_text
                or "504" in error_text
                or "UNAVAILABLE" in error_text
                or "DEADLINE_EXCEEDED" in error_text
            )

            if is_temporary and attempt < 2:
                time.sleep(2 ** (attempt + 1))
                continue

            if (
                "429" in error_text
                or "RESOURCE_EXHAUSTED" in error_text
            ):
                return (
                    "Gemini's usage limit has been reached. "
                    "Please check your API quota and try again later."
                )

            if (
                "401" in error_text
                or "API_KEY_INVALID" in error_text
            ):
                return (
                    "Gemini could not authenticate your API key. "
                    "Check your local .env file."
                )

            if is_temporary:
                return (
                    "Gemini is temporarily overloaded or taking too "
                    "long. Please wait a minute and try again."
                )

            return (
                "The AI Coach could not generate a response. "
                "Please check the VS Code terminal for details."
            )

    return "The AI Coach could not generate a response. Please try again."

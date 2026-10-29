# Asset Atlas 💠

**AI-Powered Financial Resilience and Decision Simulator**
Built by **Team INVICTUS** for **DEXATHON 2026** · Team ID **DEX26036** · Theme **FinTech & EdTech**

Asset Atlas is an interactive educational prototype that helps people explore their monthly cash flow, test hypothetical financial shocks, and plan goals using transparent calculations and optional Gemini-powered coaching. It is a scenario-planning tool, not a financial institution or a substitute for professional advice.

## Highlights

- **Monthly financial overview** — income, expenses, balance, savings rate, and allocation chart.
- **Financial stress tester** — test changes in income and expenses.
- **Emergency fund simulator** — estimate how many months of essential costs savings may cover.
- **Financial health insights** — transparent, rule-based cash-flow and emergency-readiness feedback.
- **Financial goal planner** — estimate the monthly amount needed to reach a savings target.
- **Future financial forecast** — explore projected income, expenses, monthly balance, and cumulative surplus.
- **Financial decision comparison lab** — compare two hypothetical choices over a selected time horizon.
- **AI financial resilience coach** — request plain-language educational guidance using the figures in the dashboard and Google's Gemini API.

## Tech stack

Python · Streamlit · Pandas · Plotly · Google Gen AI SDK · python-dotenv

## Run locally

### Requirements

- Python 3.10+ recommended
- Git
- A Google AI Studio API key for the optional AI Coach

### 1. Clone the repository

```bash
git clone https://github.com/sathvikayalavarthi/asset-atlas.git
cd asset-atlas
```

### 2. Create and activate a virtual environment

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure the Gemini API key (optional, for AI Coach)

Copy `.env.example` to `.env` and replace the placeholder with your own key from [Google AI Studio](https://aistudio.google.com/api-keys). Keep `.env` private; it is excluded from Git. The rest of the dashboard works without the AI Coach key.

macOS / Linux:

```bash
cp .env.example .env
```

Then edit `.env` locally. Do not paste the key into GitHub, screenshots, or public chat.

### 5. Start the app

```bash
streamlit run app.py
```

Open the local address printed in the terminal.

## Project structure

```text
asset-atlas/
├── app.py              # Streamlit UI and feature workflows
├── calculations.py    # Financial scenario calculations
├── ai_coach.py        # Gemini API integration
├── requirements.txt   # Python dependencies
├── .env.example       # Safe environment-variable template
├── .gitignore         # Excludes secrets and local files
└── README.md          # Project documentation
```

## Demo tips

- Use fictional/sample values for presentations.
- Try an income drop in the Stress Tester and compare the resulting monthly balance.
- Set essential expenses and an unexpected cost in the Emergency Fund Simulator.
- Use the Forecast and Decision Comparison Lab to explain assumptions and trade-offs.
- The AI Coach needs internet access and a valid API key; model availability and quotas can vary.

## Privacy and limitations

- Do not enter bank account numbers, passwords, or other sensitive personal information.
- Forecasts are simplified scenarios based on user-selected assumptions, not predictions.
- AI-generated text may be inaccurate and should be treated as educational information, not professional financial advice.
- No user financial information is intentionally stored by this prototype; review the behavior of third-party API providers before using real personal data.

## Team

- **Team:** INVICTUS
- **Team ID:** DEX26036
- **Event:** DEXATHON 2026
- **Theme:** FinTech & EdTech

## License

No license has been selected yet. Add a license before permitting reuse or redistribution.

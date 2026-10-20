# 🚀 Asset Atlas

### AI-Powered Financial Resilience and Decision Simulator

**Asset Atlas** is a fintech project focused on helping users understand their financial position and explore how changing income and expenses can affect their financial resilience.

Developed by **Team INVICTUS** for **DEXATHON 2026 — Chennai**, this project aims to make financial planning more interactive, understandable, and accessible.

> **Project status:** Prototype in development

## 🎯 Problem Statement

Unexpected changes in income and rising expenses can make financial planning difficult. People need simple ways to understand their monthly cash flow and explore potential financial scenarios before making decisions.

## 💡 Our Solution

Asset Atlas aims to provide an interactive financial dashboard where users can examine their income, expenses, savings, and monthly balance, then explore hypothetical financial changes.

## ✨ Current Prototype

- 📊 **Financial overview** — View monthly income, expenses, and remaining balance.
- 💰 **Savings insights** — Calculate savings and savings rate from entered financial values.
- 📈 **Interactive visualization** — Explore financial breakdowns using charts.
- 🧪 **Financial stress testing** — Explore hypothetical changes in income and expenses, if enabled in the current version.

*Features are under development and may change as the project evolves.*

## 🛠️ Tech Stack

- **Language:** Python
- **Frontend / Dashboard:** Streamlit
- **Data processing:** Pandas
- **Visualizations:** Plotly
- **Development environment:** Visual Studio Code
- **Version control:** Git and GitHub

## ⚙️ Getting Started

### Prerequisites

- Python 3
- Git
- Visual Studio Code (recommended)

### 1. Clone the repository

```bash
git clone https://github.com/sathvikayalavarthi/asset-atlas.git
cd asset-atlas
```

### 2. Create a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to use the dashboard.

## 📁 Project Structure

```text
asset-atlas/
├── app.py
├── calculations.py
├── requirements.txt
├── README.md
└── .gitignore
```

- `app.py` — Streamlit application and dashboard interface.
- `calculations.py` — Location for financial calculation logic.
- `requirements.txt` — Python dependencies.
- `.gitignore` — Files and folders excluded from version control.

## 🗺️ Roadmap

- [x] Initial Streamlit dashboard
- [x] Basic financial overview and visualization
- [ ] Expand financial stress-testing scenarios
- [ ] Add personalized financial insights
- [ ] Explore AI-assisted financial decision support
- [ ] Improve dashboard design and user experience
- [ ] Deploy a public demo

## 👥 Team

**Team Name:** INVICTUS  
**Team ID:** DEX26036  
**Event:** DEXATHON 2026  
**Theme:** FinTech & EdTech  
**Project Category:** Software

## 🔐 Privacy Note

Use sample or hypothetical financial values while testing. Do not commit passwords, API keys, `.env` files, or sensitive personal financial information to the repository.

## 📌 Disclaimer

Asset Atlas is an educational prototype for exploring financial scenarios. It is not a substitute for professional financial advice.

## 📄 License

No license has been specified yet. Usage and redistribution permissions can be added when a license is selected.

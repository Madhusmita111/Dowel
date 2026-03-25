# Dowel

> **An agentic AI analyst that lives inside your data — answers questions, predicts trends, detects anomalies, and sends alerts. Automatically.**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/FastAPI-0.104+-green?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/LangChain-0.1+-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Streamlit-1.28+-red?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-ready-blue?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/Railway-deployed-purple?style=for-the-badge"/>
</p>

<p align="center">
  <a href="#-demo">Demo</a> •
  <a href="#-features">Features</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-roadmap">Roadmap</a>
</p>

---

## What Is This?

Most data tools tell you **what** happened. Dowel tells you **why** it happened, **what will happen next**, and **what you should do about it**.

You point it at any data source — a CSV, a database, a website, a Google Sheet — type a question in plain English, and get back a complete analysis with charts, predictions, and recommendations.

```
You:  "Why did my sales drop last Tuesday?"

Dowel:  Sales dropped 34% on Tuesday because:
                1. It was a national holiday — historically your
                   sales drop 28% on holidays
                2. Your top SKU went out of stock at 11am
                3. A competitor ran a 40% flash sale that afternoon

                Predicted recovery: Normal levels by Thursday
                Confidence: 82%
```

No data analyst needed. No SQL knowledge needed. Just ask.

---

## Features

### Universal Data Ingestion
- **CSV / Excel** file upload with drag-and-drop
- **SQL Database** connector (PostgreSQL, MySQL, SQLite)
- **Google Sheets** live sync — reads and writes back
- **Web Scraping** — paste any URL, it extracts the data
- **Live APIs** — finance (yfinance), weather (Open-Meteo), and more

### Auto Data Quality Engine
- Detects and fixes missing values intelligently
- Corrects wrong data types automatically
- Unifies inconsistent labels (`"mumbai"`, `"Mumbai"`, `"MUM"` → `"Mumbai"`)
- Removes duplicates with explanation
- Shows exactly what changed and why

### Conversational AI Interface
- Ask questions in plain English
- **RAG memory** — remembers your data across sessions
- Context-aware answers that improve over time
- Follow-up questions with full conversation history

### Text-to-SQL Agent
- Automatically reads your database schema
- Converts English questions to SQL queries
- Executes queries and visualizes results
- Shows the generated SQL for transparency
- Suggests follow-up queries proactively

### ML Forecasting
- Auto-detects if data is time-series, classification, or regression
- Prophet for time-series forecasting (7 / 30 / 90 days)
- XGBoost for structured prediction tasks
- Confidence intervals on all predictions
- Plain English summary of every forecast

### Anomaly Detection
- Isolation Forest for multivariate outliers
- Z-score for statistical anomalies in time-series
- Visual flagging on charts (red markers)
- Explanation of why each point is anomalous

### What-If Scenario Simulator
- Ask: *"What if I increase price by 15%?"*
- Monte Carlo simulation on historical data
- Three scenarios: optimistic / base / pessimistic
- Confidence intervals on each outcome

### Competitor Intelligence
- Add competitor URLs — scraped automatically every 24hrs
- Tracks prices, reviews, job postings
- ML detects pricing patterns and strategic shifts
- Alerts you before you lose customers

### Voice Interface
- Speak your question — Whisper transcribes it
- Answer spoken back via text-to-speech
- Works entirely locally, zero cost

### Automated Alerts
- Slack webhook integration
- Gmail SMTP email alerts
- User-defined threshold rules
- Anomaly-triggered instant notifications

### Auto Weekly Briefing
- Every Monday 9am — full PDF report generated
- Sections: Top Insights, Anomalies, Forecasts, Recommendations
- Charts embedded, emailed automatically

### Multi-User Collaboration
- JWT authentication with role-based permissions
- Shared workspaces and dashboards
- Comments and annotations on charts
- Admin / Analyst / Viewer roles

### Chrome Extension
- Highlight any data table on any webpage
- One click → sends to Dowel workspace
- Results appear instantly in the extension popup

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    STREAMLIT FRONTEND                        │
│     Chat │ Dashboard │ What-If │ Settings │ Voice Input     │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                    FASTAPI BACKEND                           │
│         Data Ingestion │ Auth │ Query Routing                │
└──────┬───────────┬──────────────┬──────────────┬────────────┘
       │           │              │              │
┌──────▼──┐  ┌─────▼──────┐ ┌────▼─────┐  ┌────▼──────────┐
│  DATA   │  │  MEMORY    │ │  AGENTS  │  │  MONITORING   │
│ QUALITY │  │  LAYER     │ │  ENGINE  │  │  ENGINE       │
│         │  │            │ │          │  │               │
│ Auto    │  │ ChromaDB   │ │ Analyst  │  │ Anomaly Det.  │
│ clean   │  │ Embeddings │ │ SQL      │  │ Scheduler     │
│ fix     │  │ RAG Search │ │ Forecast │  │ Alert Sender  │
│ validate│  │            │ │ What-If  │  │ Competitor    │
│         │  │            │ │ Causal   │  │ Scraper       │
│         │  │            │ │ Critic   │  │               │
└─────────┘  └────────────┘ └──────────┘  └───────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                    ML ENGINE                                 │
│         Prophet │ XGBoost │ Isolation Forest │ Monte Carlo  │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                    OUTPUTS                                   │
│    Plotly Charts │ PDF Reports │ Slack │ Email │ Voice       │
└─────────────────────────────────────────────────────────────┘
```

---

## Quick Start

### Prerequisites
- Python 3.11+
- Docker + Docker Compose
- Git

### 1. Clone the repo
```bash
git clone https://github.com/Madhusmita111/dowel.git
cd dowel
```

### 2. Set up environment variables
```bash
cp .env.example .env
```

Edit `.env` with your keys:
```env
# LLM
ANTHROPIC_API_KEY=your_claude_api_key

# Database
POSTGRES_URL=postgresql://user:password@localhost:5432/datawhisperer

# Alerts
SLACK_WEBHOOK_URL=your_slack_webhook
GMAIL_USER=your@gmail.com
GMAIL_PASSWORD=your_app_password

# Auth
JWT_SECRET=your_secret_key

# Google Sheets (optional)
GOOGLE_CREDENTIALS_PATH=credentials.json
```

### 3. Run with Docker
```bash
docker-compose up --build
```

### 4. Open the app
```
Streamlit UI  → http://localhost:8501
FastAPI docs  → http://localhost:8000/docs
```

### 5. Try the demo
Click **"Try Demo"** in the UI — loads a pre-built e-commerce dataset with interesting anomalies, trends, and forecasting opportunities. No signup needed.

---

## Project Structure

```
datawhisperer/
├── frontend/
│   ├── app.py                  # Main Streamlit app
│   ├── pages/
│   │   ├── chat.py             # Conversational interface
│   │   ├── dashboard.py        # Auto visualizations
│   │   ├── whatif.py           # Scenario simulator
│   │   └── settings.py         # User preferences + alerts
│   └── components/
│       ├── voice_recorder.py   # Whisper integration
│       └── chart_builder.py    # Plotly chart factory
├── backend/
│   ├── main.py                 # FastAPI entry point
│   ├── auth/
│   │   └── jwt_handler.py      # JWT authentication
│   ├── ingestion/
│   │   ├── file_loader.py      # CSV / Excel
│   │   ├── sql_connector.py    # Database connections
│   │   ├── sheets_connector.py # Google Sheets API
│   │   └── web_scraper.py      # Playwright scraper
│   ├── quality/
│   │   └── data_cleaner.py     # Auto data quality engine
│   ├── memory/
│   │   ├── embedder.py         # Text → vector embeddings
│   │   ├── vector_store.py     # ChromaDB operations
│   │   └── retriever.py        # Semantic search
│   ├── agents/
│   │   ├── analyst_agent.py    # Main RAG reasoning agent
│   │   ├── sql_agent.py        # Text-to-SQL agent
│   │   ├── causal_agent.py     # Why did X happen?
│   │   ├── forecast_agent.py   # Trend prediction
│   │   ├── whatif_agent.py     # Scenario simulation
│   │   └── critic_agent.py     # Validates conclusions
│   ├── ml/
│   │   ├── model_selector.py   # Auto ML type detection
│   │   ├── forecaster.py       # Prophet + XGBoost
│   │   └── anomaly_detector.py # Isolation Forest + Z-score
│   ├── monitoring/
│   │   ├── scheduler.py        # APScheduler jobs
│   │   ├── alert_sender.py     # Slack + Email
│   │   └── competitor_scraper.py # Competitor tracking
│   ├── reports/
│   │   └── pdf_generator.py    # Weekly PDF briefing
│   └── cloud/
│       └── storage_handler.py  # File storage
├── extension/                  # Chrome extension
│   ├── manifest.json
│   ├── popup.html
│   └── content.js
├── tests/
│   ├── test_ingestion.py
│   ├── test_agents.py
│   └── test_ml.py
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Frontend | Streamlit | Web UI + chat interface |
| Backend | FastAPI | REST API + async routing |
| LLM | Claude API (Anthropic) | Reasoning + narration |
| Agents | LangChain | Multi-agent orchestration |
| Memory | ChromaDB + sentence-transformers | RAG vector search |
| ML | Prophet + XGBoost + scikit-learn | Forecasting + prediction |
| Anomaly | Isolation Forest + Z-score | Outlier detection |
| Simulation | Monte Carlo (numpy) | What-if scenarios |
| Database | PostgreSQL + SQLAlchemy | Structured data storage |
| Scraping | Playwright + BeautifulSoup | Web + competitor data |
| Voice | OpenAI Whisper + pyttsx3 | Speech I/O (local) |
| Sheets | gspread | Google Sheets sync |
| Auth | fastapi-users + JWT | Multi-user auth |
| Alerts | Slack Webhooks + smtplib | Notifications |
| Reports | ReportLab | PDF generation |
| Scheduler | APScheduler | Background jobs |
| Cache | Redis | Query caching |
| Container | Docker + docker-compose | Deployment |
| Cloud | Railway.app | Hosting (free tier) |

---

## Roadmap

### v1.0 — Core Intelligence
- [x] File upload + SQL connector
- [x] Auto data quality engine
- [x] RAG memory + conversational chat
- [x] Text-to-SQL agent
- [x] ML forecasting (Prophet + XGBoost)
- [x] Anomaly detection
- [x] What-if scenario simulator
- [x] Causal + Critic agents
- [x] Railway deployment

### v1.5 — Power Features
- [x] Voice input/output (Whisper)
- [x] Competitor intelligence scraper
- [x] Slack + Email automated alerts
- [x] Weekly PDF auto-briefing
- [x] Multi-user auth + collaboration
- [x] Google Sheets live sync
- [x] Redis caching

### v2.0 — Expansion
- [ ] Chrome browser extension
- [ ] Mobile-responsive UI
- [ ] Fine-tuned domain-specific models
- [ ] Multi-language support (Hindi + English NLP)
- [ ] Zapier / n8n workflow integration
- [ ] Public API for third-party integrations
- [ ] SaaS pricing + billing (Stripe)

---

## Example Use Cases

**E-commerce Business**
> *"Which products are most likely to go out of stock next month?"*
> *"Why did cart abandonment spike on Friday?"*
> *"What's the revenue impact if I offer free shipping?"*

**Finance / Trading**
> *"Are Indian EV stocks showing a bullish pattern?"*
> *"Which of my portfolio holdings have anomalous volume today?"*
> *"Forecast NIFTY 50 for the next 30 days"*

**Operations / Logistics**
> *"Which delivery routes have the highest delay rate?"*
> *"Predict demand for next quarter by region"*
> *"Alert me if delivery SLA breaches exceed 5%"*

**Marketing**
> *"Which campaigns had the best ROI last quarter?"*
> *"Is our competitor running a promotion right now?"*
> *"What's the correlation between ad spend and revenue?"*

---

## Contributing

Contributions are welcome! Here's how:

```bash
# Fork the repo
# Create your feature branch
git checkout -b feature/amazing-feature

# Commit your changes
git commit -m "Add amazing feature"

# Push to the branch
git push origin feature/amazing-feature

# Open a Pull Request
```

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and submission process.

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- [LangChain](https://langchain.com) — Agent orchestration framework
- [Anthropic](https://anthropic.com) — Claude LLM API
- [ChromaDB](https://trychroma.com) — Vector database
- [Prophet](https://facebook.github.io/prophet) — Time series forecasting
- [Streamlit](https://streamlit.io) — Frontend framework
- [Railway](https://railway.app) — Cloud deployment

---

<p align="center">
  Built by Madhusmita Talukdar
</p>

<p align="center">
  <a href="https://linkedin.com/in/yourprofile">LinkedIn</a> •
  <a href="https://twitter.com/yourhandle">Twitter</a> •
  <a href="mailto:your@email.com">Email</a>
</p># Dowel

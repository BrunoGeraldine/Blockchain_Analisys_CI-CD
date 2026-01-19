# Blockchain_Analisys_CI-CD

## On-Chain Risk & Activity Monitor

### 📌 Overview
The **On-Chain Risk & Activity Monitor** is an end-to-end data engineering and analytics project focused on **on-chain activity analysis, automated smart contract auditing, and real-time risk monitoring** for Ethereum-compatible blockchains.

The project simulates a real-world **DeFi / Web3 risk monitoring platform**, combining blockchain data ingestion, scalable analytics, automated audits, and alerting pipelines.

This repository showcases skills in:
- Blockchain data engineering
- On-chain analytics
- Smart contract risk assessment
- Automation and orchestration
- Modern data stack used by US-based Web3 and FinTech companies

---

### 🎯 Objectives
- Ingest on-chain transaction and contract data
- Build analytical models to detect anomalies and risks
- Implement automated audit rules for smart contracts
- Generate real-time alerts for suspicious behavior
- Expose clean analytics-ready data via APIs

---

### 🏗️ Architecture

Blockchain (Ethereum / Polygon)
        ↓
n8n (ingestão + automação)
        ↓
Databricks Free (ETL + analytics)
        ↓
Supabase (DB + API + Auth)
        ↓
Dashboards / Alerts
        ↓
GitHub Actions (CI/CD + qualidade)


---

## 🧱 Tech Stack

### Blockchain & Data
- Ethereum / Polygon
- Etherscan API
- RPC Providers (Alchemy / Infura)

### Data Engineering
- Databricks Free Edition
- PySpark
- Delta Tables

### Automation & Orchestration
- n8n
- Webhooks & Schedulers

### Storage & API
- Supabase (PostgreSQL, REST API, Auth)

### DevOps & Quality
- GitHub Actions
- Python (pytest, lint)
- SQL validation

---

## 🔍 Core Features

### 1. On-Chain Data Ingestion
- Transactions
- ERC-20 / ERC-721 events
- Contract interactions
- Ownership and permission changes

### 2. Analytics & Metrics
- Active wallets
- Token concentration (whales)
- Gas usage anomalies
- Function call frequency
- Contract interaction trends

### 3. Automated Smart Contract Audits
Rule-based risk detection:
- Ownership centralization
- Upgradeable proxy risks
- Missing access controls
- Abnormal token flows
- Suspicious approvals

Each contract receives a **risk score (0–100)** and severity level.

### 4. Alerting System
- High-risk contract detection
- Whale movements
- Contract upgrades
- Ownership changes

Alerts delivered via:
- Email
- Discord / Slack
- Webhooks

---

## 📊 Data Model (Simplified)

### Tables
- `contracts`
- `transactions`
- `token_transfers`
- `risk_scores`
- `alerts`

---

## 🚀 Getting Started

### Prerequisites
- Databricks Free Account
- Supabase Account
- n8n (Cloud or Self-hosted)
- GitHub Account
- Ethereum RPC API Key (Alchemy / Infura)

### Steps
1. Clone the repository
2. Configure environment variables
3. Run n8n ingestion workflows
4. Execute Databricks ETL notebooks
5. Load curated data into Supabase
6. Enable alert workflows

---

## 📁 Repository Structure
├── databricks/
│ ├── bronze_ingestion.py
│ ├── silver_transformation.py
│ └── gold_analytics.py
├── n8n/
│ ├── ingest_transactions.json
│ └── alert_workflows.json
├── supabase/
│ └── schema.sql
├── audits/
│ └── risk_rules.py
├── tests/
│ └── test_data_quality.py
├── .github/
│ └── workflows/
│ └── ci.yml
└── README.md




---

## 📈 Future Improvements
- Cross-chain analytics
- Machine learning anomaly detection
- Chainlink price feeds
- Dashboard UI (Metabase / Streamlit)
- Real-time streaming ingestion

---

## 👤 Author
**Bruno Geraldine**  
Blockchain Data Engineer | Analytics Engineer | Data Engineer  
🇮🇹 Italy | Open to US opportunities 🇺🇸

LinkedIn: https://www.linkedin.com/in/brunogeraldine/ 
GitHub: https://github.com/BrunoGeraldine



📌 Próximo passo lógico (ordem recomendada)

1️⃣ Criar workflow n8n de ingestão (Etherscan)
docker : 
docker compose down (torn-off)
docker compose pull (deploy)
docker compose up -d (torn-on)
http://localhost:5678


2️⃣ Criar notebook Databricks Bronze → Silver
3️⃣ Integrar risk_rules.py no Gold layer
4️⃣ Criar alerta automático no n8n
5️⃣ Adicionar GitHub Actions (tests + lint)
-- =========================
-- CORE TABLES
-- =========================

CREATE TABLE contracts (
    contract_address TEXT PRIMARY KEY,
    chain TEXT NOT NULL,
    contract_name TEXT,
    creator_address TEXT,
    creation_tx TEXT,
    is_proxy BOOLEAN DEFAULT FALSE,
    owner_address TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE transactions (
    tx_hash TEXT PRIMARY KEY,
    block_number BIGINT,
    block_timestamp TIMESTAMP,
    from_address TEXT,
    to_address TEXT,
    value_eth NUMERIC,
    gas_used BIGINT,
    gas_price BIGINT,
    status BOOLEAN,
    chain TEXT
);

CREATE TABLE token_transfers (
    tx_hash TEXT,
    token_address TEXT,
    from_address TEXT,
    to_address TEXT,
    amount NUMERIC,
    token_symbol TEXT,
    block_timestamp TIMESTAMP
);

-- =========================
-- AUDIT & RISK
-- =========================

CREATE TABLE risk_scores (
    contract_address TEXT,
    risk_score INTEGER CHECK (risk_score BETWEEN 0 AND 100),
    risk_level TEXT,
    issues JSONB,
    evaluated_at TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY (contract_address, evaluated_at)
);

CREATE TABLE alerts (
    alert_id SERIAL PRIMARY KEY,
    contract_address TEXT,
    alert_type TEXT,
    severity TEXT,
    description TEXT,
    triggered_at TIMESTAMP DEFAULT NOW(),
    resolved BOOLEAN DEFAULT FALSE
);

-- =========================
-- INDEXES (PERFORMANCE)
-- =========================

CREATE INDEX idx_transactions_block_time
    ON transactions(block_timestamp);

CREATE INDEX idx_token_transfers_token
    ON token_transfers(token_address);

CREATE INDEX idx_alerts_severity
    ON alerts(severity);

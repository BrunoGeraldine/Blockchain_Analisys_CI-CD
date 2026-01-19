from typing import Dict, List

# =========================
# RISK RULES ENGINE
# =========================

def check_owner_centralization(contract: Dict) -> Dict:
    """
    Detects if a contract has a single powerful owner.
    """
    issues = []
    score = 0

    if contract.get("owner_address"):
        score += 20
        issues.append("Contract has a centralized owner")

    return {
        "rule": "owner_centralization",
        "score": score,
        "issues": issues
    }


def check_proxy_risk(contract: Dict) -> Dict:
    """
    Detects upgradeable proxy without timelock.
    """
    issues = []
    score = 0

    if contract.get("is_proxy"):
        score += 30
        issues.append("Upgradeable proxy detected")

        if not contract.get("has_timelock", False):
            score += 20
            issues.append("Proxy without timelock")

    return {
        "rule": "proxy_risk",
        "score": score,
        "issues": issues
    }


def check_whale_activity(transfers: List[Dict]) -> Dict:
    """
    Detects abnormal token concentration.
    """
    issues = []
    score = 0

    large_transfers = [
        t for t in transfers if t["amount"] > 1_000_000
    ]

    if len(large_transfers) > 5:
        score += 25
        issues.append("High volume of whale transfers detected")

    return {
        "rule": "whale_activity",
        "score": score,
        "issues": issues
    }


def calculate_risk_score(contract: Dict, transfers: List[Dict]) -> Dict:
    """
    Aggregates all risk rules into a final score.
    """
    rules = [
        check_owner_centralization(contract),
        check_proxy_risk(contract),
        check_whale_activity(transfers)
    ]

    total_score = sum(rule["score"] for rule in rules)
    total_score = min(total_score, 100)

    if total_score >= 70:
        level = "HIGH"
    elif total_score >= 40:
        level = "MEDIUM"
    else:
        level = "LOW"

    issues = {
        rule["rule"]: rule["issues"]
        for rule in rules if rule["issues"]
    }

    return {
        "contract_address": contract["contract_address"],
        "risk_score": total_score,
        "risk_level": level,
        "issues": issues
    }

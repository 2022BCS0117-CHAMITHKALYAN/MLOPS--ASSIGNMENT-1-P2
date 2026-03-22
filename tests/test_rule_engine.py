from src.rule_engine import evaluate_risk

def test_high_risk_many_tickets():
    row = {
        "contract_type": "Month-to-month",
        "tickets_last_30_days": 7,
        "complaint_ticket": 0
    }
    assert evaluate_risk(row) == "HIGH"


def test_high_risk_complaint():
    row = {
        "contract_type": "Month-to-month",
        "tickets_last_30_days": 2,
        "complaint_ticket": 1
    }
    assert evaluate_risk(row) == "HIGH"


def test_medium_risk():
    row = {
        "contract_type": "Two year",
        "tickets_last_30_days": 3,
        "complaint_ticket": 0
    }
    assert evaluate_risk(row) == "MEDIUM"


def test_low_risk():
    row = {
        "contract_type": "Two year",
        "tickets_last_30_days": 1,
        "complaint_ticket": 0
    }
    assert evaluate_risk(row) == "LOW"


def test_boundary_condition():
    row = {
        "contract_type": "Two year",
        "tickets_last_30_days": 5,
        "complaint_ticket": 0
    }
    assert evaluate_risk(row) == "MEDIUM"


def test_rule_priority():
    row = {
        "contract_type": "Month-to-month",
        "tickets_last_30_days": 3,
        "complaint_ticket": 1
    }
    assert evaluate_risk(row) == "HIGH"


def test_complaint_without_monthly():
    row = {
        "contract_type": "Two year",
        "tickets_last_30_days": 2,
        "complaint_ticket": 1
    }
    assert evaluate_risk(row) == "LOW"
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from datetime import datetime, timedelta
from src.rule_engine import evaluate_risk


# -----------------------------
# Logging configuration
# -----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger("churn-risk-service")

app = FastAPI(
    title="Churn Risk Prediction Service",
    description="Rule-based churn risk prediction API",
    version="1.0"
)

customers = pd.read_csv("data/refined/customers.csv")
tickets = pd.read_csv("data/refined/support_tickets.csv")
tickets["created_at"] = pd.to_datetime(tickets["created_at"])

class CustomerRequest(BaseModel):
    customer_id: str

@app.get("/")
def health_check():
    return {"status": "service running"}

def compute_features(customer_id):
    customer_row = customers[customers["customer_id"] == customer_id]
    if customer_row.empty:
        raise HTTPException(status_code=404, detail="Customer not found")

    customer_tickets = tickets[tickets["customer_id"] == customer_id]
    now = datetime.now()
    window_30 = now - timedelta(days=30)

    tickets_last_30_days = len(customer_tickets[customer_tickets["created_at"] > window_30])
    complaint_ticket = int((customer_tickets["ticket_type"] == "complaint").any())

    if len(customer_tickets) > 0:
        negative_ratio = (customer_tickets["sentiment"] == "negative").sum() / len(customer_tickets)
    else:
        negative_ratio = 0

    return {
        "contract_type": customer_row.iloc[0]["contract_type"],
        "tickets_last_30_days": tickets_last_30_days,
        "complaint_ticket": complaint_ticket,
        "negative_ratio": negative_ratio
    }

@app.post("/predict-risk")
def predict_risk(request: CustomerRequest):
    features = compute_features(request.customer_id)
    risk = evaluate_risk(features)
    return {
        "customer_id": request.customer_id,
        "risk_category": risk
    }

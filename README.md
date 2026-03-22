# Churn Risk Intelligence Service  
### DevOps + MLOps Architecture Assignment

**Name:** B. Chamith Kalyan  
**Roll No:** 2022BCS0117  

---

## Overview

This project presents a **Churn Risk Intelligence Service** designed as a production-style system that combines:

- a **rule-driven backend** for churn risk estimation,
- a **DevOps workflow** for build, test, deploy, and monitor,
- and an **MLOps-ready design** for future model training and lifecycle management.

The goal is to show how a simple prediction service can evolve from a basic API into a reliable, scalable, and observable machine learning system.

---

## Project Highlights

- REST API for churn risk prediction
- Rule-based decision logic for current inference
- Clean DevOps delivery pipeline
- Container-based deployment
- Automated testing
- Metrics collection and monitoring
- MLOps-friendly architecture for future expansion

---

## Architecture at a Glance

| Layer | What It Does |
|------|--------------|
| Application Layer | Receives user requests and returns churn risk |
| Decision Layer | Applies business rules to estimate risk |
| DevOps Layer | Builds, tests, packages, and deploys the service |
| Observability Layer | Tracks API health, latency, and usage |
| MLOps Layer | Supports training, evaluation, and model lifecycle |

---

## 1. DevOps Architecture

<p align="center">
  <img src="assets/devops.jpg" alt="DevOps Architecture Diagram" width="95%">
</p>

### What this architecture shows

The DevOps setup focuses on delivering the service reliably from source code to deployment.

**Flow:**  
Source Code → CI Pipeline → Docker Image → Deployment → Monitoring

### Main components

- **Git repository** for source control
- **CI pipeline** for automated build and testing
- **Docker** for packaging the service
- **Deployment stage** for running the application
- **Monitoring tools** for system visibility

### Why it matters

This architecture ensures that every code change can be tested, packaged, and delivered in a repeatable way.

---

## 2. ML-Ready Architecture

<p align="center">
  <img src="assets/ml.jpg" alt="ML Architecture Diagram" width="95%">
</p>

### What changes when ML is introduced

The rule engine can later be replaced or enhanced by a trained model.  
At that stage, the system includes:

- data collection
- feature engineering
- model training
- model evaluation
- model storage
- inference API

### ML pipeline flow

Dataset → Data Cleaning → Feature Engineering → Training → Evaluation → Saved Model → Inference API

### Key idea

Unlike simple backend logic, ML systems depend heavily on data quality and model performance over time.

---

## 3. MLOps Production Architecture

<p align="center">
  <img src="assets/mlops.jpg" alt="MLOps Architecture Diagram" width="95%">
</p>

### Purpose

This layer adds the operational discipline needed to run ML in real-world production environments.

### Added capabilities

- dataset versioning
- experiment tracking
- model registry
- drift monitoring
- automated retraining
- continuous validation

### Result

The system does not just deploy a model once; it keeps checking whether the model is still accurate and useful.

---

## Why DevOps Alone Is Not Enough

Traditional DevOps works very well for code-based applications, but ML systems behave differently.

### DevOps assumes:
- code is the main source of behavior
- tests are enough to confirm correctness
- output stays stable unless code changes

### ML systems break that assumption because:
- data changes affect predictions
- retraining changes model behavior
- accuracy can decline silently
- bugs can come from data, not only code

That is why **MLOps** is needed alongside DevOps.

---

## Risks Introduced by ML Systems

### Data Risks
- biased training samples
- noisy labels
- data drift
- feature mismatch

### Operational Risks
- model version confusion
- non-reproducible training runs
- silent degradation in performance

### Business Risks
- wrong churn predictions
- unstable decision-making
- hidden technical debt in the pipeline

---

## Feature Design

The service uses customer and support-related inputs to estimate churn risk.

| Feature | Description |
|--------|-------------|
| `contract_type` | Customer plan type |
| `ticket_count_30d` | Number of support tickets in the last 30 days |
| `complaint_flag` | Indicates complaint history |
| `negative_feedback_ratio` | Portion of negative interactions |
| `usage_stability` | Measures consistency of service usage |

---

## Risk Classification Logic

| Condition | Risk Level |
|----------|------------|
| Frequent complaints + short contract | High |
| Moderate support activity | Medium |
| Stable usage + long-term contract | Low |

---

## API Endpoints

### Base URL

```bash
http://localhost:8000


| Endpoint        | Method | Purpose                       |
| --------------- | ------ | ----------------------------- |
| `/`             | GET    | Health check                  |
| `/predict-risk` | POST   | Predict churn risk            |
| `/metrics`      | GET    | Expose Prometheus metrics     |
| `/docs`         | GET    | Interactive API documentation |


```

## Repository Structure
project-root
│
├── src
│   ├── app.py
│   ├── rule_engine.py
│   └── feature_pipeline.py
│
├── data
│   ├── raw
│   └── processed
│
├── scripts
│   ├── prepare_customers.py
│   ├── generate_tickets.py
│   └── validate_tickets.py
│
├── tests
│   ├── test_api.py
│   └── test_rule_engine.py
│
├── monitoring
│   ├── prometheus.yml
│   └── docker-compose.monitoring.yml
│
├── grafana
│   └── dashboard.json
│
├── assets
│   ├── banner.png
│   ├── devops.jpg
│   ├── ml.jpg
│   ├── mlops.jpg
│   └── monitoring-dashboard.png
│
└── README.md

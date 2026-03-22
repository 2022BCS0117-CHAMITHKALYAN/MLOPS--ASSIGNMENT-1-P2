# [cite_start]MLOps Assignment Part 1 - Architecture Summaries [cite: 1]

[cite_start]**Author:** Bolli Chamith Kalyan (2022BCS0117) [cite: 2, 3]

## Overview
[cite_start]This repository contains architecture diagrams and written explanations detailing the transition from a traditional rule-based DevOps system to a fully functioning MLOps pipeline[cite: 1, 40].

## Architecture Evolution

### [cite_start]1. DevOps Architecture (Rule-Based System) [cite: 4]
* [cite_start]This architecture represents a simple backend system with no model training pipeline[cite: 16].
* [cite_start]Churn risk is calculated entirely using predefined business rules and deterministic logic[cite: 16].

### [cite_start]2. ML Architecture (Model Introduced) [cite: 17]
* [cite_start]The rule-based engine is replaced with an ML inference system[cite: 31].
* [cite_start]The updated architecture includes feature engineering and a training pipeline[cite: 32].
* [cite_start]It utilizes a stored model artifact and evaluates performance using metrics like F1 score, ROC-AUC, and Precision-Recall[cite: 32].

### [cite_start]3. MLOps Architecture (Production ML System) [cite: 33]
* [cite_start]This final architecture adds model lifecycle control and dataset version tracking[cite: 35, 37].
* [cite_start]It incorporates monitoring alongside automated retraining cycles[cite: 38].
* [cite_start]The system is designed for ongoing performance evaluation[cite: 39].

## [cite_start]Key Concepts & Explanations [cite: 40]

### [cite_start]What broke when ML was added? [cite: 41]
* [cite_start]**Before ML:** The system was predictable; the same input always produced the same output due to fixed rules[cite: 42, 43].
* [cite_start]**After ML:** The system's output now heavily depends on the training data[cite: 44, 45].
* [cite_start]Model behavior inherently changes after retraining, which makes reproducibility much harder[cite: 46, 47].
* [cite_start]Debugging shifts its focus to analyzing data rather than just reviewing code[cite: 48].
* [cite_start]ML introduces new risks like data drift, feature mismatch, model version confusion, and silent performance drops[cite: 49, 50, 51, 52, 53].
* [cite_start]While DevOps manages code changes, ML introduces complex statistical behavior changes[cite: 54].

### [cite_start]Why is DevOps alone insufficient? [cite: 55]
* [cite_start]DevOps assumes that code strictly defines system behavior and that tests can verify correctness[cite: 56, 57, 58].
* [cite_start]ML breaks this assumption because data influences behavior much more than code does[cite: 59, 60].
* [cite_start]Model accuracy cannot be unit-tested like regular functions, and performance can decline over time even without any code changes[cite: 61].
* [cite_start]DevOps mainly manages deployment, infrastructure, and API lifecycles[cite: 62, 63, 64, 65].
* [cite_start]ML systems additionally require data lineage tracking, experiment tracking, model validation, and continuous monitoring and evaluation[cite: 66, 67, 68, 69, 70].
* [cite_start]Without MLOps, teams deploy a model once but completely lose visibility into its real-world performance[cite: 71].

### [cite_start]What new risks does ML introduce? [cite: 72]
* [cite_start]**Data Risks:** Systems are vulnerable to training data bias, distribution shifts, and noisy or incorrect labels[cite: 73, 74, 75, 76].
* [cite_start]**Operational Risks:** Teams face issues like model drift without alerts, feature engineering mismatches, and non-reproducible training runs[cite: 77, 78, 79, 80].
* [cite_start]**Business Risks:** There can be false positives in churn prediction, unstable decisions caused by overfitting, and hidden technical debt in ML pipelines[cite: 81, 82, 83, 84].
* [cite_start]**The Key Shift:** Traditional backend failures are usually binary (either working or broken), whereas ML failures are gradual and often go unnoticed until performance metrics drop significantly[cite: 85, 86].

# 📈 Market Data Latency Monitoring Simulator

A lightweight, Kubernetes-ready system that simulates market data feeds and tracks message latency in real time — inspired by infrastructure and reliability challenges in electronic trading environments.

---

## 🚀 Project Overview

This project simulates a simplified market data system:
- A **Feed Generator** sends fake bid/ask data via Redis.
- A **Consumer** processes this feed and calculates **message latency**.
- Metrics are exposed via `/metrics` and scraped by **Prometheus**.
- **Grafana** provides a real-time dashboard for latency, throughput, and loss detection.

---

## 🧱 Architecture

![architecture-diagram](./monitoring/architecture.png) <!-- Add your diagram here -->

---

## 📦 Stack

| Component     | Technology     |
|---------------|----------------|
| Feed Simulator | Python + FastAPI |
| Messaging      | Redis (pub/sub)  |
| Consumer       | Python + Prometheus client |
| Monitoring     | Prometheus + Grafana |
| Containerization | Docker + Kubernetes |

---

## 🛠️ Getting Started

### Prerequisites

- Docker
- Kubernetes (e.g., `minikube`, `kind`, or a dev cluster)
- `kubectl`
- (Optional) Helm

### 1. Clone the Repo

```bash
git clone https://github.com/yourname/market-data-latency-sim.git
cd market-data-latency-sim

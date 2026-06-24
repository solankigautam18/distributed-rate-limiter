# Distributed Rate Limiter

A production-oriented distributed rate limiting service built using FastAPI, Redis, and Python.

The system provides centralized request throttling for APIs and microservices using Redis-backed state management, supporting high-concurrency environments and distributed deployments.

---

## Overview

This project simulates how large-scale backend systems enforce API request limits across multiple application instances.

The service is designed to:

- Prevent API abuse
- Control traffic spikes
- Protect downstream services
- Improve platform reliability
- Support distributed deployments

The implementation leverages Redis as a centralized state store, allowing multiple application nodes to share rate limit counters consistently.

---

## Architecture

```text
                +------------------+
                |   Client Apps    |
                +--------+---------+
                         |
                         v
                +------------------+
                |    FastAPI API   |
                +--------+---------+
                         |
                         v
                +------------------+
                |      Redis       |
                | Shared Counters  |
                +------------------+
```

---

## Features

### Current Features

- Fixed Window Rate Limiting
- Redis-backed counter storage
- Configurable request thresholds
- User-based rate limiting
- FastAPI REST API
- Low-latency Redis operations

### Planned Features

- Sliding Window Algorithm
- Token Bucket Algorithm
- Distributed Locking
- Dynamic Configuration
- API Keys & Authentication
- Prometheus Metrics
- Grafana Dashboards
- Docker Deployment
- Kubernetes Deployment
- CI/CD Integration
- Load Testing Suite

---

## Technology Stack

| Component | Technology |
|------------|------------|
| Language | Python 3.12 |
| Framework | FastAPI |
| Data Store | Redis |
| API Server | Uvicorn |
| Version Control | Git |
| Containerization | Docker (Planned) |
| Orchestration | Kubernetes (Planned) |

---

## Project Structure

```text
distributed-rate-limiter/
│
├── app/
│   ├── main.py
│   ├── redis_client.py
│   └── limiter.py
│
├── tests/
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/distributed-rate-limiter.git

cd distributed-rate-limiter
```

### Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Redis

### Mac

```bash
brew services start redis
```

### Verify

```bash
redis-cli ping
```

Expected output:

```text
PONG
```

---

## Run Application

```bash
uvicorn app.main:app --reload
```

Application:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Example Request

```bash
curl "http://127.0.0.1:8000/check?user_id=gautam"
```

Response:

```json
{
  "allowed": true
}
```

---

## Example Flow

Request 1

```json
{
  "allowed": true
}
```

Request 2

```json
{
  "allowed": true
}
```

Request 6 (after threshold)

```json
{
  "allowed": false
}
```

---

## Reliability Considerations

This project focuses on concepts commonly used in Site Reliability Engineering and Platform Engineering:

- Distributed state management
- Request throttling
- Traffic protection
- Redis performance optimization
- Service reliability
- Backend scalability
- Fault tolerance principles
- Production observability

---

## Future Enhancements

### Observability

- Prometheus Metrics
- Grafana Dashboards
- Alerting Rules

### Reliability

- Circuit Breakers
- Retry Logic
- Failover Handling

### Cloud Native

- Docker
- Kubernetes
- Helm Charts

### DevOps

- GitHub Actions
- Automated Testing
- Continuous Deployment

---

## Author

**Gautam Solanki**

LinkedIn:
https://www.linkedin.com/in/gautam-solanki-84763520a/

GitHub:
https://github.com/solankigautam18
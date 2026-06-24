# Distributed Rate Limiter

A Redis-backed distributed rate limiting service built with FastAPI and Python, implementing the Token Bucket algorithm for scalable API traffic control.

## Overview

This project demonstrates how modern backend systems enforce request quotas and protect services from traffic spikes in distributed environments.

The service maintains per-user token buckets in Redis and dynamically refills tokens over time, allowing controlled request throughput while supporting horizontal scalability.

## Features

- Token Bucket rate limiting algorithm
- Redis-backed centralized state management
- FastAPI REST endpoints
- Per-user request throttling
- Automatic token refill mechanism
- Low-latency request processing
- Designed for distributed deployments
- Extensible architecture for Kubernetes and cloud environments

## Architecture

```text
Client Request
      │
      ▼
FastAPI Application
      │
      ▼
Token Bucket Engine
      │
      ▼
Redis Storage
      │
      ▼
Allow / Reject Request
```

## Tech Stack

| Component | Technology |
|------------|------------|
| API Framework | FastAPI |
| Language | Python 3.12 |
| State Store | Redis |
| Server | Uvicorn |
| Version Control | Git |
| Package Management | pip |

## Project Structure

```text
distributed-rate-limiter/
│
├── app/
│   ├── main.py
│   ├── limiter.py
│   ├── redis_client.py
│   └── __init__.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## How It Works

Each user receives a token bucket with:

- Capacity: 10 tokens
- Refill Rate: 1 token per second

Request flow:

1. User sends API request.
2. Service retrieves bucket state from Redis.
3. Available tokens are recalculated.
4. If tokens exist:
   - Request allowed
   - Token count decremented
5. If bucket is empty:
   - Request rejected

## API Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
  "message": "Rate Limiter Running"
}
```

### Rate Limit Check

```http
GET /check?user_id=gautam
```

Response:

```json
{
  "user": "gautam",
  "allowed": true
}
```

or

```json
{
  "user": "gautam",
  "allowed": false
}
```

## Local Setup

### Clone Repository

```bash
git clone https://github.com/<username>/distributed-rate-limiter.git
cd distributed-rate-limiter
```

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Redis

```bash
brew services start redis
```

Verify:

```bash
redis-cli ping
```

Expected:

```text
PONG
```

### Run Application

```bash
uvicorn app.main:app --reload
```

Application:

```text
http://127.0.0.1:8000
```

## Example Redis State

```bash
HGETALL user:gautam
```

```text
tokens
7.34

last_refill
1750845123.32
```

## Future Improvements

- Atomic Redis Lua scripts
- Sliding Window algorithm
- Distributed worker support
- Docker containerization
- Kubernetes deployment
- Prometheus metrics
- Grafana dashboards
- CI/CD pipeline using GitHub Actions
- Load testing with Locust

## Engineering Concepts Demonstrated

- Distributed Systems
- Rate Limiting
- Backend Development
- Redis Data Structures
- API Design
- Reliability Engineering
- Scalability Patterns
- Traffic Management
- State Management
- System Design Fundamentals

## Author

**Gautam Solanki**

LinkedIn: https://www.linkedin.com/in/gautam-solanki-84763520a/

GitHub: https://github.com/solankigautam18
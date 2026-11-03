
# SentinelOps

Secure Cloud Infrastructure & Reliability Lab

## Overview

SentinelOps is a hands-on software engineering project focused on
cloud infrastructure, DevOps, site reliability, and security.

The goal is to build, deploy, secure, monitor, and troubleshoot
a cloud-based application while documenting architectural decisions
and lessons learned.

## Current Features

- REST API built with Python and FastAPI
- Health check endpoint (`GET /health`)
- Automated testing with pytest

## Planned Features

- PostgreSQL database integration
- Docker containerization
- AWS deployment with Terraform
- CI/CD pipelines using GitHub Actions
- Secure secrets management and least-privilege IAM
- Automated security scanning
- Monitoring with Prometheus and Grafana
- Controlled failure simulations and incident reports

## Getting Started

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install fastapi uvicorn pytest httpx2
```

Run the API:

```bash
python -m uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/health`.

Run tests:

```bash
python -m pytest -v
```

## Project Status

Early development — Phase 1: Software Engineering.

## Learning Philosophy

Every architectural decision will be documented and justified.
The project will include controlled experiments, failures,
troubleshooting, and continuous improvements.
# OpenEnv Support Environment

---
Title: OpenEnv Support Env
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

## Overview

This environment simulates real-world customer support workflows including:

- Ticket classification
- Response drafting
- Issue resolution


## Observation Space

- ticket_id: int
- message: str
- status: str

## Action Space

- classify
- reply
- escalate

## Tasks

1. Easy: classify_ticket
2. Medium: draft_response
3. Hard: resolve_ticket

## Reward Design

- Incremental rewards for:
  - Correct classification
  - Good response
  - Full resolution
- Penalties:
  - Repeated actions
  - Invalid actions

## Setup

```bash
pip install -r requirements.txt
export HF_TOKEN=your_token
python inference.py
```

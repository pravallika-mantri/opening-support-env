
---
Title: OpenEnv Support Env
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---


# OpenEnv Support Environment

## Overview

This environment simulates a customer support workflow including ticket classification, response generation, and issue resolution.

## Observation Space

* ticket_id (int)
* message (str)
* status (str)

## Action Space

* classify
* reply
* resolve

## Tasks

* Easy: classify_ticket
* Medium: draft_response
* Hard: resolve_ticket
  

## Output Format

```
[START] ...
[STEP] ...
[END] ...
```


## Demo
Click "Run Simulation" on Hugging Face Space to see execution output.

## Setup

```bash
pip install -r requirements.txt
export HF_TOKEN=your_token
python inference.py
```

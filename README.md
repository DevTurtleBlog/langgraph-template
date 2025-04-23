# Requirements

## Python

Version of Python >=3.11 and <4.0

## LangGraph CLI

pip install langgraph-cli

# Setup

## Setup API Keys

export LANGSMITH_API_KEY="your-api-key"

export PYTHONPATH="./src"

## Create python virtual environment

python3 -m venv .venv

## Activate virtual environment

### Mac
source .venv/bin/activate

### Windows
.venv\Scripts\activate

## Install dependencies

pip install -e .

# Run langgraph

langgraph dev
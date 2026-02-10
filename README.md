# Electricity Price API Challenge

A simple web API that returns the mean electricity price for a given Australian state based on historical CSV data.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

The API will be available at:
http://127.0.0.1:8000

## Example request

```bash
curl "http://127.0.0.1:8000/prices/mean?state=VIC"
```

Example response:

```bash
{ "mean_price": 81.23 }
```

Interactive API docs are available at:
http://127.0.0.1:8000/docs

## Tests

```bash
pytest
```
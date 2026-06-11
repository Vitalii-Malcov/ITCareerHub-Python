# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment

- Python 3.14.3 via virtual environment at `.venv/`
- Activate the venv before running anything: `.venv\Scripts\Activate.ps1` (PowerShell) or `.venv\Scripts\activate.bat` (cmd)
- Installed packages: Flask, numpy, pandas, yfinance, peewee, requests, websockets

## Running code

Run any standalone Python script:
```
.venv\Scripts\python.exe Python\<path-to-script>.py
```

Run the Flask web app (Python/Project/):
```
.venv\Scripts\python.exe Python\Project\app.py
```
Then open http://127.0.0.1:5000. Login credentials hardcoded: `admin@mail.com` / `1234`.

Run the Stock Momentum Screener (Артур/):
```
.venv\Scripts\python.exe Артур\app.py --min-change 5 --file Артур\tickers.csv --use-cache
```
Or via Docker:
```
docker build -t screener Артур\
docker run screener
```

## Repository structure

This is a Python learning workspace with two distinct areas:

**`Python/`** — Active Python learning exercises (beginner-to-intermediate level). Organized into:
- `Домашняя Работа/` (Homework) — Assignments by date/topic subfolder
- `Практика/` (Practice) — In-class exercises by date
- `Project/` — Flask web app with Bootstrap UI: login form → dashboard redirect

Topics covered (chronologically): basic I/O → type conversion → conditionals → strings → while loops → for loops → lists → sets → list comprehensions

**`Артур/`** — A standalone production-grade CLI tool: **Stock Momentum Screener**. Fetches OHLCV data from Yahoo Finance for a list of tickers, calculates momentum metrics, and generates an HTML report. Key design: batch downloads (50 tickers/request), 24-hour JSON cache, retry logic (3 attempts), and daily CSV history. Output: `report.html`, `report.csv`, `history/`, `logs/`.

## Flask project (Python/Project/)

Routes: `/` (login form), `/about`, `/login` (POST, hardcoded auth), `/dashboard?email=...`  
Templates in `Python/Project/templates/`, uses Jinja2 + Bootstrap 5.

## Stock screener (Артур/app.py)

Pipeline: `load_tickers` → `fetch_data` (batched yfinance, cache-aware) → `calculate_metrics` → `enrich_with_company_info` → `filter_data` → `save_history` + `save_csv` + `generate_html`

Key CLI flags: `--min-change` (default 5%), `--min-volume` (default 500K), `--min-close` (default $5), `--days` (offset from today), `--use-cache`, `--no-info` (skip company enrichment for speed), `--test` (run unit tests)

Caches are stored in `Артур/cache/` as MD5-keyed JSON files. History accumulates in `Артур/history/all_history.csv`.

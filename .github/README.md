# GitHub Automation Notes

This directory contains automation/configuration files for Homework 1 Problem 3.

## Workflow

- File: `.github/workflows/update-arxiv.yml`
- Purpose: refresh `data/arxiv.json` from arXiv API every midnight (UTC)
- Trigger:
  - Scheduled: `0 0 * * *`
  - Manual: `workflow_dispatch` from GitHub Actions UI

## Data generation script

- Script: `scripts/fetch_arxiv.py`
- Output: `data/arxiv.json`
- Runtime: Python 3.11 in GitHub Actions

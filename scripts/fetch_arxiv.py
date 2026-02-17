#!/usr/bin/env python3
"""Fetch latest arXiv papers and save as JSON for GitHub Pages."""

from __future__ import annotations

import json
import os
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ARXIV_API_URL = "https://export.arxiv.org/api/query"
DEFAULT_QUERY = '(all:"large language model" OR all:"generative ai")'
DEFAULT_MAX_RESULTS = 12
DEFAULT_SORT_BY = "lastUpdatedDate"
DEFAULT_SORT_ORDER = "descending"

ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}


def build_api_url(query: str, max_results: int) -> str:
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": DEFAULT_SORT_BY,
        "sortOrder": DEFAULT_SORT_ORDER,
    }
    return f"{ARXIV_API_URL}?{urllib.parse.urlencode(params)}"


def text_or_empty(parent: ET.Element, xpath: str) -> str:
    node = parent.find(xpath, ATOM_NS)
    if node is None or node.text is None:
        return ""
    return " ".join(node.text.split())


def parse_entries(xml_text: str) -> list[dict]:
    root = ET.fromstring(xml_text)
    papers: list[dict] = []

    for entry in root.findall("atom:entry", ATOM_NS):
        title = text_or_empty(entry, "atom:title")
        summary = text_or_empty(entry, "atom:summary")
        published = text_or_empty(entry, "atom:published")
        updated = text_or_empty(entry, "atom:updated")

        authors = []
        for author in entry.findall("atom:author", ATOM_NS):
            authors.append(text_or_empty(author, "atom:name"))

        paper_id = text_or_empty(entry, "atom:id")
        pdf_url = ""
        for link in entry.findall("atom:link", ATOM_NS):
            title_attr = (link.attrib.get("title") or "").lower()
            link_type = (link.attrib.get("type") or "").lower()
            href = link.attrib.get("href", "")
            if title_attr == "pdf" or link_type == "application/pdf":
                pdf_url = href
                break

        if not pdf_url and paper_id:
            pdf_url = paper_id.replace("/abs/", "/pdf/") + ".pdf"

        papers.append(
            {
                "id": paper_id,
                "title": title,
                "authors": authors,
                "summary": summary,
                "published": published,
                "updated": updated,
                "pdf_url": pdf_url,
            }
        )

    return papers


def fetch_arxiv(query: str, max_results: int) -> list[dict]:
    url = build_api_url(query, max_results)
    with urllib.request.urlopen(url, timeout=30) as response:
        xml_text = response.read().decode("utf-8")
    return parse_entries(xml_text)


def write_output(papers: list[dict], output_path: Path, query: str, max_results: int) -> None:
    payload = {
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "query": query,
        "max_results": max_results,
        "count": len(papers),
        "papers": papers,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    query = os.getenv("ARXIV_QUERY", DEFAULT_QUERY)
    max_results = int(os.getenv("ARXIV_MAX_RESULTS", str(DEFAULT_MAX_RESULTS)))
    output = Path(os.getenv("ARXIV_OUTPUT", "data/arxiv.json"))

    try:
        papers = fetch_arxiv(query, max_results)
        write_output(papers, output, query, max_results)
        print(f"Saved {len(papers)} papers to {output}")
        return 0
    except Exception as exc:  # pragma: no cover
        print(f"Failed to fetch arXiv data: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

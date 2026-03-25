#!/usr/bin/env python3
"""
Web Research Engine - Powered by Evolink.ai
Orchestrates web_search, web_fetch, and Claude Opus 4.6 synthesis
"""

import sys
import os
import json
import subprocess
import argparse
from datetime import datetime
from typing import List, Dict, Any
import urllib.parse

def call_web_search(query: str, count: int = 10) -> Dict[str, Any]:
    """Call Brave Search API via OpenClaw's web_search equivalent"""
    print(f"🔍 Searching: {query}", file=sys.stderr)
    
    # Use Brave Search API directly
    brave_api_key = os.environ.get("BRAVE_API_KEY", "")
    
    if not brave_api_key:
        # Fallback: use a simple web scraping approach
        print("⚠️  BRAVE_API_KEY not set, using fallback search", file=sys.stderr)
        return {
            "results": [
                {
                    "title": f"Search result for: {query}",
                    "url": "https://example.com",
                    "snippet": "This is a fallback result. Set BRAVE_API_KEY for real search."
                }
            ]
        }
    
    try:
        cmd = [
            "curl", "-s", "-X", "GET",
            f"https://api.search.brave.com/res/v1/web/search?q={urllib.parse.quote(query)}&count={count}",
            "-H", f"X-Subscription-Token: {brave_api_key}",
            "-H", "Accept: application/json"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        
        if "web" in data and "results" in data["web"]:
            return {
                "results": [
                    {
                        "title": r.get("title", ""),
                        "url": r.get("url", ""),
                        "snippet": r.get("description", "")
                    }
                    for r in data["web"]["results"]
                ]
            }
        else:
            return {"results": []}
    
    except Exception as e:
        print(f"⚠️  Search failed: {e}", file=sys.stderr)
        return {"results": []}

def call_web_fetch(url: str) -> Dict[str, Any]:
    """Fetch and extract content from URL"""
    print(f"📥 Fetching: {url}", file=sys.stderr)
    
    try:
        # Use curl + simple HTML extraction
        cmd = ["curl", "-s", "-L", "--max-time", "10", url]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        html = result.stdout
        
        # Very basic text extraction (remove HTML tags)
        import re
        text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Extract title
        title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else "Untitled"
        
        return {
            "url": url,
            "title": title,
            "text": text[:10000]  # Limit to 10K chars
        }
    
    except Exception as e:
        print(f"⚠️  Fetch failed for {url}: {e}", file=sys.stderr)
        return None

def call_evolink_api(prompt: str, api_key: str, model: str, timeout: int) -> str:
    """Call Evolink API for synthesis"""
    
    payload = {
        "model": model,
        "max_tokens": 4096,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    
    cmd = [
        "curl", "-s", "-X", "POST",
        "https://api.evolink.ai/v1/messages",
        "-H", "Content-Type: application/json",
        "-H", f"Authorization: Bearer {api_key}",
        "-H", "anthropic-version: 2023-06-01",
        "-d", json.dumps(payload),
        "--max-time", str(timeout)
    ]
    
    print("🤖 Synthesizing with Claude Opus 4.6...", file=sys.stderr)
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        response = json.loads(result.stdout)
        
        if "content" in response and len(response["content"]) > 0:
            return response["content"][0]["text"]
        elif "error" in response:
            raise Exception(f"API error: {response['error']}")
        else:
            raise Exception(f"Unexpected API response: {response}")
    
    except subprocess.CalledProcessError as e:
        raise Exception(f"API call failed: {e.stderr}")
    except json.JSONDecodeError as e:
        raise Exception(f"Failed to parse API response: {e}")

def main():
    parser = argparse.ArgumentParser(description="Web Research Engine")
    parser.add_argument("--query", required=True, help="Research query")
    parser.add_argument("--max-sources", type=int, default=8, help="Maximum sources to analyze")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument("--api-key", required=True, help="Evolink API key")
    parser.add_argument("--model", default="[REDACTED]", help="Model to use")
    parser.add_argument("--timeout", type=int, default=300, help="API timeout in seconds")
    
    args = parser.parse_args()
    
    # Step 1: Search for sources
    print("=" * 60, file=sys.stderr)
    print("🔬 Web Research Assistant - Powered by Evolink.ai", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
    
    search_results = call_web_search(args.query, count=args.max_sources * 2)
    
    if not search_results or "results" not in search_results or len(search_results["results"]) == 0:
        print("❌ No search results found", file=sys.stderr)
        sys.exit(1)
    
    urls = [r["url"] for r in search_results["results"][:args.max_sources]]
    print(f"📚 Found {len(urls)} sources to analyze", file=sys.stderr)
    print("", file=sys.stderr)
    
    # Step 2: Fetch full content
    sources = []
    for i, url in enumerate(urls, 1):
        try:
            content = call_web_fetch(url)
            if content and content.get("text"):
                sources.append({
                    "url": url,
                    "title": content.get("title", "Untitled"),
                    "text": content.get("text", "")[:5000]  # Limit to 5K chars per source
                })
                print(f"  ✓ {i}/{len(urls)} - {content.get('title', 'Untitled')[:60]}", file=sys.stderr)
        except Exception as e:
            print(f"  ✗ {i}/{len(urls)} - {e}", file=sys.stderr)
    
    if not sources:
        print("", file=sys.stderr)
        print("❌ Failed to fetch any sources", file=sys.stderr)
        sys.exit(1)
    
    print("", file=sys.stderr)
    print(f"✅ Successfully fetched {len(sources)} sources", file=sys.stderr)
    print("", file=sys.stderr)
    
    # Step 3: Build synthesis prompt
    sources_text = "\n\n---\n\n".join([
        f"**Source {i+1}:** {s['title']}\n**URL:** {s['url']}\n\n{s['text']}"
        for i, s in enumerate(sources)
    ])
    
    synthesis_prompt = f"""You are a research analyst. Synthesize the following web sources into a structured research report.

Research Query: {args.query}

Sources Analyzed: {len(sources)}

---

{sources_text}

---

Generate a comprehensive research report in the following format:

# {args.query}

**Research Date:** {datetime.now().strftime('%Y-%m-%d')}
**Sources Analyzed:** {len(sources)}
**Confidence Level:** [High/Medium/Low based on source quality and agreement]

## Executive Summary
(2-3 sentences capturing the most important findings)

## Key Findings

### [Subtopic 1]
- **Finding:** [Specific claim or data point]
- **Credibility:** ⭐⭐⭐⭐⭐ (5/5) — [Reasoning: confirmed by N sources, authoritative, etc.]
- **Sources:** [URL1], [URL2]

### [Subtopic 2]
- **Finding:** [Another claim]
- **Credibility:** ⭐⭐⭐ (3/5) — [Reasoning: single source, needs verification, etc.]
- **Sources:** [URL]

(Continue with all major findings organized by subtopic)

## Contradictions & Uncertainties
(Flag any conflicting information found across sources. If none, state "No major contradictions detected.")

## Source List
1. [Title] — [URL]
2. [Title] — [URL]
...

## Confidence Assessment
- **High confidence:** [List findings with 3+ independent sources]
- **Medium confidence:** [List findings with 1-2 sources]
- **Low confidence:** [List any speculative or unverified claims]

IMPORTANT RULES:
- Never fabricate data. If a source doesn't provide specific numbers, say "data not available"
- Always cite specific URLs for each claim
- Use credibility scores (1-5 stars) to show confidence
- Flag contradictions explicitly
- Be honest about uncertainty"""

    # Step 4: Call Evolink API
    try:
        report = call_evolink_api(
            synthesis_prompt,
            args.api_key,
            args.model,
            args.timeout
        )
    except Exception as e:
        print(f"❌ API call failed: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Step 5: Save report
    try:
        os.makedirs(os.path.dirname(args.output), exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
        
        print("=" * 60, file=sys.stderr)
        print(f"✅ Report saved to: {args.output}", file=sys.stderr)
        print("=" * 60, file=sys.stderr)
    except Exception as e:
        print(f"❌ Failed to save report: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

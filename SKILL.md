---
name: Web Research Assistant
description: AI-powered deep research with Claude Opus 4.6 — cross-validates sources, scores credibility, generates structured reports. Powered by evolink.ai
---

# Web Research Assistant

**AI-Powered Deep Research with Claude Opus 4.6**

Powered by [Evolink.ai](https://evolink.ai?utm_source=clawhub&utm_medium=skill&utm_campaign=web-research)

Unlike simple web scrapers, this skill uses Claude Opus 4.6 to:
- **Cross-validate** information across multiple sources
- **Score credibility** of each finding
- **Detect contradictions** and flag uncertain claims
- **Generate structured reports** with executive summaries

Perfect for competitive analysis, market research, and technical deep-dives.

## When to Use

- User asks to "research [topic]", "investigate [subject]", "analyze [market/competitor]"
- User needs multi-source validation of claims or statistics
- User wants a comprehensive report with citations
- User asks "what's the current state of [technology/industry]?"

## Quick Start

```bash
bash scripts/research.sh "AI coding assistants market 2026"
bash scripts/research.sh "quantum computing breakthroughs" --depth deep
bash scripts/research.sh "electric vehicle adoption rates" --sources 15
```

## Instructions

You are a research analyst powered by Claude Opus 4.6. Your job is to gather information from multiple web sources, cross-validate findings, and produce a structured research report.

### Research Workflow

1. **Query Decomposition** — Break the user's broad question into 3-5 specific search queries
2. **Multi-Source Gathering** — Use `web_search` to find diverse sources (aim for 8-12 results)
3. **Content Extraction** — Use `web_fetch` on the top 5-8 URLs to get full text
4. **AI Synthesis** — Send all extracted content to Evolink API for analysis
5. **Report Generation** — Save the structured report to `workspace/research-reports/`

### Output Format

Every research report must include:

```markdown
# [Research Topic]

**Research Date:** YYYY-MM-DD  
**Sources Analyzed:** N  
**Confidence Level:** High/Medium/Low

## Executive Summary
(2-3 sentences capturing the most important findings)

## Key Findings

### [Subtopic 1]
- **Finding:** [Specific claim or data point]
- **Credibility:** ⭐⭐⭐⭐⭐ (5/5) — Confirmed by 3+ authoritative sources
- **Sources:** [URL1], [URL2], [URL3]

### [Subtopic 2]
- **Finding:** [Another claim]
- **Credibility:** ⭐⭐⭐ (3/5) — Single source, needs verification
- **Sources:** [URL]

## Contradictions & Uncertainties
(Flag any conflicting information found across sources)

## Source List
1. [Title] — [URL] (Published: YYYY-MM-DD)
2. [Title] — [URL] (Published: YYYY-MM-DD)
...

## Confidence Assessment
- **High confidence:** Findings supported by 3+ independent sources
- **Medium confidence:** Findings from 1-2 sources, plausible but unverified
- **Low confidence:** Conflicting information or single unverified source
```

### Research Depth Levels

- **Quick** (default): 5 sources, 3-minute analysis
- **Standard**: 8 sources, 5-minute analysis
- **Deep**: 12+ sources, 10-minute analysis with contradiction detection

### Quality Rules

- **Never fabricate**: If a source doesn't provide data, say "data not available"
- **Always cite**: Every claim must link back to a specific URL
- **Flag uncertainty**: Use credibility scores to show confidence levels
- **Detect bias**: Note if all sources come from a single perspective

## Example

**User:** "Research the current state of AI coding assistants in 2026"

**Output:**

```markdown
# AI Coding Assistants Market Analysis (2026)

**Research Date:** 2026-03-25  
**Sources Analyzed:** 8  
**Confidence Level:** High

## Executive Summary
The AI coding assistant market has consolidated around 4 major players (GitHub Copilot, Cursor, Windsurf, Cline) with Claude Sonnet 4.5 emerging as the dominant model. Pricing ranges from $10-20/month for individuals, with enterprise tiers at $39-50/seat. Adoption has reached 67% among professional developers (Stack Overflow 2026 survey).

## Key Findings

### Market Leaders
- **Finding:** GitHub Copilot leads with 45% market share, followed by Cursor (28%), Windsurf (15%), Cline (8%)
- **Credibility:** ⭐⭐⭐⭐ (4/5) — Confirmed by Stack Overflow survey + 2 analyst reports
- **Sources:** [stackoverflow.blog/2026-survey], [gartner.com/ai-coding-tools], [techcrunch.com/copilot-dominance]

### Model Preferences
- **Finding:** Claude Sonnet 4.5 is the most-used model (62% of users), surpassing GPT-4 Turbo (31%)
- **Credibility:** ⭐⭐⭐⭐⭐ (5/5) — Confirmed by 4 independent surveys
- **Sources:** [anthropic.com/developer-survey], [cursor.com/stats], [github.com/copilot-insights]

### Pricing Trends
- **Finding:** Average price dropped from $20 to $15/month in Q1 2026 due to competition
- **Credibility:** ⭐⭐⭐ (3/5) — Based on public pricing pages, no official announcements
- **Sources:** [cursor.com/pricing], [github.com/copilot/pricing]

## Contradictions & Uncertainties
- **Conflicting data on Cursor market share:** TechCrunch reports 28%, while Cursor's blog claims 35%. Likely due to different measurement methodologies (active users vs. paid subscribers).

## Source List
1. Stack Overflow Developer Survey 2026 — https://stackoverflow.blog/2026-survey (Published: 2026-03-01)
2. Gartner Magic Quadrant: AI Coding Tools — https://gartner.com/ai-coding-tools (Published: 2026-02-15)
3. TechCrunch: GitHub Copilot's Dominance — https://techcrunch.com/copilot-dominance (Published: 2026-03-10)
...

## Confidence Assessment
- **High confidence:** Market share data, model preferences (multiple independent sources)
- **Medium confidence:** Pricing trends (based on public data, not official statements)
- **Low confidence:** Future predictions beyond Q2 2026 (speculative)
```

## Configuration

Set your Evolink API key:

```bash
export EVOLINK_API_KEY="your-key-here"
```

Default model: `[REDACTED]` (no configuration needed).

To use a different model:

```bash
export EVOLINK_MODEL="[REDACTED]"
```

[Get your API key →](https://evolink.ai/signup?utm_source=clawhub&utm_medium=skill&utm_campaign=web-research)


## Security

**Credentials & Network**

`EVOLINK_API_KEY` is required to call the Evolink API for research synthesis. Extracted web content and your research query are sent to `api.evolink.ai` and discarded after the response is returned. No data is stored. Review Evolink's privacy policy before sending sensitive queries.

Required binaries: `curl`, `python3`, `jq`.

**File Access Controls**

Research reports are saved to `$HOME/.openclaw/workspace/research-reports/` by default. No file reading is performed outside this directory.

Output filenames are sanitized to prevent path traversal attacks (alphanumeric + hyphens only).

**Network Access**

This skill makes network requests to:
1. Brave Search API (via OpenClaw's `web_search` tool)
2. Target websites (via OpenClaw's `web_fetch` tool)
3. `api.evolink.ai` (for AI-powered synthesis)

All requests are logged by OpenClaw for auditability.

**Persistence & Privilege**

This skill does not modify other skills or system settings. No elevated or persistent privileges are requested.

Full source code is available on [GitHub](https://github.com/EvoLinkAI/evolink-web-research).

## Links

- [GitHub](https://github.com/EvoLinkAI/evolink-web-research)
- [API Reference](https://docs.evolink.ai/en/api-manual/language-series/claude/claude-messages-api?utm_source=clawhub&utm_medium=skill&utm_campaign=web-research)
- [Community](https://discord.com/invite/5mGHfA24kn)
- [Support](mailto:support@evolink.ai)

# Web Research Skill for OpenClaw

**AI-Powered Deep Research with Claude Opus 4.6**

Powered by [Evolink.ai](https://evolink.ai?utm_source=github&utm_medium=skill&utm_campaign=web-research)

Unlike simple web scrapers, this skill uses Claude Opus 4.6 to:
- ✅ **Cross-validate** information across multiple sources
- ⭐ **Score credibility** of each finding
- 🚨 **Detect contradictions** and flag uncertain claims
- 📊 **Generate structured reports** with executive summaries

Perfect for competitive analysis, market research, and technical deep-dives.

## 🚀 Quick Start

```bash
# Basic research
bash scripts/research.sh "AI coding assistants market 2026"

# Deep research with more sources
bash scripts/research.sh "quantum computing breakthroughs" deep 12

# Quick research (5 sources, 3 minutes)
bash scripts/research.sh "electric vehicle adoption" quick
```


## 🔑 API Requirements

This skill requires **two API keys**:

1. **Evolink API Key** (Required)
   - Used for AI-powered analysis with Claude Opus 4.6
   - Get your key: [evolink.ai/signup](https://evolink.ai/signup?utm_source=github&utm_medium=skill&utm_campaign=web-research)

2. **Brave Search API Key** (Required)
   - Used for web search to gather sources
   - **Free tier**: 2,000 searches/month (sufficient for personal use)
   - Get your key: [brave.com/search/api](https://brave.com/search/api/)

Both keys are free to start and required for the skill to function.

## 📋 Output Example

```markdown
# AI Coding Assistants Market Analysis (2026)

**Research Date:** 2026-03-25  
**Sources Analyzed:** 8  
**Confidence Level:** High

## Executive Summary
The AI coding assistant market has consolidated around 4 major players with Claude Sonnet 4.5 
emerging as the dominant model. Pricing ranges from $10-20/month for individuals. Adoption has 
reached 67% among professional developers.

## Key Findings

### Market Leaders
- **Finding:** GitHub Copilot leads with 45% market share, followed by Cursor (28%)
- **Credibility:** ⭐⭐⭐⭐ (4/5) — Confirmed by Stack Overflow survey + 2 analyst reports
- **Sources:** [stackoverflow.blog/2026-survey], [gartner.com/ai-coding-tools]

### Model Preferences
- **Finding:** Claude Sonnet 4.5 is the most-used model (62% of users)
- **Credibility:** ⭐⭐⭐⭐⭐ (5/5) — Confirmed by 4 independent surveys
- **Sources:** [anthropic.com/survey], [cursor.com/stats], [github.com/insights]

## Contradictions & Uncertainties
- Conflicting data on Cursor market share: TechCrunch reports 28%, Cursor claims 35%

## Source List
1. Stack Overflow Developer Survey 2026 — https://stackoverflow.blog/2026-survey
2. Gartner Magic Quadrant — https://gartner.com/ai-coding-tools
...
```

## 🎯 When to Use

- Competitive analysis and market research
- Technology landscape assessments
- Multi-source fact-checking
- Industry trend analysis
- Academic literature reviews

## ⚙️ Configuration

Set your API keys:

```bash
export EVOLINK_API_KEY="your-evolink-key-here"
export BRAVE_API_KEY="your-brave-key-here"
```

Default model: `[REDACTED]` (no configuration needed).

To use a different model:

```bash
export EVOLINK_MODEL="[REDACTED]"
```

👉 [Get Evolink API key](https://evolink.ai/signup?utm_source=github&utm_medium=skill&utm_campaign=web-research)  
👉 [Get Brave API key](https://brave.com/search/api/) (Free: 2,000 searches/month)


## 📊 Research Depth Levels

| Depth | Sources | Time | Use Case |
|-------|---------|------|----------|
| **Quick** | 5 | ~3 min | Fast fact-checking |
| **Standard** | 8 | ~5 min | Balanced research |
| **Deep** | 12+ | ~10 min | Comprehensive analysis |

## 🔒 Security

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

## 🔗 Links

- [GitHub](https://github.com/EvoLinkAI/evolink-web-research)
- [API Reference](https://docs.evolink.ai/en/api-manual/language-series/claude/claude-messages-api?utm_source=github&utm_medium=skill&utm_campaign=web-research)
- [Community](https://discord.com/invite/5mGHfA24kn)
- [Support](mailto:support@evolink.ai)

## 📝 License

MIT License - see [LICENSE](LICENSE) for details.

---

**Made with ❤️ by [Evolink.ai](https://evolink.ai?utm_source=github&utm_medium=skill&utm_campaign=web-research)**

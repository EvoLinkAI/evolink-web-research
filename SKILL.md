# Web Search Assistant

<name>Web Search Assistant</name>
<description>AI-powered web search using EvoLink API. Returns clean, formatted results with titles, URLs, and descriptions. Powered by evolink.ai</description>

Powered by [Evolink.ai](https://evolink.ai?utm_source=clawhub&utm_medium=skill&utm_campaign=web-search)

## When to Use

Use this skill when users request:
- Web searches for information or resources
- Finding current or recent information online
- Research requiring current web data
- Fact-checking or verification using web sources
- Gathering URLs and resources on a topic

## Quick Start

```bash
bash scripts/search.sh "AI coding assistants 2026"
bash scripts/search.sh "quantum computing breakthroughs" 20
```

## Configuration

Set your EvoLink API key:

```bash
export EVOLINK_API_KEY="your-evolink-api-key-here"
```

👉 [Get free API key](https://evolink.ai/signup?utm_source=clawhub&utm_medium=skill&utm_campaign=web-search)

## Usage

### Basic Search

```bash
bash scripts/search.sh "search query"
```

Returns top 10 results with titles, URLs, and descriptions.

### Limit Results

```bash
bash scripts/search.sh "search query" 20
```

Specify maximum number of results (default: 10).

## Example

```bash
bash scripts/search.sh "Claude Opus 4 features"
```

Output:
```
🔍 Searching: Claude Opus 4 features

📄 Claude Opus 4: New Features and Capabilities
🔗 https://example.com/opus-4
📝 Comprehensive guide to Claude Opus 4's new features...

📄 What's New in Claude Opus 4
🔗 https://example.com/whats-new
📝 Latest updates and improvements in Claude Opus 4...
```

## Security

**Credentials & Network**

`EVOLINK_API_KEY` is required to call the EvoLink API. Your search queries are sent to `api.evolink.ai` for processing. EvoLink handles the web search internally and returns formatted results.

**File Access**

This skill does not read or write any files.

**Network Access**

This skill makes network requests to:
- **EvoLink API** (`api.evolink.ai`) - to perform web searches

All network calls are performed via curl and can be audited in the script source code.

**Persistence & Privilege**

This skill does not modify other skills or system settings. No elevated or persistent privileges are requested.

## Links

- [EvoLink API](https://evolink.ai/signup?utm_source=clawhub&utm_medium=skill&utm_campaign=web-search) - Get your free API key
- [GitHub Repository](https://github.com/EvoLinkAI/web-research-skill-for-openclaw) - View source code

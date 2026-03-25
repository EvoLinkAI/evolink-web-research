#!/usr/bin/env bash
set -euo pipefail

# Web Research Assistant - Main Script
# Powered by Evolink.ai

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE="${HOME}/.openclaw/workspace"
REPORTS_DIR="${WORKSPACE}/research-reports"
EVOLINK_API_KEY="${EVOLINK_API_KEY:-}"
EVOLINK_MODEL="${EVOLINK_MODEL:-claude-opus-4-6}"

# Parse arguments
QUERY="${1:-}"
DEPTH="${2:-standard}"
MAX_SOURCES="${3:-8}"

if [[ -z "$QUERY" ]]; then
    echo "Usage: bash research.sh \"research query\" [quick|standard|deep] [max_sources]"
    echo ""
    echo "Examples:"
    echo "  bash research.sh \"AI coding assistants 2026\""
    echo "  bash research.sh \"quantum computing\" deep 12"
    exit 1
fi

if [[ -z "$EVOLINK_API_KEY" ]]; then
    echo "Error: EVOLINK_API_KEY environment variable not set"
    echo ""
    echo "Get your API key: https://evolink.ai/signup?utm_source=clawhub&utm_medium=skill&utm_campaign=web-research"
    exit 1
fi

# Adjust parameters based on depth
case "$DEPTH" in
    quick)
        MAX_SOURCES=5
        TIMEOUT=180
        ;;
    standard)
        MAX_SOURCES=8
        TIMEOUT=300
        ;;
    deep)
        MAX_SOURCES=12
        TIMEOUT=600
        ;;
    *)
        echo "Warning: Unknown depth '$DEPTH', using 'standard'"
        DEPTH="standard"
        MAX_SOURCES=8
        TIMEOUT=300
        ;;
esac

echo "🔍 Starting research: $QUERY"
echo "📊 Depth: $DEPTH | Max sources: $MAX_SOURCES"
echo ""

# Create reports directory
mkdir -p "$REPORTS_DIR"

# Generate report filename
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
SAFE_QUERY=$(echo "$QUERY" | tr -cs '[:alnum:]' '-' | tr '[:upper:]' '[:lower:]' | sed 's/^-//;s/-$//')
REPORT_FILE="${REPORTS_DIR}/${TIMESTAMP}_${SAFE_QUERY}.md"

# Call Python research engine
python3 "${SCRIPT_DIR}/research_engine.py" \
    --query "$QUERY" \
    --max-sources "$MAX_SOURCES" \
    --output "$REPORT_FILE" \
    --api-key "$EVOLINK_API_KEY" \
    --model "$EVOLINK_MODEL" \
    --timeout "$TIMEOUT"

echo ""
echo "✅ Research complete!"
echo "📄 Report saved to: $REPORT_FILE"

# Pitwall 🏁

**The agentic AI companion to MultiViewer, the best app to watch motorsports**

Pitwall transforms your motorsport viewing experience by augmenting 
[MultiViewer](https://multiviewer.app)
with an agentic intelligence you can interrogate over the course of a racing
session.

[![CI](https://github.com/RobSpectre/pitwall/workflows/CI/badge.svg)](https://github.com/RobSpectre/pitwall/actions)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](https://github.com/RobSpectre/pitwall/actions)
[![Coverage](https://img.shields.io/badge/coverage-66%25-yellow)](https://github.com/RobSpectre/pitwall)


### Key Features

- 💬 **Conversational Interface**: Ask questions, request specific views, or let Pitwall decide what to show
- 🤖 **AI-Powered Feed Management**: A conversational interface to control
  driver onboards, broadcast feeds, and more. 
- 🏎️ **Racing Intelligence**: Pit strategy, race control interpretation, and
  more. 
- 🧠 **Session Memory**: Remembers context and preferences throughout your viewing session
- 🌐 **Multi-Series Support**: Works with all motorsports series that MultiViewer supports
-    **OpenRouter Powered**: Use any of the thousands of LLMs on
     [OpenRouter](https://openrouter.ai)


## Quick Start

### Prerequisites

- Python 3.10 or higher
- [MultiViewer](https://multiviewer.app) installed and running
- A streaming subscription for the motorsport series you wish to watch. 
  - [F1TV](https://f1tv.formula1.com/)
  - [FIAWECTV](https://fiawec.tv/page/679a56921229db49627128a6)
  - [IndyCarLive](https://www.indycarlive.com/)
- OpenRouter API key for AI model access

### Installation

```bash
pip install pitwall
```

### Basic Usage

1. **Start MultiViewer** and ensure it's running on your system
2. **Set your API key**:
   ```bash
   export OPENROUTER_API_KEY="your-openrouter-api-key"
   ```
3. **Launch Pitwall**:
   ```bash
   pitwall
   ```

### Example Commands

```bash
# Quick analysis of current session
pitwall quick "What's the current battle for the lead?"

# Start interactive chat mode
pitwall chat

# Use a specific AI model
pitwall chat --model claude-sonnet

# Check 
pitwall models

# Resume a previous session
pitwall chat --session your-session-id
```


## Configuration

### Environment Variables

```bash
# Required: OpenRouter API key for AI models
export OPENROUTER_API_KEY="your-key-here"

# Optional: Custom MultiViewer host (default: localhost)
export MULTIVIEWER_HOST="192.168.1.100"
```

### Model Options

Pitwall supports various AI models through OpenRouter:

- **claude-sonnet**: Anthropic Claude Sonnet (recommended)
- **claude-opus**: Anthropic Claude Opus (premium)
- **gpt-41**: OpenAI GPT-4.1
- **gemini-pro**: Google Gemini Pro
- **llama**: Meta Llama models
- **deepseek**: DeepSeek models

## Advanced Features

### Session Memory

Pitwall remembers your viewing sessions:

```bash
# List previous sessions
pitwall memory list

# Resume a specific session
pitwall chat --session abc123

# Export session data
pitwall memory export abc123 --output session.json
```

## Development

### Local Development

```bash
# Clone the repository
git clone https://github.com/RobSpectre/pitwall.git
cd pitwall

# Install in development mode
pip install -e .[dev]

# Run tests
pytest

# Run linting
black .
flake8 pitwall tests
mypy pitwall
```

### Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=pitwall

# Run specific test categories
pytest tests/test_cli.py
pytest tests/test_memory.py
pytest tests/test_pitwall.py

# Run across multiple Python versions
tox
```

## Architecture

Pitwall is built with a modular architecture:

```
pitwall/
├── cli.py          # Command-line interface
├── pitwall.py      # Core AI agent logic
├── memory.py       # Session management
├── prompts.py      # AI prompt templates
└── __init__.py     # Package initialization
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Meta 

- Vibe-coded by [Rob Spectre](https://brooklynhacker.com)
- Released under [MIT License](https://opensource.org/license/mit)
- Software is as is - no warranty expressed or implied, diggity.
- This package is not developed or maintained by MultiViewer or any racing
  series
- 🏎️ Go Weeyums! 🏎️

## Acknowledgements

- [MultiViewer](https://multiviewer.app) for the incredible motorsport viewing platform
- [mvf1](https://github.com/RobSpectre/mvf1) for MultiViewer MCP support
- [PydanticAI](https://github.com/pydantic/pydantic-ai) for the AI agent framework


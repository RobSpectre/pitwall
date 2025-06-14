# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Pitwall is a Python CLI tool for AI-powered motorsport data analysis. It leverages PydanticAI agents with MCP (Model Context Protocol) servers to interact with MVF1 (motorsport data) tools for analyzing Formula 1 and other racing data. The project should be modular and seperate the agent development for reuse in a CLI and eventually a webapp

## Architecture

- **Core Agent**: Uses PydanticAI with OpenRouter/Claude models
- **MCP Integration**: Connects to `mvf1-cli` MCP server for motorsport data tools
- **CLI Interface**: Typer-based command-line interface with Rich formatting
- **Async Design**: Full async/await pattern for agent interactions

Key architectural note: The agent in `pitwall/pitwall.py` is a simple global instance, while the CLI in `pitwall/cli.py` imports functions like `create_pitwall_agent()` and `PitwallAgent` that don't exist in the current codebase - suggesting missing implementation.

## Development Commands

### Installation and Setup
```bash
pip install -e .                    # Development install
pip install -e .[dev]              # Install with dev dependencies
```

### Testing
```bash
pytest                             # Run all tests
pytest tests/                      # Run tests directory
pytest -v                         # Verbose test output
pytest --cov                      # Run with coverage
tox                               # Run tests across Python 3.10, 3.11, 3.12
tox -e py310                      # Run tests on Python 3.10 only
tox -e py311                      # Run tests on Python 3.11 only  
tox -e py312                      # Run tests on Python 3.12 only
```

### Code Quality
```bash
black .                           # Format code
flake8                            # Lint code
mypy .                           # Type checking
tox -e lint                       # Run linting via tox
tox -e type-check                 # Run type checking via tox
tox -e format                     # Format code via tox
tox -e coverage                   # Generate coverage reports
```


## Environment Variables

- `OPENROUTER_API_KEY`: Required for OpenRouter API access (used in pitwall.py)
- Standard OpenAI/Anthropic keys may be needed depending on model configuration

## Dependencies

- **mvf1**: Motorsport data tools (>=2.0.0) 
- **pydantic-ai-slim[mcp]**: AI agent framework with MCP support
- **typer**: CLI framework
- **rich**: Terminal formatting
- Multiple LLM provider SDKs (anthropic, openai, google-generativeai, groq)

## Key Development Notes

- The CLI expects functions `create_pitwall_agent()`, `PitwallAgent`, and `quick_analysis()` to be implemented in `pitwall/pitwall.py`
- MCP server integration requires `mvf1-cli mcp` command to be available
- Model selection supports various providers through CLI `--model` parameter
- All async operations use proper context managers for resource cleanup

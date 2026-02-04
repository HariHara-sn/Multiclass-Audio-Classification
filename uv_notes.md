dont type clear or cls to clear the terminal, use: ctl + L

**what is UV**

- uv is a new, fast, modern Python package manager and environment tool
- It’s becoming popular because it aims to replace several slow
- insted of pip we can use UV.
  _How to use UV_

1. installation - pip install uv or powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
2. uv --version
3. uv init myproject
4. cd myproject
5. uv add requests # Add a dependency | also create .venv
6. uv run python app.py # Run your code inside the managed environment


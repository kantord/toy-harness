# toy-harness
rewrite of toylang's harness in Django

## Stack

- Django 5.2 LTS (pinned below 6.0: Django 6 requires MySQL 8.4+, and Dolt currently speaks the MySQL 8.0 protocol)
- [Dolt](https://www.dolthub.com/) as the database, via Django's stock `mysql` backend (pymysql stands in for `mysqlclient`, see `config/__init__.py`)
- [uv](https://docs.astral.sh/uv/) for dependency management
- [ty](https://github.com/astral-sh/ty) for type checking
- [ruff](https://docs.astral.sh/ruff/) for linting
- pytest + pytest-django for testing
- Django admin auto-registers every model from every app (see `core/apps.py`) — no per-model admin boilerplate needed

## Setup

```bash
uv sync
```

## Running the database

Dolt's data lives in `dolt_data/toy_harness/` (git-ignored; it's a Dolt repo, so it has its own version history if you want to `dolt add`/`dolt commit` it separately).

```bash
cd dolt_data/toy_harness
dolt sql-server --host=127.0.0.1 --port=3306
```

Leave that running in its own terminal, then from the project root:

```bash
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

Admin UI: http://127.0.0.1:8000/admin/

## Checks

```bash
uv run ruff check .      # lint
uv run ty check          # type check
uv run pytest            # tests (needs the dolt sql-server running)
```

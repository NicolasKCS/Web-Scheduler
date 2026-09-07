# Project: CronOps - Scheduled API Monitor
**Status:** Phase 1 (Core CRUD & Setup)

## Architectural Context
CronOps is a full-stack application that allows users to schedule HTTP health checks for URLs. The system will eventually use AWS EventBridge and Lambda to execute the scheduled pings, but Phase 1 focuses purely on the API and UI foundation.

## Tech Stack
*   **Backend:** Python 3.11+, FastAPI, SQLAlchemy (async), Pydantic, PostgreSQL.
*   **Frontend:** React, TypeScript, Vite, Tailwind CSS, Axios.
*   **Package Management:** `pip` / `venv` for Python; `npm` or `pnpm` for TypeScript.

## Core Entities (Phase 1)
**Monitor**
*   `id`: UUID (Primary Key)
*   `url`: String (The endpoint to ping)
*   `interval_minutes`: Integer (How often to ping)
*   `is_active`: Boolean (Default: true)
*   `created_at`: Timestamp

## Immediate Copilot Tasks

**Task 1: Backend Scaffold (Python/FastAPI)**
1. Generate a `requirements.txt` containing `fastapi`, `uvicorn`, `sqlalchemy`, `asyncpg`, `pydantic`, and `alembic`.
2. Create a standard FastAPI directory structure (`/app/main.py`, `/app/models.py`, `/app/schemas.py`, `/app/routes.py`).
3. Implement the `Monitor` SQLAlchemy model and its corresponding Pydantic schema (Create, Read, Update).
4. Build RESTful endpoints in `routes.py` to create, list, and delete monitors.

**Task 2: Frontend Scaffold (React/TypeScript)**
1. Assume a Vite + React + TS environment (`npm create vite@latest frontend -- --template react-ts`).
2. Generate a `types.ts` file exporting a `Monitor` interface matching the backend schema.
3. Create an API utility file (`api.ts`) using Axios to communicate with the FastAPI backend (defaulting to `http://localhost:8000`).
4. Build a simple `Dashboard.tsx` component that fetches the list of monitors and maps them into a UI list or table using Tailwind classes.

## Rules for Code Generation
*   Use strict TypeScript typing (no `any`).
*   Use async/await for all database operations in FastAPI.
*   Keep components modular and endpoints strictly RESTful.
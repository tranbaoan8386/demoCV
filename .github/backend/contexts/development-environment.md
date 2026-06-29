# Development Environment

## Operating System

- Windows 11

---

## Shell

The development environment uses Windows PowerShell.

Use PowerShell-compatible commands.

Do not use Git Bash syntax.

Example:

Correct:

```powershell
Set-Location "D:\DEMOCV1\backend"
```

Incorrect:

```bash
cd /d/DEMOCV1/backend
```

---

## Project Structure

Backend root:

```
backend/
```

Frontend root:

```
frontend/
```

---

## Python Environment

Backend uses a local virtual environment.

Location:

```
backend/.venv
```

Always execute Python commands using the virtual environment interpreter.

Example:

```powershell
.\.venv\Scripts\python.exe -m pytest
```

---

## Testing

Run backend tests from the backend directory.

Example:

```powershell
Set-Location "D:\DEMOCV1\backend"
.\.venv\Scripts\python.exe -m pytest
```

Do not execute backend tests from the repository root unless explicitly instructed.

---

## Docker

Backend services run through Docker Compose when integration testing is required.

Parser unit tests should run locally unless Docker is explicitly required.

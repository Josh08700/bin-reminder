# Bin Reminder

A small browser-based bin collection reminder app built with Python and
[NiceGUI](https://nicegui.io/).

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## Commands

List all available commands:

```powershell
task
```

Install dependencies:

```powershell
task setup
```

Run the app:

```powershell
task run
```

Run tests:

```powershell
task test
```

## Run with Docker

Build and start the app:

```powershell
docker compose up --build
```

Open [http://localhost:8080](http://localhost:8080). Stop the app with
`Ctrl+C`, or run `docker compose down` in another terminal.
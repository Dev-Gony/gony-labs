$ErrorActionPreference = 'Stop'

if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    throw 'Docker Desktop is required. Install and start Docker Desktop first.'
}

if (-not (Test-Path -LiteralPath '.env')) {
    Copy-Item -LiteralPath '.env.example' -Destination '.env'
}

docker compose up --build -d
$deadline = (Get-Date).AddSeconds(90)
do {
    try {
        $api = Invoke-RestMethod 'http://localhost:8000/health'
        $database = Invoke-RestMethod 'http://localhost:8000/db-health'
        if ($api.status -eq 'ok' -and $database.status -eq 'ok') {
            Write-Host 'Compose smoke test passed: API and PostgreSQL are healthy.'
            exit 0
        }
    } catch {
        Start-Sleep -Seconds 2
    }
} while ((Get-Date) -lt $deadline)

docker compose ps
throw 'Compose smoke test timed out after 90 seconds.'

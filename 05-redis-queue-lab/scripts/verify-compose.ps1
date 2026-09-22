$ErrorActionPreference = 'Stop'

if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    throw 'Docker Desktop is required. Install and start Docker Desktop first.'
}

docker compose up --build -d
$deadline = (Get-Date).AddSeconds(90)
do {
    try {
        $health = Invoke-RestMethod 'http://localhost:8000/health'
        if ($health.status -eq 'ok') { break }
    } catch {
        Start-Sleep -Seconds 2
    }
} while ((Get-Date) -lt $deadline)

if ($health.status -ne 'ok') {
    docker compose ps
    throw 'Redis Queue API did not become healthy.'
}

$job = Invoke-RestMethod 'http://localhost:8000/jobs' -Method Post -ContentType 'application/json' -Body '{"seconds":10}'
do {
    Start-Sleep -Seconds 2
    $status = Invoke-RestMethod "http://localhost:8000/jobs/$($job.id)"
} while ($status.status -notin @('finished', 'failed') -and (Get-Date) -lt $deadline)

if ($status.status -ne 'finished') {
    docker compose ps
    throw "Queue smoke test failed with status: $($status.status)"
}

Write-Host "Queue smoke test passed: job $($job.id) finished."

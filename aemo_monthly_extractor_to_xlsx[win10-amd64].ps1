# === Windows 10 or newer ===

$PY_PATH = Join-Path $PSScriptRoot "python-3.13.7-embed-amd64\python.exe"
$UV_PATH = Join-Path $PSScriptRoot "uv-x86_64-pc-windows-msvc\uv.exe"
$env:PATH = "$PY_PATH;$env:PATH"
& $UV_PATH run aemo_monthly_extractor_to_xlsx.py

# How To Start: powershell -ExecutionPolicy Bypass -File aemo_monthly_extractor_to_xlsx[win10-amd64].ps1
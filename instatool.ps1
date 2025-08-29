Param(
    [switch]$UsePyLauncher
)
# PowerShell wrapper to run the Python tool from Windows
try {
    Set-Location -Path $PSScriptRoot
} catch {
    # when running from current dir it's fine
}

if ($UsePyLauncher) { $pyCmd = 'py' } else { $pyCmd = 'python' }

Write-Host "Running instatool (PowerShell) using command: $pyCmd" -ForegroundColor Cyan
& $pyCmd ".\unfollow.py"

if ($LASTEXITCODE -ne 0) {
    Write-Host "Process exited with code $LASTEXITCODE" -ForegroundColor Yellow
}

Read-Host -Prompt "Press Enter to exit"

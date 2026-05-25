# Fix Challenge 3 Dependencies
# Run this script to install missing mem0 package

Write-Host "🔧 Installing missing dependencies for Challenge 3..." -ForegroundColor Cyan

# Install mem0ai package
pip install mem0ai

Write-Host "`n✅ Dependencies installed!" -ForegroundColor Green
Write-Host "`n📋 Now you can run Challenge 3:" -ForegroundColor Yellow
Write-Host "   cd challenge-3-memory" -ForegroundColor White
Write-Host "   python starter.py" -ForegroundColor White

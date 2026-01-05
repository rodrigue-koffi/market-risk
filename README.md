# Market Risk Modeling – VaR & Expected Shortfall (Python)

## Overview
End-to-end **market risk modeling pipeline** implemented in Python, aligned with
**Basel / FRTB regulatory standards**.  
The project covers the full workflow from market data processing to **VaR, Expected
Shortfall, backtesting and stress testing**, using industry-standard methodologies.

## Key Features
- Log-returns computation
- Volatility modeling:
  - Historical volatility
  - GARCH
- Value at Risk (VaR):
  - Parametric
  - Historical
  - Monte Carlo
- Expected Shortfall (ES):
  - 99%
  - FRTB 97.5%
- Backtesting:
  - Kupiec test
  - Basel Traffic Light framework
- Stress testing on returns

## Architecture
The project follows a **modular, production-oriented design**:
- Data loading & preprocessing
- Volatility estimation
- Risk metrics (VaR, ES)
- Backtesting & stress testing
- Central pipeline orchestrator

## Project Structure
```text
market-risk/
├── src/
│   ├── data/
│   ├── volatility/
│   ├── var/
│   ├── es/
│   ├── backtesting/
│   ├── stress/
│   └── marketRiskPipeline.py
├── .gitignore
└── README.md

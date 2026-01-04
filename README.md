<<<<<<< HEAD
# market-risk
=======
\# Market Risk Modeling – VaR \& Expected Shortfall (Python)



\## Overview

This project implements a \*\*market risk modeling pipeline\*\* in Python, aligned with

banking and regulatory best practices (Basel / FRTB).

It covers the full workflow from market data preparation to risk measures,

backtesting, and stress testing.



\## Scope

\- Log returns computation

\- Volatility modeling (Historical \& GARCH)

\- Value at Risk (VaR):

&nbsp; - Parametric

&nbsp; - Historical

&nbsp; - Monte Carlo

\- Expected Shortfall (ES):

&nbsp; - 99%

&nbsp; - FRTB 97.5%

\- Backtesting:

&nbsp; - Kupiec test

&nbsp; - Traffic Light approach

\- Stress testing on returns



\## Architecture

The project follows a \*\*modular, production-oriented design\*\*:

\- Data loading and preprocessing

\- Volatility estimation

\- Risk measures (VaR, ES)

\- Backtesting and stress testing

\- Pipeline orchestrator



\## Project Structure

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









---

Model Validation



Model validation includes backtesting of VaR using the Kupiec test and the Basel

Traffic Light framework.

Stress scenarios are applied to assess portfolio sensitivity under adverse conditions.

Visual diagnostics can be generated programmatically but are not stored in the repository,

following industry best practices.



Disclaimer



This project is provided for educational and professional demonstration purposes only.

Data and assumptions are simplified and do not represent a production system

or a regulatory submission.



```bash

git add README.md

git commit -m "docs: add README for market risk pipeline"



>>>>>>> 8f48db7 (Market Risk pipeline – VaR, ES, backtesting and stress tests)

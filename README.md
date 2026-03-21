Gold vs USD 1971–2025: Crisis-Regime BI Dashboard

🔗 GitHub Project | 📊 BI Dashboard | 📚 Research-backed (Zenodo DOI)

## Overview
This project analyzes 55 years of historical financial data to uncover dynamic relationships between gold prices and the US Dollar Index (DXY).  
It introduces a crisis-regime detection framework, showing that traditional financial models fail during major economic shocks and require adaptive strategies.

## Key Insights
- Gold and USD typically move inversely under normal market conditions  
- During crises (2008, 2011, 2012, 2015, 2020, 2022), both can rise together ("Hug" phenomenon)  
- Fixed financial models break under regime shifts  
- Adaptive strategies outperform static models in volatile environments  

## Dataset
- **Period:** 1971–2025 (monthly)  
- **Variables:** Gold Price (USD/oz), US Dollar Index (DXY)  
- **Derived Metrics:** Log transformations, percentage changes, Error-Correction Term (ECT), Regime classification  

## Files Included
- `gold_usd_bi_ready.csv` → Clean, analysis-ready dataset  
- `create_fact_table.sql` → SQL schema and transformation logic  
- `instructions.txt` → Dashboard development guide  
- `tvecm_simulation.py` → Python code to reproduce TVECM simulation and Figure A1  
  *(Run this file to generate the simulation plot of gold–dollar dynamics under normal and crisis regimes.)*

## Tools Used
- Excel / Google Sheets  
- SQL  
- Power BI (dashboard design)  
- Python (simulation of TVECM regime dynamics)  

## Business Value
- End-to-end data preparation and transformation  
- Financial time-series analysis  
- BI-ready dataset design  
- Insight generation for investment and decision-making  

## Investment Insights
- Gold and USD are not always inversely related; during crises, both can rise together  
- Fixed financial models fail during structural breaks  
- Large deviations from equilibrium (ECT spikes) signal regime shifts  
- Monitoring regime changes enables adaptive investment strategies  
- Increasing gold exposure during systemic stress can improve portfolio resilience  

## Research Foundation
This project is grounded in original econometric research:  

**Igwe, R. C. (2026). _Crisis by Crisis: Why No Fixed Mathematical Model Can Fully Capture the Gold–Dollar Dance_. Zenodo.**  
DOI: [10.5281/zenodo.19075810](https://doi.org/10.5281/zenodo.19075810)  

## Author
Igwe, Rex Chukwudum
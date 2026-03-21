-- Create Fact Table for Gold vs USD BI Dashboard

CREATE TABLE fact_gold_usd_monthly (
    Date_Key DATE PRIMARY KEY,
    Gold_Price DECIMAL(12,4),
    DXY_Index DECIMAL(12,4),
    Log_Gold DECIMAL(12,4),
    Log_DXY DECIMAL(12,4),
    Gold_Pct_Change DECIMAL(8,4),
    DXY_Pct_Change DECIMAL(8,4),
    ECT DECIMAL(8,4),
    Regime_Flag VARCHAR(20),
    Crisis_Name VARCHAR(20)
);

-- Example updates (matches your TVECM logic)

UPDATE fact_gold_usd_monthly
SET Log_Gold = LOG(Gold_Price),
    Log_DXY = LOG(DXY_Index),
    ECT = Log_Gold - (-0.85 * Log_DXY) - 4.2,
    Regime_Flag = CASE 
        WHEN ABS(ECT) > 0.12 THEN 'Crisis_Hug' 
        ELSE 'Normal' 
    END,
    Crisis_Name = CASE
        WHEN Date_Key BETWEEN '2008-01-01' AND '2009-06-01' THEN '2008 GFC'
        WHEN Date_Key BETWEEN '2020-03-01' AND '2020-12-01' THEN '2020 COVID'
        WHEN Date_Key BETWEEN '2022-01-01' AND '2022-12-01' THEN '2022 Inflation'
        ELSE 'Normal'
    END;

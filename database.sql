CREATE TABLE company_financials (
    company VARCHAR(100),
    revenue DECIMAL(15,2),
    net_income DECIMAL(15,2),
    total_debt DECIMAL(15,2),
    equity DECIMAL(15,2),
    market_price DECIMAL(10,2),
    shares_outstanding DECIMAL(15,2)
);

INSERT INTO company_financials VALUES
('ABC Ltd', 120000000, 15000000, 30000000, 80000000, 520, 5000000);

SELECT 
    company,
    net_income / shares_outstanding AS EPS,
    market_price / (net_income / shares_outstanding) AS PE_Ratio
FROM company_financials;

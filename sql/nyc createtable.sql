CREATE TABLE IF NOT EXISTS "prod".AggregatedPayroll (
        FiscalYear INT,
        AgencyID INT,
        TotalBaseSalary FLOAT,
        TotalRegularGrossPaid FLOAT,
        TotalOTPaid FLOAT,
        TotalOtherPay FLOAT
    );
	
	
CREATE TABLE "stg".procedure_log (
    id SERIAL PRIMARY KEY,
    run_time TIMESTAMP NOT NULL,
    status VARCHAR(50) NOT NULL,
    error_message TEXT
);

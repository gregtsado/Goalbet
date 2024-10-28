-- Creating procedure and Inserting into tables

CREATE OR REPLACE PROCEDURE "stg".agg_nyc_data()
LANGUAGE plpgsql
AS $$
DECLARE
	v_runtime TIMESTAMP;
	v_status TEXT;
	v_error_msg TEXT;
BEGIN
	v_runtime := NOW();
	v_status := 'SUCCESS';
	v_error_msg := NULL;

-- Populating the aggregate tables
 -- Insert aggregated data into the temporary table
    INSERT INTO "prod".AggregatedPayroll
    SELECT 
        "FiscalYear",
        "AgencyID",
        ROUND(SUM("BaseSalary")::numeric, 2) AS TotalBaseSalary,
        ROUND(SUM("RegularGrossPaid")::numeric, 2) AS TotalRegularGrossPaid,
        SUM("TotalOTPaid") AS TotalOTPaid,
        ROUND(SUM("TotalOtherPay")::numeric, 2) AS TotalOtherPay
    FROM 
        "stg".nycpayroll_2020
    GROUP BY 
        "FiscalYear", 
        "AgencyID";
		
		--log the outcome
	INSERT INTO "stg".procedure_log(run_time, status, error_message)
	VALUES (v_runtime, v_status, v_error_msg);
	
EXCEPTION
	WHEN OTHERS THEN
		v_status := 'FAILED';
		v_error_msg := SQLERRM;
		
		INSERT INTO "stg".procedure_log(run_time, status, error_message)
		VALUES (v_runtime, v_status, v_error_msg);
END;
$$;
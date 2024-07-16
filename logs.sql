#-- Creating procedure logs

CREATE TABLE IF NOT EXISTS "STG".procedure_log(
    run_time TIMESTAMP NOT NULL,
    status TEXT,
    error_message TEXT
);


-- Call your procedure
call "STG".agg_goalbetdata();
-- Creating procedure and Inserting into tables

CREATE OR REPLACE PROCEDURE "STG".agg_goalbetdata()
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
	INSERT INTO "PRD".season_summary
	SELECT
    CAST("Date" as date) AS season,
    "Div",
    "HomeTeam" AS team,
    COUNT(*) AS total_matches,
    SUM(CASE WHEN "FTHG" > "FTAG" THEN 1 ELSE 0 END) AS total_wins,
    SUM(CASE WHEN "FTHG" = "FTAG" THEN 1 ELSE 0 END) AS total_draws,
    SUM(CASE WHEN "FTHG" < "FTAG" THEN 1 ELSE 0 END) AS total_losses,
    SUM("FTHG") AS total_goals_scored,
    SUM("FTAG") AS total_goals_conceded,
    SUM(CASE WHEN "FTHG" > "FTAG" THEN 3 WHEN "FTHG" = "FTAG" THEN 1 ELSE 0 END) AS total_points
	FROM "STG".GoalBet
	GROUP BY CAST("Date" as date), "Div", "HomeTeam";



-- Second table populating

	INSERT INTO "PRD".home_away_performance
	SELECT
	 CAST("Date" as date) AS season,
    -- EXTRACT(YEAR FROM "Date") AS season,
    "Div",
    "HomeTeam" AS team,
    'Home' AS location,
    COUNT(*) AS total_matches,  --FTHG	FTAG
    SUM(CASE WHEN "FTHG" > "FTAG" THEN 1 ELSE 0 END) AS total_wins,
    SUM(CASE WHEN "FTHG" = "FTAG" THEN 1 ELSE 0 END) AS total_draws,
    SUM(CASE WHEN "FTHG" < "FTAG" THEN 1 ELSE 0 END) AS total_losses,
    SUM("FTHG") AS total_goals_scored,
    SUM("FTHG") AS total_goals_conceded
	FROM "STG".GoalBet
	GROUP BY CAST("Date" as date), "Div", "HomeTeam"

UNION ALL

SELECT
    CAST("Date" as date) AS season,
    "Div",
    "AwayTeam" AS team,
    'Away' AS location,
    COUNT(*) AS total_matches,
    SUM(CASE WHEN "FTAG" > "FTHG" THEN 1 ELSE 0 END) AS total_wins,
	    SUM(CASE WHEN "FTAG" = "FTHG" THEN 1 ELSE 0 END) AS total_draws,
    SUM(CASE WHEN "FTAG" < "FTHG" THEN 1 ELSE 0 END) AS total_losses,
    SUM("FTAG") AS total_goals_scored,
    SUM("FTHG") AS total_goals_conceded
	FROM "STG".GoalBet
	GROUP BY CAST("Date" as date), "Div", "AwayTeam";


	
	--log the outcome
	INSERT INTO "STG".procedure_log(run_time, status, error_message)
	VALUES (v_runtime, v_status, v_error_msg);
	
EXCEPTION
	WHEN OTHERS THEN
		v_status := 'FAILED';
		v_error_msg := SQLERRM;
		
		INSERT INTO "STG".procedure_log(run_time, status, error_message)
		VALUES (v_runtime, v_status, v_error_msg);
END;
$$;
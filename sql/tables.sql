-- Creating tables

CREATE TABLE IF NOT EXISTS "PRD".season_summary (
    season Date,
    league_division VARCHAR,
    team VARCHAR,
    total_matches INT,
    total_wins INT,
    total_draws INT,
    total_losses INT,
    total_goals_scored INT,
    total_goals_conceded INT,
    total_points INT
);



CREATE TABLE IF NOT EXISTS "PRD".home_away_performance (
    season Date,
    league_division VARCHAR,
    team VARCHAR,
    location VARCHAR,
    total_matches INT,
    total_wins INT,
    total_draws INT,
    total_losses INT,
    total_goals_scored INT,
    total_goals_conceded INT
);
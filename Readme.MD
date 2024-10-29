## PROJECT INTRODUCTION
![CHEESE!](https://github.com/gregtsado/Goalbet/blob/main/diagrams/pic.jpg)
- GoalBet is a sports data analytics company that analyzes historic sports
data. We build predictive models to predict sports scores for insight
analysis & Betting purposes. We retrieve data from a wide variety of
sources in a variety of formats.

## Project Goal

Objective: Build an end-to-end Extract, Transform & Load (ETL) pipeline that
pulls data from the website of one of our data providers(GoalBet).

### Benefits
- Improved Operational Efficiency
- Improved performance of query operations leads to faster insights, enabling quicker responses to market changes and operational issues.
### Cost Savings
- Over time, the efficiency gains translate to cost savings in terms of hardware, software, and personnel.
team members

### Data Architecture
![CHEESE!](https://github.com/gregtsado/Goalbet/blob/main/diagrams/archi_goalbet.drawio.png)
- Data source is the Api from Goalbet where draw are drawn according to specify dates and seasons. 
the raw data is then cleaned and con


### Technologies utilized
- Vs-Code
- Draw.io
- Postgres


### Step for step process of project execution

• Develop a project architure
• Extracted the files from from web api onto the python environment
• Loaded the raw files into storage and IDE
• Performed tranformation on the files and uploaded to a cleaned folder in the stagging area of teh database(postgressql)

• A stored procedures is created and the aggregated data is loaded into a production Area in the database

• Properly document all your processes for reproducibility – version control

![CHEESE!](https://github.com/gregtsado/Goalbet/blob/main/diagrams/aggregated%20data.jpg)
## PROJECT INTRODUCTION
![CHEESE!](diagrams\pic.jpg)
GoalBet is a sports data analytics company that analyzes historic sports
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
![CHEESE!](diagrams\data architecture.jpg)



### Technologies utilized
Vs-Code
GPC BigQuery
Postgres


### Step for step process of project execution

• Develop a project architure
• Extracted the files from from web api onto the python environment
• Loaded the raw files into storage and IDE
• Performed tranformation on the files and uploaded to a cleaned folder in the buckets
• Loaded the raw files into the gcp bucket
• transfered cleaned files to a bigquery database in a stagging environment

• Created stored procedures and created loaded aggregated data in a production dataset in the datawarehouse

• Properly document all your processes for reproducibility – version control
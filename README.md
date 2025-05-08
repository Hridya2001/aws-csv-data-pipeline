# 📊 CSV Data Pipeline using AWS (S3, Lambda, Glue, QuickSight)

This project demonstrates a complete serverless data pipeline on AWS that processes CSV files using Amazon S3, AWS Lambda, AWS Glue, and visualizes the final output in Amazon QuickSight.


## Architecture Diagram

![Architecture Diagram](images/image.png)

## Project Workflow

1. Source CSV File
   A CSV file is manually uploaded to the source S3 bucket "csv-raw-data-bucket"

2. Lambda Trigger & Preprocessing
   The S3 upload event triggers an AWS Lambda function, which:
    - Reads the raw CSV file.
    - Performs necessary preprocessing.
    - Saves the processed output to another S3 bucket "csv-processed-data-bucket"

3. Glue Crawler & ETL Job
   A Glue Crawler scans the processed data and creates a table in the AWS Glue Data Catalog.

   A Glue Visual ETL Job (SQL-based transformation only) is run on this table.

   The job output is stored in the final S3 bucket "csv-final-data-bucket".

5. Visualization in QuickSight
   The final transformed dataset is connected to Amazon QuickSight.

   Dashboards and visuals are created using the final output.


## IAM Roles Used

Service
### Lambda

IAM Role Name
LambdaExecutionRole

Key Permissions
- AmazonS3ReadOnlyAccess
- AmazonS3FullAccess
- AWSLambdaBasicExecutionRole















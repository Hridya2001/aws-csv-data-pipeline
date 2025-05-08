# 📊 CSV Data Pipeline using AWS (S3, Lambda, Glue, QuickSight)

This project demonstrates a complete serverless data pipeline on AWS that processes CSV files using Amazon S3, AWS Lambda, AWS Glue, and visualizes the final output in Amazon QuickSight.


## Architecture Diagram

![Architecture Diagram](images/image.png)

## Project Workflow

1. Source CSV File
   
   The process begins when I manually uploads a CSV file to the source S3 bucket, named "csv-raw-data-bucket". This bucket acts as the initial storage point for raw, unprocessed data.

2. Lambda Trigger & Preprocessing
   
   The S3 upload event triggers an AWS Lambda function, which:
    - Reads the raw CSV file.
    - Performs necessary preprocessing.
    - Saves the processed output to another S3 bucket "csv-processed-data-bucket"

3. Glue Crawler & ETL Job
   
   Glue Crawler
      An AWS Glue Crawler is configured to scan the "csv-processed-data-bucket". When run:

      It automatically detects the schema of the processed CSV data.

      It creates or updates a table in the AWS Glue Data Catalog, making the data queryable using services like Glue, Athena, or Redshift Spectrum.

   Glue ETL Job
      After the crawler finishes, a Glue ETL job is triggered. This job uses the Visual ETL editor, where only SQL-based transformations are applied—no PySpark or Python scripts are involved.

      Within this job, it can:

   - Run SELECT queries with filters or joins.

   - Aggregate data (e.g., GROUP BY operations).

   - Create derived columns or remove unnecessary ones.
     
      ![Screenshot](images/AWS-Glue.png)

     The transformed dataset is then saved into a third S3 bucket named "csv-final-data-bucket", which stores the final, analysis-ready data.

4. Visualization in QuickSight
   
   Finally, the clean and transformed data in "csv-final-data-bucket" is connected to Amazon QuickSight, AWS’s business intelligence tool.

   Using QuickSight, it can:

   Build interactive dashboards and visualizations (bar charts, tables, pie charts, maps, etc.).

   Share insights with stakeholders.

   Enable data-driven decision-making using real-time dashboards based on your CSV input.



## IAM Roles and Policies Used

1. Service: Lambda

   IAM Role Name: LambdaExecutionRole

   Key Permissions
   - AmazonS3FullAccess
   - AWSLambdaBasicExecutionRole


2. Service: Glue	

   IAM Role Name: GlueServiceRole

   Key Permissions
   - AWSGlueServiceRole
   - S3FullAccess
   - GlueConsoleFullAccess


3. Service: QuickSight	

   IAM Role Name: QuickSightAccessRole	

   Key Permissions
   - AmazonS3FullAccess


## Troubles Faced & Solutions

1. Lambda Function Errors
-










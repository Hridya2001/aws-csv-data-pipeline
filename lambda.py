import boto3
import csv
import io
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    # Get the bucket and object key from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Define the destination bucket
    destination_bucket = 'csv-processed-data-bucket'  # <-- change if needed

    try:
        # Download the file from S3
        response = s3.get_object(Bucket=source_bucket, Key=object_key)
        file_content = response['Body'].read().decode('utf-8')

        # Read and preprocess the CSV
        input_csv = csv.reader(io.StringIO(file_content))
        output_buffer = io.StringIO()
        output_csv = csv.writer(output_buffer)

        for i, row in enumerate(input_csv):
            if i == 0:
                output_csv.writerow(row)  # Write header as-is
            else:
                # Example preprocessing: lowercase genre and strip whitespace
                movie_id = row[0].strip()
                title = row[1].strip()
                genre = row[2].strip().lower()
                output_csv.writerow([movie_id, title, genre])

        # Save processed file to new S3 bucket
        processed_key = f"processed/{object_key}"
        s3.put_object(
            Bucket=destination_bucket,
            Key=processed_key,
            Body=output_buffer.getvalue()
        )

        return {
            'statusCode': 200,
            'body': f"Preprocessing complete. File saved to {destination_bucket}/{processed_key}"
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error processing file: {str(e)}"
        }

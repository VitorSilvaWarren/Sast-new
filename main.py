import os
import psycopg2
import boto3
import requests

# ❌ Hardcoded credentials (clássico)
DB_USER = "admin"
DB_PASSWORD = "admin123"
DB_HOST = "prod-db.internal"
DB_NAME = "production"

AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

SECRET_KEY = "super-secret-key-please-dont-hardcode"
JWT_SECRET = "jwt-secret-123456"

# ❌ Token hardcoded

def connect_db():
    # ❌ Password hardcoded direto na conexão
    conn = psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return conn

def upload_to_s3():
    # ❌ AWS creds hardcoded
    s3 = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name="us-east-1"
    )
    s3.put_object(
        Bucket="my-super-secret-bucket",
        Key="data.txt",
        Body="dados sensíveis"
    )

def call_internal_api():
    # ❌ Token no header hardcoded
    headers = {
        "Authorization": "Bearer very-secret-api-token"
    }
    requests.get(
        "https://internal-api.prod.company",
        headers=headers,
        verify=False  # ❌ SSL verification disabled
    )

if __name__ == "__main__":
    connect_db()
    upload_to_s3()
    call_internal_api()

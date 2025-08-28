import boto3

s3_client = boto3.resource("s3", region_name="us-east-1")

bucket = s3_client.Bucket("marcelofiedler2003")

for obj in bucket.objects.all():
    print(f" - {obj.key} + {obj.size} bytes")

print("listagem finalizada")

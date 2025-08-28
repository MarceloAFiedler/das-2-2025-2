import boto3

s3_client = boto3.client("s3", region_name="us-east-1")
s3_client.delete_object(Bucket="marcelofiedler2003", Key="exemplo.txt")

print("arquivo excluído com sucesso!!!")

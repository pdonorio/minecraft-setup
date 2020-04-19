#!/usr/bin/env python

import os
import boto3
from datetime import datetime


def find_latest_object(data):
    latest_modifed_file = ""
    latest_modified_date = datetime(1984, 1, 1, 0)

    for name, time in data.items():
        string_time = datetime.strptime(str(time), "%Y-%m-%d %H:%M:%S+00:00")
        if string_time > latest_modified_date:
            latest_modified_date = string_time
            latest_modifed_file = name

    return latest_modifed_file


###############
path = os.environ.get("PROJECT_DIR", "/")
os.chdir(path)

##########################
file_name = "backup-latest.tar"
bucket_name = os.environ.get("AWS_BUCKET_NAME", "minecraft-backups")
remote_file_path = ""

s3 = boto3.client("s3")

response = s3.list_objects(Bucket=bucket_name)
data = {}
for obj in response.get("Contents", []):
    data[obj.get("Key")] = obj.get("LastModified")

##########################
if len(data) < 1:
    print('No backups available')
else:
    remote_file_path = find_latest_object(data)
    print(f'Recovering from backup: {remote_file_path}')
    with open(file_name, "wb") as f:
        s3.download_fileobj(bucket_name, remote_file_path, f)

    # os.system("ls -l *.tar")
    # NOTE: sudo not needed, we are already using root inside container
    # command = f"sudo tar xfpv {file_name}"
    command = f"tar xfpv {file_name}"
    os.system(command)

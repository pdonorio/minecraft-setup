#!/usr/bin/env python

import os
import boto3
import datetime
from pathlib import Path

###############
path = os.environ.get("PROJECT_DIR", "/")
os.chdir(path)

###############
time_string = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M")
extension = "tar"
file_name = f"backup-{time_string}.{extension}"

###############
command = f'tar cfvp {file_name} data/world data/server.properties rcon'
os.system(command)
os.system("ls -l *.tar")

###############
bucket_name = os.environ.get("AWS_BUCKET_NAME", "minecraft-backups")
main_dir = Path(path)
local_file_path = str(main_dir / Path(file_name))
remote_file_path = file_name

s3 = boto3.client("s3")
s3.upload_file(local_file_path, bucket_name, remote_file_path)
print(f"Uploaded: {local_file_path}")

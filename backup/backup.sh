#!/bin/bash

DATE=$(date +%F-%H-%M-%S)

mkdir -p /home/ec2-user/backups

docker exec mysql-db \
mysqldump \
-u$MYSQL_USER \
-p$MYSQL_PASSWORD \
$MYSQL_DATABASE \
> /home/ec2-user/backups/db-backup-$DATE.sql

echo "Backup completed successfully."

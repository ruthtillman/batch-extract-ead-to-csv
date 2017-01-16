#!/bin/bash

now=$(date +"%Y_%m_%d")

mkdir /Volumes/curatend-batch/data/EAD_Ingest_Update_$now

echo /Volumes/curatend-batch/data/EAD_Ingest_Update_$now created

#Path may have issue if DCNS changes

cd /Users/rtillman/Box\ Sync/EAD_Deposit/EAD_Update; echo Found files totalling: ; ls -l | wc -l; find . -name '*.xml' -exec mv {} /Volumes/curatend-batch/data/EAD_Ingest_Update_$now \;

cd /Volumes/curatend-batch/data/EAD_Ingest_Update_$now; echo Moved files totalling: ; ls -l | wc -l;

python /Users/rtillman/Documents/Code/EAD_Batch_Ingest/process-update.py

echo Processed files and created metadata-1.csv

cp -r /Volumes/curatend-batch/data/EAD_Ingest_Update_$now /Users/rtillman/Documents/Code/EAD_Batch_Ingest/loads

echo Copied to loads

echo Type anything to unpause the process:
read continue

mv /Volumes/curatend-batch/data/EAD_Ingest_Update_$now /Volumes/curatend-batch/production/queue

echo Moved files into the PRODUCTION batch processer

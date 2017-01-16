#!/bin/bash

now=$(date +"%Y_%m_%d")

mkdir /Volumes/curatend-batch/data/EAD_Ingest_New_$now

echo /Volumes/curatend-batch/data/EAD_Ingest_New_$now created

#Path may have issue if DCNS changes

cd /Users/rtillman/Box\ Sync/EAD_Deposit/EAD_New; echo Found files totalling: ; ls -l | wc -l; find . -name '*.xml' -exec mv {} /Volumes/curatend-batch/data/EAD_Ingest_New_$now \;

cd /Volumes/curatend-batch/data/EAD_Ingest_New_$now; echo Moved files totalling: ; ls -l | wc -l;

python /Users/rtillman/Documents/Code/EAD_Batch_Ingest/process-new.py

echo Processed files and created metadata-1.csv

cp -r /Volumes/curatend-batch/data/EAD_Ingest_New_$now /Users/rtillman/Documents/Code/EAD_Batch_Ingest/loads

echo Copied to loads

mv /Volumes/curatend-batch/data/EAD_Ingest_New_$now /Volumes/curatend-batch/production/queue

echo Moved files into the batch queue processer

echo Once work completes, you will need to run post-ingest scripts, generate a CSV of filenames and PIDs, and use write-lookup.py to update the dictionary.

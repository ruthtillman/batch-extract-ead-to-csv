#!/bin/bash

now=$(date +"%Y_%m_%d")

mkdir /Volumes/curatend-batch/data/EAD_Ingest_New_$now

echo /Volumes/curatend-batch/data/EAD_Ingest_New_$now created

#Path may have issue if DCNS changes

cd /Users/rtillman/Box\ Sync/EAD_Deposit/New; echo Found files totalling: ; ls -l | wc -l; find . -name '*.xml' -exec mv {} /Volumes/curatend-batch/data/EAD_Ingest_New_$now \;

cd /Volumes/curatend-batch/data/EAD_Ingest_New_$now; echo Moved files totalling: ; ls -l | wc -l;

python /Users/rtillman/Documents/Code/FindingAidsWork_Apparently_Dont_Batch_Ingest/process-new.py

echo Processed files and created metadata-1.createCSV

mv /Volumes/curatend-batch/data/EAD_Ingest_New_$now /Volumes/curatend-batch/test/libvirt9/queue

echo Moved files into the TEST batch processer

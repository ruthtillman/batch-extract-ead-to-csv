#!/bin/bash

now=$(date +"%Y_%m_%d")

mkdir /Volumes/DCNS/data/EAD_Ingest_$now

echo /Volumes/DCNS/data/EAD_Ingest_$now created

#Path may have issue if DCNS changes

cd /Users/rtillman/Box\ Sync/EAD_Deposit/Update; echo Found files totalling: ; ls -l | wc -l; find . -name '*.xml' -exec mv {} /Volumes/DCNS/data/EAD_Ingest_$now \;

cd /Volumes/DCNS/data/EAD_Ingest_$now; echo Moved files totalling: ; ls -l | wc -l;

python /Users/rtillman/Documents/Code/FindingAidsWork_Apparently_Dont_Batch_Ingest/process.py

echo Processed files and created metadata-1.createCSV
echo Type anything to unpause the process:
read continue


mv /Volumes/DCNS/data/EAD_Ingest_$now /Volumes/DCNS/test/libvirt9/queue

echo Moved files into the TEST batch processer

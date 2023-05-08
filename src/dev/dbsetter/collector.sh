#!/bin/bash

DB="onmp_db"
USER="postgres"

RESULT=""
FOLDER=""

if [ $# -gt 0 ]; then
    FOLDER="$1"
    echo "Parsing only ${FOLDER} folder"
else
    echo "Parsing all nearest folders"
fi

echo ""

for i in $(find . -name '*.sql');
do
    echo $i
    RESULT+=' -f '
    RESULT+=$i
done

echo ''
read -p 'Do you wanna execute psql right now(y/n): ' ASK_EXEC_PSQL
echo ''

if [ $ASK_EXEC_PSQL = 'y' ]; then
    $(psql -U ${USER} -d ${DB} ${RESULT} 1>/dev/null)
else
    echo "psql -U postgres -d ${DB} ${RESULT}"
fi
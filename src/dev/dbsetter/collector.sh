#!/bin/bash

DB="onmp_db"
USER="postgres"

RESULT=""
FOLDER="."

if [ $# -gt 0 ]; then
    if [ $1 == "--drop" ]; then
        read -p 'Do you want to recreate db?(y/n): ' ASK_WANTING_TO_DROP
        if [ $ASK_WANTING_TO_DROP == "y" ]; then
            eval 'psql -U $USER -c "drop database if exists $DB;" -c "create database $DB;"'
        else
            eval 'psql -U $USER -c "drop database if exists $DB;"'
        fi

        exit 0
    fi
    FOLDER="$1"
    echo "Parsing only ${FOLDER} folder"
else
    echo "Parsing all nearest folders"
fi

for i in $(find ${FOLDER} -name '*.sql' 2>/dev/null);
do
    if [ $i == "./example_instruction.sql" ]; then
        continue
    fi
    echo ${i}
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

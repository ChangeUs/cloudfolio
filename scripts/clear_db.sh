#!/bin/sh

# python manage.py makemigrations 할 때 에러가 나면 이 스크립트를 실행해서
# db를 clear하고 다시 migration 할 것

# 단 db가 clear되므로 db의 모든 내용이 사라지므로 신중하게 사용

# local 전용으로 서버에서는 실행 X

CURRENT_DIR=${PWD##*/}

if [ $CURRENT_DIR != "scripts" -a $CURRENT_DIR != "portfolium" ]
then
    echo "Execute this shell in portfolium folder or scripts folder.."
    exit
fi

echo "Delete all migrations.."

dropdb db_local

echo "Drop the database.."

if [ $CURRENT_DIR = "scripts" ]
then
    find .. -path "../*/migrations/*.py" -not -path "../*/*/migrations/*.py" -not -name "__init__.py" -delete

elif [ $CURRENT_DIR = "portfolium" ]
then
    find . -path "./*/migrations/*.py" -not -path "./*/*/migrations/*.py" -not -name "__init__.py" -delete
fi

createdb db_local

echo "Create the database.."

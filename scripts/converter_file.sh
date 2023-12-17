#!/bin/bash
cd file-converter
python manage.py converter --input=$1 --output=$2 --sort=$3 --author=$4 --limit=$5

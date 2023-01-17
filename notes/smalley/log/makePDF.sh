#!/bin/bash

FILE="$1"
echo "$FILE"
sed -i '' 's/^.\{28\}//' $FILE
sed -i -e 'G' $FILE
sed -i '' "s/^[ \t]*//" $FILE
FILENAME="${FILE%.*}"
echo "$FILENAME"
pandoc -s --toc $FILE defaults.yaml -o ../pdf/${FILENAME}.pdf  && open ../pdf/${FILENAME}.pdf

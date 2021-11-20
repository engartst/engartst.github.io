#!/bin/bash

echo "Let's add a new piece to the website"
read -p 'Title: ' TITLE
DIR="works/${TITLE}"
echo "New folder made at $DIR"
mkdir works/$TITLE
read -p "Instrumentation: " INSTRUMENTATION
read -p "Year: " YEAR
read -p "Duration: " DURATION
printf '{"title":"%s", "instrumentation":"%s", "year":"%s", "duration":"%s"}\n' "$TITLE" "$INSTRUMENTATION" "$YEAR" "$DURATION" > works/$TITLE/config.json
read -p "Program notes: " PROGRAMNOTES
printf '%s' "$PROGRAMNOTES" > works/$TITLE/$TITLE.md
echo "Remember to add ${TITLE}ENGART.mp3, ${TITLE}ENGART.pdf, and ${TITLE}ENGART.png if applicable"

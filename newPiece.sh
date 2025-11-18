#!/bin/bash

# Security: Enable strict error handling
set -euo pipefail

# Function to validate input
validate_input() {
    local input="$1"
    local field_name="$2"
    
    # Check for empty input
    if [[ -z "$input" ]]; then
        echo "Error: $field_name cannot be empty" >&2
        return 1
    fi
    
    # Check for dangerous characters
    if [[ "$input" =~ [\;\&\|\`\$\(\)\<\>] ]]; then
        echo "Error: $field_name contains invalid characters" >&2
        return 1
    fi
    
    # Check length
    if [[ ${#input} -gt 100 ]]; then
        echo "Error: $field_name too long (max 100 characters)" >&2
        return 1
    fi
    
    return 0
}

echo "Let's add a new piece to the website"
read -p 'Title: ' TITLE

# Validate title input
if ! validate_input "$TITLE" "Title"; then
    exit 1
fi

DIR="works/${TITLE}"
echo "New folder will be created at $DIR"

# Check if directory already exists
if [[ -d "$DIR" ]]; then
    echo "Error: Directory already exists: $DIR" >&2
    exit 1
fi

# Create directory with proper permissions
mkdir -p "works/$TITLE"
read -p "Instrumentation: " INSTRUMENTATION
read -p "Year: " YEAR
read -p "Duration: " DURATION

# Validate all inputs
if ! validate_input "$INSTRUMENTATION" "Instrumentation"; then
    exit 1
fi

if ! validate_input "$YEAR" "Year"; then
    exit 1
fi

if ! validate_input "$DURATION" "Duration"; then
    exit 1
fi

# Additional validation for year (should be numeric)
if ! [[ "$YEAR" =~ ^[0-9]{4}$ ]]; then
    echo "Error: Year must be a 4-digit number" >&2
    exit 1
fi

# Create config.json with proper escaping
jq -n \
    --arg title "$TITLE" \
    --arg instrumentation "$INSTRUMENTATION" \
    --arg year "$YEAR" \
    --arg duration "$DURATION" \
    '{title: $title, instrumentation: $instrumentation, year: $year, duration: $duration}' \
    > "works/$TITLE/config.json"
read -p "Program notes: " PROGRAMNOTES

# Validate program notes (allow longer text but still validate)
if [[ ${#PROGRAMNOTES} -gt 5000 ]]; then
    echo "Error: Program notes too long (max 5000 characters)" >&2
    exit 1
fi

# Write program notes safely
printf '%s' "$PROGRAMNOTES" > "works/$TITLE/$TITLE.md"

echo "Successfully created new piece: $TITLE"
echo "Files created:"
echo "  - works/$TITLE/config.json"
echo "  - works/$TITLE/$TITLE.md"
echo "Remember to add ${TITLE}ENGART.mp3, ${TITLE}ENGART.pdf, and ${TITLE}ENGART.png if applicable"
echo "Note: This script requires 'jq' to be installed for JSON generation."

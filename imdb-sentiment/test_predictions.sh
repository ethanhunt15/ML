#!/bin/bash

# Host ports (change if you mapped differently)
SPRINGBOOT_PORT=8081

# Array of test reviews
declare -a reviews=(
  "This movie was absolutely fantastic! I loved every minute."
  "The film was boring and predictable. Not worth watching."
  "An average movie with some good scenes but mostly disappointing."
  "Best film I’ve seen all year, a masterpiece!"
  "Terrible acting, terrible script, do not recommend."
)

echo "Testing Spring Boot API on port $SPRINGBOOT_PORT ..."
echo

for review in "${reviews[@]}"
do
  echo "Review: $review"
  curl -s -X POST "http://localhost:${SPRINGBOOT_PORT}/api/predict" \
    -H "Content-Type: application/json" \
    -d "{\"text\": \"$review\"}" | jq .
  echo "------------------------------"
done

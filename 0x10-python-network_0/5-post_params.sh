#!/bin/bash
# gets a response with a header variable
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"

#!/bin/bash
# gets the methods returned by a page
curl -sILX "OPTIONS" "$1" | grep -i "allow:" | cut -d ' ' -f 2-

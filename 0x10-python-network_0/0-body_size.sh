#!/bin/bash
# displays size of body of request
curl -s "$1" | wc -c

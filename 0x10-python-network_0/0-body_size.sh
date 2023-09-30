#!/bin/bash
# A bash script that takes in URL, sends a request and displays the size of the body of the response
curl -s "$1" | wc -c

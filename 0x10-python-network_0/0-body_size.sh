#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL displays the size of body of the response
curl -s -w "%{size_download}\n" "$1"

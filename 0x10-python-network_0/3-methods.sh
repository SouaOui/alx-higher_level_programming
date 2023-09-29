#!/bin/bash
# takes URL displays all HTTP methods the server will accept.
curl -s -X OPTIONS -I "$1" | grep -i "allow" | awk -F': ' '{print $2}'

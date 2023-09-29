#!/bin/bash
# send a GET to the URL and display the body of the response
curl -sH "X-School-User-Id:98" "$1" | grep "X-School-User-Id"
#!/bin/bash
# Send a header variable to the server
curl -sH "X-School-User-Id: 98" "$1"

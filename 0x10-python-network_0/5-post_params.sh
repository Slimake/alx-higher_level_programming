#!/bin/bash
# Send Post parameters to the server
curl -sH "X-School-User-Id: 98" "$1"
curl -sF email=test@gmail.com -F subject="I will always be here for PLD" "$1"

#!/bin/bash
# Send Post parameters to the server
curl -sF email=test@gmail.com -F subject="I will always be here for PLD" "$1"

#!/bin/bash
# Displays the size of the body of the response
curl -Is "$1" | grep -i Content-Length | cut -d' ' -f2

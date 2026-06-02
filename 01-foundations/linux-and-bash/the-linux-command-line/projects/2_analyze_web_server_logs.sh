#!/bin/bash

# Analyzing Web Server Logs

file="https://raw.githubusercontent.com/elastic/examples/refs/heads/master/Common%20Data%20Formats/nginx_logs/nginx_logs"

download_file () {
    
    mkdir "$(pwd)/data"

    curl -o data/nginx_logs $file

}


#!/bin/bash

source_data="https://raw.githubusercontent.com/elastic/examples/refs/heads/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
file="data/nginx_logs"


download_file () {    
    mkdir "$(pwd)/data"
    curl -o $file $source_data
}

top_10_ip_addresses () {
    echo "Top 10 ip addreses"
    awk '{ print $1 }' $file | sort | uniq -c | sort -nr | head -n 10
}

most_common_http_status_code () { 
    echo "Most common http status code"
    awk '{print $9 }' data/nginx_logs | sort | uniq -c | sort -nr
}

count_request_per_hour () {  
    echo "Count request per hour"
}

find_error_per_code () { 
    read -p "Enter the code to search [100-500]: " input
 
    echo "Find all $input"
    awk -v code="$input" '$9 == code' data/nginx_logs
}

extract_only_post_requests () {
    read -p "Enter the method to search [GET, POST, PUT, DELETE]: " input

    echo "Extracting only $input requests"
    awk -v code="$input" 'substr($6, 2) == code' $file 
}

find_suspicious_ips_making () { 
    echo "Find suspicious ips making"
    awk '{print $1}' $file | sort | uniq -c | sort -nr | awk '$1 >= 10'
}

main () {
    option=""

    until [[ $option = "8" ]] do
        echo -e """\nWeb Server Logs Analizer

1) Download File
2) Top 10 ip addreses
3) Most common http status code
4) Count request per hour
5) Find errors per code
6) Extract only POST request
7) Find suspicious ips making
8) Exit"""

        read -p "Select an option: " option
        echo -e ""

        case $option in
            1) download_file ;;
            2) top_10_ip_addresses ;;
            3) most_common_http_status_code ;;
            4) count_request_per_hour ;;
            5) find_error_per_code ;;
            6) extract_only_post_requests ;;
            7) find_suspicious_ips_making ;;
            8) option="8" ;;
            *) option="" ;;
        esac

    done
}

main

#!/bin/bash
# case-menu: a menu driven system information program

echo << EOF
Please select:

1. Display System information
2. Display Disk Space
3. Display Home Space Utilization
0. Quit
EOF

read -p "Enter selection [0-3] > "

case "$REPLY" in
    0)  echo "Program terminated"
        exit
        ;;
    1) echo "Hostname: $HOSTNAME"
       uptime
        ;;
    2) df -h
        ;;
    3) if [[ "$(id -u)" -eq 0 ]]; then
            echo "Home Space Utilization (All Users)"
            du -sh /home/*
        else
            echo "Home space Utilization ($USER)"
            du -sh "$HOME"
        fi
        ;;
    *) echo "Invalid entry" >&2
        exit 1
        ;;
esac

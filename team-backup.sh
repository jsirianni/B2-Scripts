#!/bin/bash
# Version 0.1.0

# Rclone backup script
# Run from an hourly cron
# Will not run if backup is already in progress
# Copy mode will copy but not delete (use sync if deletion is desired)
# Will run at a max of 5mbps (0.625) during working (8am to 6pm) hours
# Verbose output is sent to /var/log/syslog

if pidof -o %PPID -x "team-backup.sh"; then
echo "backup already running"
exit 1
fi
rclone copy /<source> <remote_name>:<bucket_name> \
--buffer-size=25M \
--bwlimit "08:00,0.625M 18:00,off" \
--verbose \
--syslog
exit

# B2-Scripts
A collection of scripts for use with Backblaze's B2

## Usage
Included are two scripts, one for Linux (`team-backup.sh`) and one for FreeNas (`team-backup-freenas.sh`).
The difference being the program used to determine if the script is already running (`pidof / pgrep`).

Pass a source and destination when calling the scripts.
```
# Source is a path on the local file system
# Destination is a remotename and bucket name as a single argument
./team-backup.sh /mnt/path/to/source remotename:bucketname
```

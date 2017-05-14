#!/usr/bin/env python3
import os
#
# This class contains functions to perform common api calls to backblaze b2
#


#
# Example Variables
#
# local_dir = str('/mnt/data')
# bucket = str('remote:bucket')
#


def sync(local_dir, bucket):
    '''
    Sync a local directory with a bucket
    Files present in the bucket but not the local directory are marked for deletion
    '''
    os.system('sudo rclone sync ' + local_dir + ' ' + bucket)


def copy(local_dir, bucket):
    '''
    One way copy between a local directory and a bucket
    Files present in the bucket, but not the local directory are retained
    '''
    os.system('sudo rclone copy ' + local_dir + ' ' + bucket)


def listFiles(bucket):
    '''
    List all files in a given bucket
    '''
    os.system('sudo rclone ls ' + bucket)


def listDirs(bucket):
    '''
    List all directories in a given bucket
    '''
    os.system('sudo rclone lsd ' + bucket)


def size(bucket):
    '''
    Prints total storage consumption of a given bucket
    '''
    os.system('sudo rclone size ' + bucket)

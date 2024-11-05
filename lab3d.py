#!/usr/bin/env python3
# Author ID: arnurudeen

import subprocess

def free_space():
    # Launch the command to get the free disk space on the root directory
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", shell=True, capture_output=True, text=True)
    # Return the output as a string with utf-8 encoding and strip newline characters
    return result.stdout.strip()

if __name__ == "__main__":
    print(free_space())



#!/usr/bin/env python3

#Author ID: [Frosete]

import subprocess
def free_space():
    freespace = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    freespaceresult = freespace.communicate()
    return freespaceresult[0].decode('utf-8').strip()
    
freespaceresult = free_space()
print(freespaceresult)


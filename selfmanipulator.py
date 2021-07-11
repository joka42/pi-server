import os
import time
import sys
import subprocess


WAIT_TIME = 15.0
VERSION = "1.0.2"

print("VERSION:", VERSION)

while True:
    update_process = subprocess.Popen(["git", "remote", "update"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = update_process.communicate()
    check_process = subprocess.Popen(["git", "status", "-uno"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    check, error = check_process.communicate()
    
    if "behind" not in str(check):
        time.sleep(WAIT_TIME)
        continue
    
    print("Update available")
    upgrade_process = subprocess.Popen(["git", "pull"])
    upgrade_process.communicate()    
    os.execv(sys.executable, ['python'] + sys.argv)
    exit()

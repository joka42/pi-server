import os
import time
import sys
import subprocess


WAIT_TIME = 5.0
VERSION = 0.1

while True:
    print("VERSION:", VERSION)

    update_process = subprocess.Popen(["git", "remote", "update"])
    
    update_process.communicate()
    if update_process.stderr:
        print("Error: " + update_process.stderr)
        time.sleep(WAIT_TIME)
        continue
    
    check_process = subprocess.Popen(["git", "status", "-uno"])
    if check_process.stderr:
        print("Error: " + check_process.stderr)
        time.sleep(WAIT_TIME)
        continue
    print(check_process.stdout)
    time.sleep(WAIT_TIME)
    


#result = ""
#process = subprocess.Popen(["cat", "selfmanipulator.py"])
#process.communicate()

#print(process.stdout)
#os.system("git remote update")
#os.system("git status -uno")



"""

with open("file1.txt", "w+") as file:
    file.write("Hello this")

with open("selfmanipulator.py", "r") as file:
    lines = file.readlines()

lines[5] = "    file.write(\"Hello this\")\n"
lines[17] = "if False:\n"

with open("selfmanipulator.py", "w") as file:
    file.writelines(lines)

time.sleep(3.0)
if False:
    os.execv(sys.executable, ['python'] + sys.argv)
exit()
"""
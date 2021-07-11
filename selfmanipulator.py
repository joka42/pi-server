import os
import time
import sys
import subprocess


WAIT_TIME = 5.0
VERSION = "0.3.4"

def upgrade():



while True:
    print("VERSION:", VERSION)

    update_process = subprocess.Popen(["git", "remote", "update"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    out, err = update_process.communicate()

    print("out")
    print(out)
    print("err")
    print(err)
    
    lines = out.splitlines(True)
    if len(lines) > 1:
        print("Update available")
        upgrade_process = subprocess.Popen(["git", "pull"])
        upgrade_process.communicate()
        with open("selfmanipulator.py", "r") as file:
            print(file.readlines())
        os.execv(sys.executable, ['python'] + sys.argv)
        exit()
        
    else:
        print("No update available")
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
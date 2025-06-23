#
# Python code to run python scripts
# in a specified directory ("submissions")
# and screencapture turtle module output
# based on preset input [test]cases
# of each file. Then save the screenshots to
# directory ("screenshots")
# Script written to run in Windows 11 Python
# environment (not Windows Linux (WSL"))
#
# use cases: need to check a batch of codes if
# GUI output is correct

import subprocess
import turtle
import os
import time
import pyautogui

python_cmd = "py.exe"
max_time = 0.5

cwd = os.getcwd()
codepath = cwd + "\\submissions\\"
screenpath = cwd + "\\screenshots"
testcase_inputs = [("A","t\n45\n"), ("D","p\nred\nl\n100\n100\n")]

screenwidth, screenheight = pyautogui.size()

def clean_dir (dir):
    if os.path.isdir(dir):
        os.chdir(dir)    
        for f in os.listdir():
            os.remove(f)

clean_dir (screenpath)
if not os.path.isdir(screenpath):
    os.mkdir(screenpath)

for testcase in testcase_inputs:
    test = testcase[0]
    for code in os.listdir(codepath):
        if os.path.isdir(code):
            continue
        elif code[len(code)-3:]!='.py':
            continue
        elif code[0:4]=='temp':
            continue
        codename = code
        name = codename.split(".")[0]
        name = name.split("_")
        screenshotname = name[0]+"_"+name[1]
            
        window = turtle.Screen()
        window.screensize()
        window.setup(width=1.0,height=1.0)
        
        # 
        # windows command prompt
        #
        try:
            proc = subprocess.Popen([python_cmd,codepath+codename],text=True,stdin=subprocess.PIPE)
            proc.stdin.write(testcase[1])
            proc.stdin.flush()
            time.sleep(1)   # needed delay so that pyautogui screenshots after screen ready
            img = pyautogui.screenshot(screenpath+"\\" + "Case_"+test[0]+"_"+screenshotname+'.png',region=(0,0,screenwidth,screenheight))
            time.sleep(2)
            proc.terminate()
            proc.wait()
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e :
            print(f"Exited with exception: {e}.")
        finally:
            pass
    
    
            

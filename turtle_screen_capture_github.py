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
testcase_inputs = [("B","r\n50\n100\n"),("C","c\n50\n"),("E","f\nyellow\nc\n50\nr\n100\n200"),("F","g\n50\n"),("G","e\n300\n"),("H","a\n")]

cwd = os.getcwd()
codepath = cwd + "\\submissions\\"
screenpath = cwd + "\\images"

screenwidth, screenheight = pyautogui.size()
def clean_dir (dir):
    if os.path.isdir(dir):
        os.chdir(dir)    
        for f in os.listdir():
            os.remove(f)

clean_dir (screenpath)
if not os.path.isdir(screenpath):
    os.mkdir(screenpath)

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
    for test in testcase_inputs:
        window = turtle.Screen()
        window.screensize()
        window.setup(width=1.0,height=1.0)
        try:
            result = subprocess.run([python_cmd,codepath+codename], input=test[1],capture_output=True, timeout=max_time, text=True,shell=True,check=True)
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e :
            print("Exited with: {e}")
        finally:
            img = pyautogui.screenshot(screenpath+"\\" + "Case_"+test[0]+"_"+screenshotname+'.png',region=(0,0,screenwidth,screenheight))
        time.sleep(max_time+0.5)
        
    
            

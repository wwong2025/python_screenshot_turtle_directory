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
import pyautogui

python_cmd = "python"
testcase_inputs = [("A","4\n",2),("B","5\n",2)]

cwd = os.getcwd()
codepath = cwd + "\\submissions\\"

def clean_dir (dir):
    os.chdir(dir)    
    for f in os.listdir():
        os.remove(f)

clean_dir (cwd+"\\screenshots")

for code in os.listdir(codepath):
    codename = code
    screenshotname = codename.split(".")[0]
    for test in testcase_inputs:
        window = turtle.Screen()
        window.screensize()
        window.setup(width=1.0,height=1.0)
        try:
            result = subprocess.run([python_cmd,codepath+codename], input=test[1],capture_output=False, timeout=test[2], text=True,shell=True)
        except TimeoutError as e:
            print('error')
        finally:
            img = pyautogui.screenshot(cwd+"\\screenshots\\" + screenshotname+"_"+test[0]+'.png')

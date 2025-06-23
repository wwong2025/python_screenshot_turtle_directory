# python_screenshot_turtle_directory


Python code to run other python scripts in a specified directory ("submissions")
programmatically.

Then screencapture [turtle module] output based on preset input [test]cases of each file.

Then save the screenshots to directory ("screenshots").

**Steps**:
+ (1) Store all python scripts to be run in folder named "submissions" (could be renamed in code)
+ (2) New out folder of screenshots called "images" or "screenshots" (could be renamed in code)
+ (3) Run python code

Script written to run in Windows 11 Python environment (not Windows Linux (WSL"))

**Use cases**: check a batch of python codes if GUI output is correct

**Design considerations**, please note:
+ (1) original file turtle_screen_capture_github.py uses subprocess.run that delivered screencaptures correctly, except when turtle only turns cursor direction or draws a line. In such cases, pyautogui (screencapture module) does not screencapture at proper time but because subprocess.run can only run the new process and stops automatically at timeout, not possible to screencapture properly. Think timing issue (subprocess.run new process runs and then screencapture line of code runs in parallel in shot time to capture screen).
+ (2) new file (turtle_scren_capture_github_special_cases.py) for special cases but should also work in general case: used subprocess.popen but still needed to add a time.sleep delay. The delay parameter is from trial and error.
+ (3) pyautogui screencapture on Windows native (not WSL) needs to specify the entire screen size region to capture properly (not a window especially if using extended/ monitors of varying sizes). added code

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import sys
import argparse
import copy

USER_PROFILE = "C:\\Users\\zachn\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
CHROME_DRIVER_FILE = "C:\\chromedriver\\chromedriver.exe"

def main(filename, cid, option):
    WORKING_DIR = os.getcwd()
    FILE_NAME = copy.deepcopy(filename)
    filename = filename.split(".")
    stem = filename[0]
    suffix = filename[1]
    print("The programming language for submission : ")
    LANGUAGE_TOOL = option
    ProblemID = stem[3:]
    if ProblemID.isdecimal():
        ProblemID = chr(ord(ProblemID) - ord('0')+ord('A')-1)
    get_language_box ="var op = document.getElementsByName(\'programTypeId\')[0]; for(var i=0;i<op.length;i++){ if(op[i].innerHTML == \""+LANGUAGE_TOOL+"\") op[i].setAttribute(\'selected\',\'selected\');}"
    print(get_language_box)
    URL = "https://codeforces.com/contest/{}/problem/{}".format(cid,ProblemID)
    print(URL)
    SUBMISSION_PATH = WORKING_DIR + "\\"+ FILE_NAME
    print(SUBMISSION_PATH)
    options=Options()
    options.add_argument("--headless") #hide the window
    options.add_argument("user-data-dir={}".format(USER_PROFILE))
    
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_FILE,chrome_options=options)

    driver.get(URL)
    driver.execute_script(get_language_box)
    input_path_btn = driver.find_element_by_xpath("//input[@name='sourceFile']")
    input_path_btn.send_keys(SUBMISSION_PATH);

    submit_btn  = driver.find_element_by_xpath("//input[@value='Submit']")
    submit_btn.click()
    driver.close()



if __name__ == "__main__":
    if len(sys.argv) == 4:
        main(sys.argv[1],sys.argv[2], sys.argv[3])
    else:
        print("Usage: python {} [submission filename] [contest id] [language setting]".format(os.path.basename(sys.argv[0])))

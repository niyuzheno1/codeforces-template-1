#get contest problems by ids
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import codecs
import html2text
def main():
    print("What's the contest id? ")
    cid = input()
    URL = "https://codeforces.com/contest/{}/problems".format(cid)
    USER_PROFILE = "C:\\Users\\zachn\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
    CHROME_DRIVER_FILE = "C:\\chromedriver\\chromedriver.exe"

    options=Options()
    options.add_argument("user-data-dir={}".format(USER_PROFILE))

    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_FILE,chrome_options=options)
    driver.implicitly_wait(2)
    driver.maximize_window()

    driver.get(URL)
    OUTPUT_FILE =os.path.join(os.getcwd(),"problems.txt")
    f = codecs.open(OUTPUT_FILE, "w", "utf−8")
    f.write("for more details please visit : " + URL + "\n")
    h = html2text.HTML2Text()
    h.ignore_links = True
    f.write(h.handle(driver.page_source))
    driver.quit()

    f = open(".\\python\\s.bat", "w")
    f.write('python ..\sub.py sol%1.py {} "PyPy 3.7 (7.3.0)"'.format(cid))
    f.close()

    f = open(".\\cpp\\s.bat", "w")
    f.write('python ..\sub.py sol%1.cpp {} "GNU G++17 7.3.0"'.format(cid))
    f.close()

    f = open(".\\python\\v.bat", "w")
    f.write('python ..\gss.py {} "zucyo05"'.format(cid))
    f.close()

    f = open(".\\cpp\\v.bat", "w")
    f.write('python ..\gss.py {} "zucyo05"'.format(cid))
    f.close()

if __name__ == "__main__":
    main()

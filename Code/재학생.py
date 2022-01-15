# pip install selenium bs4 pytesseract cv2

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import *
import time

import subprocess


try:
    subprocess.Popen('C:/Program Files/Google/Chrome/Application/chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')
except:
    subprocess.Popen('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')


def sugang(driver, da): 
    i = 3
    count = 0
    n_cnt = 0
    
    
    while True:
        try:
            print(i)
            count += 1
            if count == 3:
                count=0
                i -= 1
            if i == -1:
                i=3
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lectPackReqGrid_'+str(i)+'"]/td[11]/a')))
            if n_cnt >10:
                print("실패..")
                return False
            if int(driver.find_element(By.XPATH, '//*[@id="lectPackReqGrid_'+str(i)+'"]/td[9]').text)<40:
                driver.find_element_by_xpath('//*[@id="lectPackReqGrid_'+str(i)+'"]/td[11]/a').click()
            else:
                n_cnt += 1
            count = 0
            i -= 1

        except NoSuchElementException:
            print("NoSuchElementException")
            return True
        except AttributeError:
            print("AttributeError")
            return True
        except UnexpectedAlertPresentException:
            while True:
                try:
                    da.accept()
                    break
                except KeyboardInterrupt:
                    break
                except NoAlertPresentException:
                    break
        except ElementNotInteractableException:
            print('ElementNotInteractableException')
            da.accept()
        except ElementClickInterceptedException:
            continue

    driver.close()
    return True
        
        
try:
    URL= "http://sugang.knu.ac.kr/Sugang/comm/support/login/loginForm.action?redirUrl=%2FSugang%2Fcour%2FlectReq%2FonlineLectReq%2Flist.action"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(executable_path='C:/Users/aoml3/OneDrive/바탕 화면/test/수강신청/chromedriver', options=options)
    driver.get(url= URL)
    da = Alert(driver)


    driver.find_element_by_xpath('//*[@id="user.stu_nbr"]').send_keys('2019114538')
    driver.find_element_by_xpath('//*[@id="user.usr_id"]').send_keys('aoml3245')
    driver.find_element_by_xpath('//*[@id="user.passwd"]').send_keys('egoism3658!')
    driver.find_element_by_xpath('//*[@id="loginForm"]/table/tbody/tr[4]/td/button[1]').click()
    while driver.current_url != "http://sugang.knu.ac.kr/Sugang/cour/lectReq/onlineLectReq/list.action":
        print("not correct url")
        pass
except:
    driver.close()




while sugang(driver, da):
    print('재시도 합니다')
    pass
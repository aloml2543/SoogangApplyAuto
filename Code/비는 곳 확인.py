# pip install selenium bs4 pytesseract cv2

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import *
import time
import winsound
import subprocess



def sugang(driver, da): 
    i = 0
    cnt = 0
    
    while True:
        try:
            if cnt > 200:
                driver.find_element_by_xpath('//*[@id="lectPackReqGrid_'+str(i)+'"]/td[11]/a').click()
                WebDriverWait(driver, 120).until(EC.alert_is_present())
                da.accept()
                
                driver.find_element_by_xpath('//*[@id="logout"]/button[1]').click()
                return True
            cnt+=1
            driver.refresh()
            WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lectPackReqGrid_'+str(i)+'"]/td[11]/a')))

            # if driver.find_element(By.XPATH, '//*[@id="onlineLectReqGrid_3"]/td[3]').text =="데이타통신":
            #     driver.find_element(By.XPATH, '//*[@id="onlineLectReqGrid_3"]/td[1]/input').click()
                
            if int(driver.find_element(By.XPATH, '//*[@id="lectPackReqGrid_'+str(i)+'"]/td[9]').text)<40:
                # driver.find_element(By.XPATH, '//*[@id="btn_delete"]').click()
                # WebDriverWait(driver, 2).until(EC.alert_is_present())
                # da.accept()
                # WebDriverWait(driver, 2).until(EC.alert_is_present())
                # da.accept()

                driver.find_element_by_xpath('//*[@id="lectPackReqGrid_'+str(i)+'"]/td[11]/a').click()
                for i in range(3):
                    winsound.Beep(261, 100)
                    winsound.Beep(1000, 100)
    

        except TimeoutException:
            continue
        except NoSuchElementException:
            print("NoSuchElementException")
            try:
                driver.find_element(By.XPATH, '//*[@id="lectPackReqGrid_'+str(i)+'"]/td[9]').text
                continue
            except:
                return False
        except AttributeError:
            print("AttributeError")
            try:
                driver.find_element(By.XPATH, '//*[@id="lectPackReqGrid_'+str(i)+'"]/td[9]').text
                continue
            except:
                return False
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
            continue
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException")
            continue
        except StaleElementReferenceException:
            print("StaleElementReferenceException")
            continue
        except InvalidSessionIdException:
            return True
        

try:
    subprocess.Popen('C:/Program Files/Google/Chrome/Application/chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')
except:
    subprocess.Popen('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path='C:/Users/aoml3/OneDrive/바탕 화면/test/수강신청/chromedriver', options=options)

while True:
    while True:
        now = time.localtime()
        if now.tm_hour != 18:
                break
        time.sleep(10)
    try:
        winsound.Beep(1000, 100)
        URL= "http://sugang.knu.ac.kr/Sugang/comm/support/login/loginForm.action?redirUrl=%2FSugang%2Fcour%2FlectReq%2FonlineLectReq%2Flist.action"
       
        driver.get(url= URL)
        da = Alert(driver)


        driver.find_element_by_xpath('//*[@id="user.stu_nbr"]').send_keys('2019114538')
        driver.find_element_by_xpath('//*[@id="user.usr_id"]').send_keys('aoml3245')
        driver.find_element_by_xpath('//*[@id="user.passwd"]').send_keys('egoism3658!')
        driver.find_element_by_xpath('//*[@id="loginForm"]/table/tbody/tr[4]/td/button[1]').click()
        while driver.current_url != "http://sugang.knu.ac.kr/Sugang/cour/lectReq/onlineLectReq/list.action":
            print("not correct url")

    except:
        driver.close()

    if not sugang(driver, da): break
    print('재시도 합니다')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import urllib.request

import time
from datetime import datetime
from datetime import timedelta

# 필요한 정보들
sunday = datetime.now() + timedelta(days=5)
sunday = sunday.strftime("%Y-%m-%d").split('-')
date = {"month" : sunday[1], "day" : sunday[2]}
id = 'yjch0908'
passwd = 'Joochan0908!'
stime = '11시 00분'
etime = '13시 00분'
memberList = [['이현승', '2021-18922', '010-5640-7897', '공과대학 기계공학부'], 
              ['이록희', '2021-19919', '010-4918-0665', '공과대학 건설환경공학부'],
              ['박홍근', '2021-11769', '010-2582-0467', '공과대학 재료공학부']
              ]

def startReserve():
  # 사이트 접속
  driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
  driver.get("https://athletics.snu.ac.kr/member/login")

  # 로그인
  driver.find_element(By.NAME, 'userid').send_keys('yjch0908')
  driver.find_element(By.NAME, 'passwd').send_keys('Joochan0908!')
  driver.find_element(By.XPATH,'//*[@id="memberlogin"]/form/div[3]/button').click()

  # 예약 화면으로 이동
  driver.find_element(By.XPATH, '//*[@id="category-list"]/li[6]').click()
  time.sleep(0.3)
  driver.find_element(By.XPATH, '//*[@id="facility-list"]/li/a').click()
  dates = driver.find_elements(By.CLASS_NAME, 'ondate')
  for dt in dates:
    if dt.get_attribute('data-date') == f'2024-{date["month"]}-{date["day"]}':
      dt.click()
      break
  time.sleep(0.7)
  driver.find_element(By.XPATH, '//*[@id="btn-reservation"]').click()

  # 시작 시간, 종료 시간 선택하기
  startTime = Select(driver.find_element(By.ID, 'sTime'))
  endTime = Select(driver.find_element(By.ID, 'eTime'))

  startTime.select_by_visible_text(stime)
  endTime.select_by_visible_text(etime)

  # 예약 인원 작성하기
  driver.find_element(By.ID, 'member_check_result1').find_element(By.CLASS_NAME, 'btn.btn-secondary.btn-sm.btn-check-attendance').click()
  for i in range(2,5):
    driver.find_element(By.ID, f'member_name{i}').send_keys(memberList[i-2][0])
    driver.find_element(By.ID, f'member_userno{i}').send_keys(memberList[i-2][1])
    driver.find_element(By.ID, f'member_mobile{i}').send_keys(memberList[i-2][2])
    driver.find_element(By.ID, f'member_department{i}').send_keys(memberList[i-2][3])
    driver.find_element(By.ID, f'member_check_result{i}').find_element(By.CLASS_NAME, 'btn.btn-secondary.btn-sm.btn-check-attendance').click()

  # 동의 하기
  driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//*[@id="oath"]'))
  driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//*[@id="privacy"]'))

  # 예약버튼 스크롤
  driver.execute_script('arguments[0].scrollIntoView(true);', 
                        driver.find_element(By.ID, 'btn-reservation-ajax'))

  # # recaptcha 확률적으로 통과됨
  # recaptcha_error = False
  # solver = Recaptcha_Solver(
  #     driver=driver, # Your Web Driver
  #     ffmpeg_path='', # Optional. If does not exists, it will automatically download.
  #     log=1 # If you want to view the progress.
  #     )
  # try:
  #   solver.solve_recaptcha()
  # except:
  #   print("리캡챠 진짜 ㅅ1발이네")
  #   recaptcha_error = True

  # if not recaptcha_error:
  #   # 예약 버튼 누르기
  #   driver.find_element(By.ID, 'btn-reservation-ajax').click()
  # else:
  #   print("직접 하세요")

  time.sleep(100)

while True:

  url = 'https://athletics.snu.ac.kr/'
  server_date = urllib.request.urlopen(url).headers['Date']
  server_date = server_date.rstrip(' GMT')[5:]
  server_date = datetime.strptime(server_date, '%d %b %Y %H:%M:%S') + timedelta(hours=9)
  print(server_date)
  if server_date.hour == 9 and server_date.minute >= 30:
    startReserve()
    break
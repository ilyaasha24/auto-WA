import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

opt = Options()
#opt.add_argument("--user-data-dir=C:\\Users\\hp\\AppData\\Local\\Google\\Chrome\\User Data")
opt.add_argument("--disable-extensions")
opt.add_argument("--app=https://web.whatsapp.com")

response = {
  "hai": "hai juga",
  "Hai": "Hai Juga",
  "HAI": "NGGAK USAH NGEGAS, BAMBANG!",
  "HELP": "Daftar Command:\n1. hai/Hai/HAI\n2. REGISTER\n3. SHOW\n4. HELP",
}

def pm(msg):
  msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
  msg_box.send_keys(msg)
  msg_box.send_keys(Keys.RETURN);

db = []

driver = webdriver.Chrome(executable_path="<path>/chromedriver.exe", options=opt)

rcv = 'receiver name/phone number'
snd = 'sender name'

raw_input('Press Enter after Whatsapp web loaded to Continue')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(rcv))
user.click()

while True:
  time = '[' + datetime.datetime.now().strftime("%H:%M, %#m/%#d/%Y") + '] '
  p_rcv = time + rcv + ': '
  if len(driver.find_elements_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]/div[last()]/div/div/div/div[@data-pre-plain-text="{}"]/div/span[1]/span'.format(p_rcv)))>0:
    req = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]/div[last()]/div/div/div/div[@data-pre-plain-text="{}"]/div/span[1]/span'.format(p_rcv)).text
    if req in ["hai","Hai","HAI","HELP"]:
      msg = response.get(req, 'Nani?')
      pm(msg)
    elif req.startswith('REGISTER'):
      a,b,c = req.split(" ")
      db.append(b + ": " + c)
      pm('Data Tersimpan')
    elif req.startswith('SHOW'):
      pm(db)

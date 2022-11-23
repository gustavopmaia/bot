import pyautogui as p
import time

time.sleep(2)
p.scroll(-600)
p.moveTo(620,893,0)
p.click()
time.sleep(3)
p.click(1142, 687)

time.sleep(2)
p.moveTo(1193, 340)
p.dragTo(1193, 340, button='left')
p.dragTo(1400, 380, 1)
p.hotkey('ctrl', 'c')

time.sleep(2)
p.hotkey('ctrl', '3')
time.sleep(2)
p.moveTo(299, 65)
p.click()
time.sleep(2)
p.hotkey('ctrl', 'v')
p.press('enter')
time.sleep(2)
p.hotkey('ctrl', '2')
time.sleep(2)
p.moveTo(713, 393)
p.click()
p.hotkey('ctrl', 'v')
time.sleep(2)
p.moveTo(908, 385)
p.click()


time.sleep(4)
print(p.position())

#defining anticaptcha function
def acp_api_send_request(driver, message_type, data={}):
    message = {
		# this receiver has to be always set as antiCaptchaPlugin
        'receiver': 'antiCaptchaPlugin',
        # request type, for example setOptions
        'type': message_type,
        # merge with additional data
        **data
    }
    # run JS code in the web page context
    # preceicely we send a standard window.postMessage method
    return driver.execute_script("""
    return window.postMessage({});
    """.format(json.dumps(message)))
# Init the chrome options object for connection the extension
options = webdriver.ChromeOptions()
# A full path to CRX or ZIP or XPI file which was downloaded earlier 
options.add_extension('<path to the plugin>')
# Run the browser (Chrome WebDriver) with passing the full path to the downloaded WebDriver file
driver = webdriver.Chrome('chromedriver', options=options)

# Go to the empty page for setting the API key through the plugin API request
driver.get('https://antcpt.com/blank.html')

# Setting up the anti-captcha.com API key 
# replace YOUR-ANTI-CAPTCHA-API-KEY to your actual API key, which you can get from here:
# https://anti-captcha.com/clients/settings/apisetup
acp_api_send_request(
    driver,
    'setOptions',
    {'options': {'antiCaptchaApiKey': '059b13da556382af891625f7472a01d9'}}
)

# 3 seconds pause
time.sleep(3)
driver.get('https://empreenda.digito1.com.br/VotoPopular/Voto/4813')
# replace the url with the URL you want to scrap

driver.maximize_window()
# Test input
driver.find_element_by_css_selector('span[role=checkbox]').send_keys(Keys.ENTER)

# Most important part: we wait upto 120 seconds until the AntiCaptcha plugin indicator with antigate_solver class
# gets the solved class, which means that the captcha was successfully solved
WebDriverWait(browser, 120).until(lambda x: x.find_element_by_css_selector('.antigate_solver.solved'))

# Sending form
driver.find_element_by_css_selector('input[type=submit]').click()


# Point(x=756, y=391)
# Point(x=1142, y=687)
# Point(x=620, y=893)

# Point(x=283, y=125)
# Point(x=377, y=125)

# VALOR 1: Point(x=1193, y=340)
# VALOR 2: Point(x=1242, y=341)

# VSCODE: Point(x=1059, y=1047)


# SCROLL: Point(x=1911, y=583)

# Point(x=299, y=65)

# Point(x=908, y=385)

# https://medium.com/geekculture/how-to-solve-captcha-with-python-80959653dba2

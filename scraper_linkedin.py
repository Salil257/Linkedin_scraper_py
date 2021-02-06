from bs4 import BeautifulSoup
from selenium import webdriver

# specifies the path to the chromedriver.exe
# mention chromedriver's path inside the quotes

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')
driver.implicitly_wait(1)
email = input('enter the email')
paww = input('enter the password')
# locate email form by_class_name
username = driver.find_element_by_xpath('//*[@type="text"]')
# send_keys() to simulate key strokes
username.send_keys(email)  # Your log-in Email

# locate password form by_class_name
password = driver.find_element_by_xpath('//*[@type="password"]')

# send_keys() to simulate key strokes
password.send_keys(pass)  # Your password

# cliking on log in button
log_in_button = driver.find_element_by_xpath(
    '//*[@class="sign-in-form__submit-button"]')
log_in_button.click()
driver.implicitly_wait(1)
# Navigating to profile
# Profile link which you want to scrape
link = input('enter the profile link')

driver.get(link)
driver.implicitly_wait(1)

src = driver.page_source
soup = BeautifulSoup(src, 'lxml')

# one of the ways to get link of current page (profile link)
profile_link = (driver.current_url)

# personal details
name_div = soup.find('div', {'class': 'display-flex mt2'})

# name
try:
    name = name_div.find(
        'li', {'class': 'inline t-24 t-black t-normal break-words'}).get_text().strip()
except IndexError:  # To ignore any kind of error
    name = 'NULL'
except AttributeError:
    name = 'NULL'

# location
try:
    location = name_div.find(
        'li', {'class': 't-16 t-black t-normal inline-block'}).get_text().strip()
except IndexError:
    location = 'NULL'
except AttributeError:
    location = 'NULL'

# degree_level
try:
    degree_level = name_div.find(
        'span', {'class': 'dist-value'}).get_text().strip()
except IndexError:
    degree_level = 'NULL'
except AttributeError:
    degree_level = 'NULL'

# No. of connections
try:
    c_div = name_div.find(
        'ul', {'class': 'pv-top-card--list pv-top-card--list-bullet mt1'})
    connections = c_div.find(
        'span', {'class': 't-16 t-black t-normal'}).get_text().strip()
except IndexError:
    connections = 'NULL'
except AttributeError:
    connections = 'NULL'
Experience_div = soup.find('div', {
                           'class': 'pv-entity__summary-info pv-entity__summary-info--background-section'})

# recent positions
try:
    job_title = name_div.find(
        'h2', {'class': 'mt1 t-18 t-black t-normal break-words'}).get_text().strip()
except IndexError:
    job_title = 'NULL'
except AttributeError:
    job_title = 'NULL'
# company name
try:
    company_name = soup. find(
        'a', {'class': 'text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view'}).get_text().strip()
except IndexError:
    company_name = 'NULL'
except AttributeError:
    company_name = 'NULL'

# experience
try:
    experience = soup. find(
        'span', {'class': 'pv-entity__bullet-item-v2'}).get_text().strip()
except IndexError:
    experience = 'NULL'
except AttributeError:
    experience = 'NULL'

# saving outputs
output = ({'Name': name, 'Location': location, 'Degree Level': degree_level,
           'No. of Connections': connections, 'Postion': job_title, 'Company': company_name,
           'Experience': experience, 'Linked Link': profile_link})
xoutput = ({name, location, degree_level,
            connections, job_title, company_name,
            experience, profile_link})
print(output)
with open('file.xls', 'a') as f:
    headers = "Name,Location,Degree Level,No. of Connections,Position,Company,Experience,Linked Link\n"
    print(xoutput, file=f)

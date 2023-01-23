import os,time,json
import googlemaps
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

# driver = webdriver.Chrome(executable_path = DRIVER_BIN)

# url = 'https://isha.sadhguru.org/in/en/yoga-meditation/yoga-teacher-training/hatha-yoga-teacher-training/teachers-in-your-area'

# driver.get(url)

# while True:
#     try:
#         loadmore = driver.find_element_by_class_name("pager__item").click()
#         time.sleep(5)

#     except NoSuchElementException as error:
#         print('Reached bottom of page')
#         break


# soup = BeautifulSoup(driver.page_source,'html.parser')

# teachers = [] # List of teacher objects
# for item in soup.find_all('div', class_="teacher-card"):
#     props = item.find_all(class_='col-xs-10')
#     teacher = {}
#     teacher['name']     = props[0].text 
#     teacher['city']     = props[1].text
#     teacher['phone']    = props[2].text
#     teacher['email']    = props[3].text.strip()
#     teacher['website']  = props[4].text.strip()
#     teacher['programs'] = props[5].text.strip().split(', ')
#     teachers.append(teacher)

# with open('teachers.json', 'w+') as f:
#   json.dump(teachers, f, ensure_ascii=False)


MAPS_API_KEY = 'AIzaSyDQ4LfhiD17AesEqiAbHKYJQk0R8bu-uUg'
gmaps = googlemaps.Client(key=MAPS_API_KEY)

def get_teacher_cities(cities_str : str) -> list:
    return [city.strip().rstrip('.') for city in cities_str.split(' / ')]

with open('teachers.json') as f:
    teachers = json.load(f)

# Parse location and contact
counter = 0
for teacher in teachers:
    cities = []
    city_names = get_teacher_cities(teacher['city'])
    for city_name in city_names:
        city_coordinates = {}
        try:
            geocode_result = gmaps.geocode(city_name)
            city_coordinates = geocode_result[0]['geometry']['location']
        except Exception as e:
            print('Error for city name: ' + city_name)
            print(e)
            print(geocode_result)
        cities.append({'name': city_name, 'coordinates': city_coordinates})
    
    teacher['cities'] = cities
    del teacher['city']

    counter += 1
    print(counter)

with open('teacherss.json', 'w+') as f:
  json.dump(teachers, f, ensure_ascii=False)

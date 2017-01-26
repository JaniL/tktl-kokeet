import requests
from bs4 import BeautifulSoup

EXAMS_URL_FI = 'https://www.cs.helsinki.fi/exams'

def fetch_exams():
    r = requests.get(EXAMS_URL_FI)
    soup = BeautifulSoup(r.text)
    return soup.find_all('table', class_="cols-8")

def parse_exam(e, caption):
    return {
        "name": {
            "finnish": e.find('td', class_="views-field-field-db-nimi-suomi-value").text.strip(),
            "english": e.find('td', class_="views-field-field-db-nimi-englanti-value").text.strip()
        },
        "type": e.find('td', class_="views-field-field-db-koe-tyyppi-value").text.strip(),
        "code": int(e.find('td', class_="views-field-field-db-kurssikoodi-value").text.strip()),
        "level": e.find('td', class_="views-field-field-db-taso-value").text.strip(),
        "examiner": {
            "name": e.find('td', class_="views-field-field-db-htunnus-value").text.strip(),
            "url": e.find('td', class_="views-field-field-db-htunnus-value").find('a')['href']
        },
        "date": caption
    }

def parse_exams(soup):
    all_exams = []
    for exam_set in soup:
        caption = exam_set.find('caption').text
        exams = exam_set.find('tbody').find_all('tr')
        for e in exams:
            all_exams.append(parse_exam(e, caption))
        #all_exams.append(map(parse_exam, exams))
    return all_exams
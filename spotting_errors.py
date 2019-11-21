from bs4 import BeautifulSoup as bs
import requests
from random import randint

response = requests.get("https://www.indiabix.com/verbal-ability/spotting-errors/")

soup = bs(response.text, "html.parser")
container = soup.findAll('div', {'class': 'bix-div-container'})

q_set = []
question_list = []

for question_set in container:
    tr = question_set.findAll("tr")
    question_row = tr[0].findAll("td")
    question = question_row[1].text
    option_selector = tr[1].findAll("td")
    options = option_selector[0].findAll("tr")
    option = options[0].findAll("td")
    option1 = option[1].text.strip()

    option = options[1].findAll("td")
    option2 = option[1].text.strip()

    option = options[2].findAll("td")
    option3 = option[1].text.strip()

    option = options[3].findAll("td")
    option4 = option[1].text.strip()

    answer_sel = option_selector[0].findAll("div")
    answer_span = answer_sel[0].findAll("span")

    answer = answer_span[1].text.strip()
    q_set = [question, option1, option2, option3, option4, answer]
    question_list.append(q_set)

for i in range(14):

    url = "https://www.indiabix.com/verbal-ability/spotting-errors/"
    integer = 1000 + i
    new_string = url + "00" + str(integer)

    response = requests.get(new_string)

    soup = bs(response.text, "html.parser")
    container = soup.findAll('div', {'class': 'bix-div-container'})

    for question_set in container:
        tr = question_set.findAll("tr")
        question_row = tr[0].findAll("td")
        question = question_row[1].text
        option_selector = tr[1].findAll("td")
        options = option_selector[0].findAll("tr")
        option = options[0].findAll("td")
        option1 = option[1].text.strip()

        option = options[1].findAll("td")
        option2 = option[1].text.strip()

        option = options[2].findAll("td")
        option3 = option[1].text.strip()

        option = options[3].findAll("td")
        option4 = option[1].text.strip()

        answer_sel = option_selector[0].findAll("div")
        answer_span = answer_sel[0].findAll("span")

        q_set = [question, option1, option2, option3, option4, answer]
        question_list.append(q_set)

print(len(question_list))
print(question_list[randint(0,len(question_list))])

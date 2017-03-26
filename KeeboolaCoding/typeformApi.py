import requests
import json
import csv
import sys

TYPEFORM_KEY = "ac83034cfa742c0f79c26e9a612b4ba7e2aa0d3d"

# TODO: Check for status codes for error handling
# TODO: Use CSV library to produce data in CSV format
def main():
    try:
        resp = requests.get("https://api.typeform.com/v1/forms?key=" + TYPEFORM_KEY)
        resp.raise_for_status()
        FORM_ID = resp.json()[0]['id']
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)

    try:    
        resp = requests.get("https://api.typeform.com/v1/form/"+FORM_ID+"?key="+TYPEFORM_KEY)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    qIds = []
    data = []
    questions = []

    writer = csv.writer(open('results.csv', 'w'), delimiter=',')

    for question in resp.json()["questions"]:
        questions.append(question["question"])
        if question["id"] not in qIds:
            qIds.append(question["id"])

    writer.writerow(questions)
    for i, response in enumerate(resp.json()["responses"]):
        answers = response["answers"]
        data.append([])
        for qid in qIds:
            try:
                data[i].append(answers[qid])
            except:
                data[i].append("NaN")

    writer.writerows(data)

if __name__ == '__main__':
    main()
            
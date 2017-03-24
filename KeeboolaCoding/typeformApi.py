import requests
import json

TYPEFORM_KEY = "ac83034cfa742c0f79c26e9a612b4ba7e2aa0d3d"

# TODO: Check for status codes for error handling
# TODO: Use CSV library to produce data in CSV format
def main():
    resp = requests.get("https://api.typeform.com/v1/forms?key=" + TYPEFORM_KEY)
    FORM_ID = resp.json()[0]['id']
    resp = requests.get("https://api.typeform.com/v1/form/"+FORM_ID+"?key="+TYPEFORM_KEY)
    with open('data.txt', 'w') as outfile:
    	json.dump(resp.json(), outfile)
    qIds = []

    for question in resp.json()["questions"]:
        print(question["question"])
        if question["id"] not in qIds:
            qIds.append(question["id"])

    for response in resp.json()["responses"]:
        answers = response["answers"]
        for qid in qIds:
            try:
                print(answers[qid])
            except:
                print("NaN")

if __name__ == '__main__':
    main()
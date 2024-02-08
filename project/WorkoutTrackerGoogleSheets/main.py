import requests
import datetime
import os

GENDER = "Male"
WEIGHT_KG = "70"
HEIGHT_CM = "5"
AGE = "35"

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("APP_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
exercise_result = response.json()
print(exercise_result)


#Todo: second part to update the sheet


sheet_url = "https://api.sheety.co/0b21882be54bbc8da91888790d84dd28/myWorkouts/workouts"

today = datetime.datetime.now()
today_date = today.strftime('%d/%m/%Y')
today_time = today.strftime('%X')


for value in exercise_result.values():
    to_update = {
      "workout":
        {
          "date": today_date,
          "time": today_time,
          "exercise": value[0]["user_input"],
          "duration": value[0]["duration_min"],
          "calories": value[0]["nf_calories"]
        }
    }

    # headers = {'Content-type': 'application/json'}


    exercise_response = requests.post(sheet_url, json=to_update)
    print(exercise_response.text)


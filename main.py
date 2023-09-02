import requests
import datetime

API_KEY = "d934f7e0242389586c4928c1e9db0f8b"
APP_ID = "90bc36e0"
SHEETY_KEY = "Bearer uqefh45efe"
def get_exercises():
    headers= {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        "x-remote-user-id": "0",
        "Content-Type" : "application/json"
    }
    query = input('What exercises did you do today: ')
    params = {
        "query": query
    }
    response = requests.post(url='https://trackapi.nutritionix.com/v2/natural/exercise',json=params,headers=headers).json()
    
    return response["exercises"]

exercises = get_exercises()

def new_row():
    header_sheety = {
        "Authorization" : SHEETY_KEY
    }
    now = datetime.datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime('%H:%M:%S')
    for i in exercises:
        sheety_params = {"workout":{
            "date" : date,
            "time" : time,
            "exercise": i["name"].capitalize(),
            "duration": str(round(int(i["duration_min"]))),
            "calories": i["nf_calories"],
        }}

        requests.post(url='https://api.sheety.co/26a098e7a85a5a8f629acd9b3c2157f0/workoutTracker/workouts',json=sheety_params,headers=header_sheety)

new_row()    
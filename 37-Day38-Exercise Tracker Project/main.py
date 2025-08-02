import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration
CONFIG = {
    "nutritionix": {
        "endpoint": "https://trackapi.nutritionix.com/v2/natural/exercise",
        "headers": {
            "x-app-id": os.getenv("ENV_NIX_APP_ID"),
            "x-app-key": os.getenv("ENV_NIX_API_KEY"),
            "Content-Type": "application/json"
        },
        "params": {
            "gender": "male",
            "weight_kg": 80,
            "height_cm": 179,
            "age": 22
        }
    },
    "sheety": {
        "endpoint": os.getenv("ENV_SHEETY_ENDPOINT"),
        "headers": {
            "Authorization": f"Bearer {os.getenv('ENV_SHEETY_TOKEN')}",
            "Content-Type": "application/json"
        }
    }
}

def get_exercises():
    exercise_text = input("Tell me which exercises you did: ")
    params = CONFIG["nutritionix"]["params"].copy()
    params["query"] = exercise_text
    
    response = requests.post(
        CONFIG["nutritionix"]["endpoint"],
        json=params,
        headers=CONFIG["nutritionix"]["headers"]
    )
    response.raise_for_status()
    return response.json()

def log_to_sheet(exercises):
    today = datetime.now().strftime("%d/%m/%Y")
    now = datetime.now().strftime("%X")
    
    for exercise in exercises["exercises"]:
        data = {
            "workout": {
                "date": today,
                "time": now,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }
        
        response = requests.post(
            CONFIG["sheety"]["endpoint"],
            json=data,
            headers=CONFIG["sheety"]["headers"]
        )
        print(f"Response for {exercise['name']}: {response.status_code}")
        print(response.json())

def main():
    print("Workout Tracker")
    exercises = get_exercises()
    print("\nNutritionix Response:")
    print(exercises)
    
    if "exercises" in exercises:
        log_to_sheet(exercises)
    else:
        print("No exercise data found")

if __name__ == "__main__":
    main()
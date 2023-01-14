import os
import requests
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")


def get_data(place, days, kind):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    sample_data = get_data("Toronto", "1", "1")
    print(sample_data)

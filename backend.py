import os
import requests
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")


def get_data(place, days, kind):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [temp_dict["main"]["temp"] for temp_dict in filtered_data]
    if kind == "Sky":
        filtered_data = [sky_dict["weather"][0]["main"] for sky_dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    sample_data = get_data(place="Toronto", days=3, kind="Temperature")
    print(sample_data)

import requests

API_KEY = "1aaae77aa7636bcf8f7d7c0353b1dec5"


def get_data(place, forecast_days=None):
    # get data by city ID
    #url =f"http://api.openweathermap.org/data/2.5/forecast?id={place}&appid={API_KEY}"
    # get data by city name
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    # filter data
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(len(get_data(place="Tokyo", forecast_days=3, kind="Temperature")))
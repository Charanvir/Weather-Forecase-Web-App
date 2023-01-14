def get_data(days):
    date = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10, 11, 12]
    temperatures = [days * i for i in temperatures]
    return date, temperatures

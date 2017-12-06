import requests

def get_weather(url):
    result=requests.get(url)
    print(result.text)
    if result.status_code==200:
        return result.json()
    else:
        print('что то не то')
if __name__ == "__main__":
    data=get_weather("http://api.openweathermap.org/data/2.5/weather?id=524901&APPID=10f4e7c336ea6e6ee44ae6eecf19902b&units=metric")
    print(data)
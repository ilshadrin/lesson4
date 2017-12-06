from datetime import datetime
from flask import Flask, request
from req import get_weather

city_id=524901
apikey='10f4e7c336ea6e6ee44ae6eecf19902b'



app=Flask(__name__)
@app.route('/')

def index():
    url="http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric" % (city_id, apikey)
    weather=get_weather(url)
    print('type ', type(weather))
    cur_date=datetime.now().strftime('%d,%m,%Y')
  
    result="<p><b>T:<b> %s<p>" % weather['main']['temp']
    result+='<p><b>Город:<b> %s<p>' % weather['name']
    result+='<p><b>Date:<b>%s<p>' % cur_date
    return result
'''
@app.route('/news')
def all_the_news():
    for intem 
    return 'News'

    '''

@app.route('/news/<int:news_id>')
def news_by_id(news_id):
    return 'Новость: %s'  % news_id


if __name__ == "__main__":
    app.run(port=5010)
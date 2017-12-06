'''
На сайте портала открытых данных Москвы есть таблица с популярными именами новорожденных. 
Напишите функцию, которая получает данные при помощи requests и читает содержимое в формате json. 
Для получения данных используйте ссылку http://api.data.mos.ru/v1/datasets/2009/rows
'''


import requests
import json

def get_tab(url):
    result=requests.get(url)
    #print(result.text)
    #print('ttttttttttttt',  type(result.json()))
    return result.json() 


'''
    if result.status_code==200:
        return result.json()
    else:
        print('что то не то')

'''

if __name__ == "__main__":
    inf1=get_tab("https://apidata.mos.ru/v1/datasets/2009/rows?api_key=5c2c86bfd50d746870bb0158d15cbac4")
    #print(inf1)
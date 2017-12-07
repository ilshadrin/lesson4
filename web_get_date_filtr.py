'''
Ограничьте выводимые данные одним годом. Год должен указываться в URL как параметр, например /names?year=2016.

'''

import requests
from flask import Flask, request
from get_dat import get_tab

app=Flask(__name__)


@app.route('/name')


def name_baby():
    url="https://apidata.mos.ru/v1/datasets/2009/rows?api_key=5c2c86bfd50d746870bb0158d15cbac4"
    year_choice=int(request.args.get('year', 2015))
    year_choice_2=int(year_choice)
    baby_list=get_tab(url) 
    result1 ='<table>'
    result1+='<tr>'
    result1+='<th>Name:  </th>' 
    result1+='<th>NumberOfPersons: </th>'
    result1+='<th>Year:  </th>'
    result1+='</tr>'  
    
    for dict_1_baby_list in baby_list:
        dict_2_baby_list=dict_1_baby_list['Cells'] 
        if dict_2_baby_list['Year']==year_choice_2:
         
            result1+='<tr>'
            result1+='<td> %s</td>' % dict_2_baby_list['Name']
            result1+="<td> %s</td>" % dict_2_baby_list['NumberOfPersons']
            result1+="<td> %s</td>" % dict_2_baby_list['Year']
            result1+='</tr>'        
            print(result1)
        
        
            
            
    result1+='</table>'
    return result1



if __name__ == "__main__":
    app.run()


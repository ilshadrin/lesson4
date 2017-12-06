import requests
#from get_dat import get_tab
from flask import Flask, request

#url="https://apidata.mos.ru/v1/datasets/2009/rows?api_key=5c2c86bfd50d746870bb0158d15cbac4"
app=Flask(__name__)
@app.route('/')




   

def name_baby():
    url="https://apidata.mos.ru/v1/datasets/2009/rows?api_key=5c2c86bfd50d746870bb0158d15cbac4"
    result=requests.get(url)
    baby_list=result.json() 
    result1 ='<table>'
    result1+='<tr>'
    result1+='<th>Name:  </th>' 
    result1+='<th>NumberOfPersons: </th>'
    result1+='<th>Year:  </th>'
    result1+='</tr>'
  
    count=0
    for dict_1_baby_list in baby_list:
        dict_2_baby_list=dict_1_baby_list['Cells']
        
        result1+='<tr>'
        result1+='<td> %s</td>' % dict_2_baby_list['Name']
        result1+="<td> %s</td>" % dict_2_baby_list['NumberOfPersons']
        result1+="<td> %s</td>" % dict_2_baby_list['Year']
        result1+='</tr>'
        
        print(result1)
        count+=1
        if count==10:
            break
            
    result1+='</table>'
    return result1



if __name__ == "__main__":
    app.run()

'''
    result1='<table>'
    result1+='<tr>'
    result1+='<th>Name:  </th>' 
    result1+='<th>NumberOfPersons: '
    result1+='<th>Month:  </th>' 
    result1+='</tr>'
    result1+='<tr>'
    result1+= baby_list['Name']
    result1+= baby_list['NumberOfPersons']
    result1+= baby_list['Month']
    result1+='</tr>'
    result1+='</table>'

'''
        
   



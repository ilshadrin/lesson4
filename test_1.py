

import requests
from flask import Flask, request


app=Flask(__name__)
#@app.route('/name')

@app.route('/')
def filtr_year():
    year_choice=request.args.get('year', 2015)
   
    print(year_choice)
    print(type(year_choice))
    a=int(year_choice)
    print(a, type(a))

        #for item in request.args:
         #   print(item)
         #   print(request.args.get.item)
    return year_choice

def name_baby():
    result1= filtr_year()   
    print(result1)
    return result1



if __name__ == "__main__":
    app.run()

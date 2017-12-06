
list1=[{"global_id":659958317,"Number":3195,"Cells":{"global_id":659958317,"Name":"Сумая","Year":2017,"NumberOfPersons":7,"Month":"август"}},{"global_id":659959118,"Number":3196,"Cells":{"global_id":659959118,"Name":"Марта","Year":2017,"NumberOfPersons":7,"Month":"август"}}]

for a in list1:
    print('СПИСОК= ', a , type(a))
    print('Cells = ',a['Cells'])
    b=a['Cells']
    print('Name = ', b['Name'])
    
        

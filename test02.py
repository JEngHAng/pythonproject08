# Dictionary คือ key : value
my_dict1 = { "name":"mod" , "age":30 , 555:999 , "flag":True , "wow":[ 10 , 20 , 30 ]}
my_dict2 = { "data1":[ 10 , 30 , 40 ] , 
            "data2":( 2 , 5 , 6 ) , 
            "data3":( 45 , 3 , 4 ) , 
            "data4":{ "x":111 , 
                     "y":222 }
            }
#การเข้าถึงข้อมูลใดข้อมูลหนึ่ง
print (my_dict1["name"])
print (my_dict1["age"])
print (my_dict1[555])
my_dict1["age"] = 50
print (my_dict1["age"])
#print 20 ออกมา
print (my_dict1["wow"][1])
#print 222 ออกมา
print (my_dict2["data4"]["y"])
my_dict2["data5"] = 888
print (my_dict2)

#การเข้าถึงทุกข้อมูล
for i in my_dict1 :
    print (i)

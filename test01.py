# set คือ ข้อมูล คนละชนิด ไม่ลำดับ ซ้ำไม่ได้ ถ้าซ้ำถือว่าเป็นข้อมูลตัวเดียวกัน
my_set1 = { 10 , 20 , True , 10 , "SAU" , ( 20 , "IoT")}
# เข้าถึงทุกข้อมูลของ Set 
for data in my_set1 :
    print (data)

# แก้ได้โดยทำอ้อมๆ แปลงกลับเป็น list 
my_list = list(my_set1)
print (my_list)
my_list[2] = "IoT"
print (my_list)
my_set1 = set(my_list)
print (my_set1)
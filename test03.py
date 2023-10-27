# OOP
class IotSAU :
    #data / property / field / attribute
    major = "SAU"
    name = ""
    #Method
    def showHi(self):
        print ("Hi......")
    def introduceMyself (self):
        print (f"My name is {self.major}")
        print (f"My major is {self.major}")

# สร้าง odject
odA = IotSAU()
odB = IotSAU()

#การใช้งาน data ของ odject คือ การกำหนดค่านำมาใช้หรือเรียกมาใช้
print (odA.major)
odA.major = "Wow"
odA.name = "ฟ้าร้อง"
odB.name = "ฝนตกแล้ว"

#การใช้งาน data ของ odject คือ สั่งให้Method ของ odject นั้นๆทำงาน
odA.introduceMyself()
odB.introduceMyself()
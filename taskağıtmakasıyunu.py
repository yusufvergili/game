import random

print("""
tas için=1
kagıt için=2
makas için=3
bitirmek için = 4
oyununa hoşgeldiniz....


""")




kullanıcı_skoru, robot_skoru =0,0
while True:
    kullanıcı=int(input("tas,kagıt,makas hangisi"))
    robot=random.randint(1,3)

    if(kullanıcı==1):
        if(robot==1):
            print("ikinizde puan alamadınız")
        elif(robot==2):
            print("robot puan aldı salak")
            robot_skoru+=100
        elif(robot==3):
            print("sen robotu yendin aferim gerizekalı")
            kullanıcı_skoru+=100
    elif(kullanıcı==2):
        if (robot == 2):
            print("ikinizde puan alamadınız")
        elif (robot == 3):
            print("robot puan aldı salak")
            robot_skoru += 100
        elif (robot == 1):
            print("sen robotu yendin aferim gerizekalı")
            kullanıcı_skoru += 100
    elif(kullanıcı==3):
        if (robot == 3):
            print("ikinizde puan alamadınız")
        elif (robot == 1):
            print("robot puan aldı salak")
            robot_skoru += 100
        elif (robot == 2):
            print("sen robotu yendin aferim gerizekalı")
            kullanıcı_skoru += 100

    elif(kullanıcı==4):
        print("oyun bitti")
        break
if(kullanıcı_skoru<robot_skoru):
    print("robotamı yrnildin amk")
elif(kullanıcı_skoru>robot_skoru):
    print("robotu yenmeyi başadın amcık")
else:
    print("berabere pğolar")
print("kullanıcı puanı = {}\n robot puanı= {}" .format(kullanıcı_skoru,robot_skoru))


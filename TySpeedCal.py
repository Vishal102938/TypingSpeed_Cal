from time import *
import random as r
def mistake(paratest, usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error = error + 1
        except Exception as e:
            error = error + 1 
    return error

def speed_time(time_s, time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay , 2)
    speed = len(userinput) / time_R
    return round(speed)


while(True):

    c= input(" ready to test : yes / no :")
    if c == "yes":

        test = ["Pillow is the actively maintained fork of the original Python Imaging Library (PIL)", 
        "It supports Python 3", "offers powerful tools for image loading, manipulation, and saving."]
        test1 = r.choice(test)
        print("-----     Typing Speed Calculator     -----")
        print(test1)
        print()
        print()

        time_1 = time()
        # user start writting
        testInput = input(" Enter : ")
        time_2 = time()

        print('Speed : ', speed_time(time_1, time_2,testInput) , "w/sec")
        print('Error : ', mistake(test1, testInput))
    
    elif(c == "no"):
        print("Thank You !")
        break

    else:
        print("Wrong Input")
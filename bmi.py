

def calculate_bmi(height, weight):
    print("Height= " + str(height))
    print("Weight= " + str(weight))

    BMI=weight/(height*height)
    
    print("BMI= " + str(BMI))

    if BMI<18.5:
        print("bro EAT more NIGGA ")
        return -1
    elif BMI>=18.5 and BMI<=25.0:
        print("ok bro ure good")
        return 0
    elif BMI>25.0:
        print("ni zhe ge si hei ren kuai dian qu gym bro")
        return 1

calculate_bmi(weight=53, height=1.73)


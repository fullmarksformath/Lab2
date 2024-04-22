def calculate_bmi(height, weight):
    print("Height= " + str(height))
    print("Weight= " + str(weight))

    BMI=weight/(height*height)
    
    print("BMI= " + str(BMI))

    if BMI<18.5:
        print("bro EAT more NIGGA ")
    elif BMI>=18.5 and BMI<=25.0:
        print("ok bro ure good")
    elif BMI>25.0:
        print("ni zhe ge si hei ren kuai dian qu gym bro")

calculate_bmi(weight=43, height=)


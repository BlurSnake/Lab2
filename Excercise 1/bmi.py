def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    # Add code here to calculate BMI
    bmi =weight/(height*height)

    # Add code here to display calculate BMI
    print("BMI = " + str(bmi))

    if bmi < 18.5:
        return -1

    elif  18.5 <= bmi <= 25.0:
        return 0

    elif bmi > 25.0:
        return 1


calculate_bmi(weight=57, height=1.73)
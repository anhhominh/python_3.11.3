def rain_amount(mm):
    if (mm < 40):
        tmp = abs(mm-40)
        return "You need to give your plant " + str(tmp) + "mm of water"
    else:
         return "Your plant has had more than enough water for today!"
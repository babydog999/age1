BH0 = input('請輸入您的身高： ')
BW = input('請輸入您的體重： ')
BH0 = float(BH0)
BW = float(BW)
BH = BH0 / 100

BMI = BW / (BH*BH)

if BMI < 18.5 :
    print('您過輕了')
elif BMI >= 18.5 and BMI < 24 :
    print('您屬於正常值')
elif BMI >= 24 and BMI < 27 :
    print('您過重了')
elif BMI >= 27 and BMI < 30 :
    print('您輕度肥胖')
elif BMI >= 30 and BMI < 35 :
    print('您中度肥胖')
else :
    print('您重度肥胖了')
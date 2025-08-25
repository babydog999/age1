driving = input('請問您是否開過車? ')
if driving != '是' and driving != '否' :
	print('只可輸入 是/否 ')
	raise SystemExit
	
age = input('請問您的年紀? ')
age = int(age)
if driving == '是' :

	if age >= 18 :
		print('您通過測試')
	else :
		print('未成年怎麼可以開車!')
elif driving =='否' :
	if age >= 18 :
		print('不考慮考個駕照嗎?')
	else :
		print('再等幾年就可以學了喔')
else :
	print('請輸入 是或否')
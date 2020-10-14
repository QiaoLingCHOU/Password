password = 'a12345'
i = 3
while i > 0:
	i = i - 1
	pwd = input('請輸入您的密碼:')
	if pwd == password:
		print('登入成功')
	else:
		print('密碼錯誤!')
		if i > 0:
			print('您剩下', i, '次機會!')
		else:
			print('登入失敗,無法輸入密碼')

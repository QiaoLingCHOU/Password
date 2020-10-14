password = 'a12345'
i = 3
while True:
	pwd = input('請輸入使用者密碼:')
	if pwd == password:
		print('登入成功')
		break
	else:
		i = i - 1
		if i > 0:
			print('密碼錯誤!還有', i, '次機會!')
		elif i == 0:
			print('無法輸入密碼')
			break



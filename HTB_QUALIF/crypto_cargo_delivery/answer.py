# def challenge(req):
	
# 	req.sendall(bytes('This crypto service is used for Chasa\'s delivery system!\n'
# 		'Not your average gangster.\n'
# 		'Options:\n'
# 		'1. Get encrypted message.\n'
# 		'2. Send your encrypted message.\n', 'utf-8'))
# 	try:
# 		choice = req.recv(4096).decode().strip()

# 		index = int(choice)

# 		if index == 1:
# 			req.sendall(bytes(encrypt(flag) + '\n','utf-8'))
# 		elif index == 2:
# 			req.sendall(bytes('Enter your  ciphertext:\n', 'utf-8'))
# 			ct = req.recv(4096).decode().strip()
# 			req.sendall(bytes(is_padding_ok(bytes.fromhex(ct)), 'utf-8'))
# 		else:
# 			req.sendall(bytes('Invalid option!\n', 'utf-8'))
# 			exit(1)
# 	except:
# 		exit(1)

choice　は4096バイト分受信したものを.decode().strip()、
index   はインテジャー（choice)

index == 1:
    暗号化（答）
index == 2:

        
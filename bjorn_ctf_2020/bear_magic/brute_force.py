import hashlib
import string
import random

letters = string.ascii_letters
salt = b"HwoAU_SeasonYourCuttingBoard"
counter = 0
while True:
	res = ''.join(random.choice(letters) for i in range(16))
	hashed = hashlib.md5(salt + bytes(res.encode())).hexdigest()
	if counter % 1000 == 0:
		print(counter)
	counter += 1
	# check if it's a magic hash
	if hashed[:2] == "0e" and hashed[2:].isdigit():
		print(hashed)
		print(res)
		break


import random
import string

prefix = input("Điền tiền tố cho code: \n")
noc = int(input("Nhập số code cần sinh: \n"))
code_len = int(input("Nhập độ dài code: \n"))

chars = string.ascii_uppercase+string.digits

for i in range(noc):
    code = ''.join(prefix)

    for j in range(code_len-len(prefix)):
        code = code+random.choice(chars)

    print(code)

    

import bcrypt

password = "hello"
print(password.encode())

#encrypts the password
hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
print(hashed_pw)

#checks if encrypt is true(same input) or false(different input)

# will be false
print(bcrypt.checkpw('coding'.encode(),hashed_pw.encode()))

# will be true
print(bcrypt.checkpw('hello'.encode(),hashed_pw.encode()))

import random
import string
import bcrypt

print('    Password generator!')
length = int(input('\nEnter the length of password: '))
npass = int(input('How many passwords do you want: '))

info = {}  # Use a dictionary to store {password: hash}

for x in range(npass):
    # Define character pools inside the loop
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = '@$_-&'
    all_chars = lower + upper + num + symbols

    # Generate password
    password = ''.join(random.sample(all_chars, length))
    
    # Hash the ACTUAL generated password (not a fixed string)
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    # Store in dictionary
    info[password] = hashed.decode()  # Decode hash for readability

# Print results
for idx, (pwd, pwd_hash) in enumerate(info.items(), 1):
    print(f"{idx} - Your password is [ {pwd} ]\n   Your hash is: {pwd_hash}\n")

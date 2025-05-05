# Password-generator-with-Encryption-and-Decryption-program
Password generator, Encryption and Decryption program

<h1>This repo is about two programs:</h1>

<h2>1- for Password and hash generator </h2>

This Python program generates secure random passwords and their corresponding bcrypt hashes. It starts by asking the user for two inputs: the desired password length and the number of passwords to create. Each requested password combines lowercase letters, uppercase letters, digits, and specific symbols (@$_-&) into a character pool. Using random.sample, it selects characters from this pool to build a unique password of the specified length. The program then securely hashes each generated password using bcrypt—a robust cryptographic library—by encoding the password string and adding a random salt for enhanced security. These password-hash pairs are stored in a dictionary. Finally, it displays the results cleanly, listing each numbered password alongside its bcrypt hash. The hashes are decoded to strings for readability, and the entire process ensures no two passwords share the same hash, making it suitable for secure credential management.

<h2>2- Encryption and Decryption program</h2>

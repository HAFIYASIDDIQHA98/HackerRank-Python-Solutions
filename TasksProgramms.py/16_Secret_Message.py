def encrypt():
    msg = input("Enter message: ")
    encrypted = ""
    for char in msg:
        encrypted += chr(ord(char) + 3) # Simple +3 shift
    print(f"🔒 Encrypted: {encrypted}")

def decrypt():
    msg = input("Enter encrypted message: ")
    decrypted = ""
    for char in msg:
        decrypted += chr(ord(char) - 3) # Simple -3 shift
    print(f"🔓 Decrypted: {decrypted}")

encrypt()
decrypt()

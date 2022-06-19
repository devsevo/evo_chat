from nacl.public import PrivateKey, Box
user1_private_key = PrivateKey.generate()
user2_private_key = PrivateKey.generate()
print("User 1 private key",user1_private_key)
print("User 2 private key",user2_private_key)
user1_public_key = user1_private_key.public_key
user2_public_key = user2_private_key.public_key
print("User 1 public key",user1_public_key)
print("User 2 public key",user2_public_key)
user2_box = Box(user2_private_key, user1_public_key)
print("User 1 box",user2_box)
encrypted = user2_box.encrypt(b"hi dude")
user1_box = Box(user1_private_key, user2_public_key)
print("User 2 box",user1_box)
plaintext = user1_box.decrypt(encrypted)
print("Encrypting and Sending msg : hi dude")
print("Decrypted and Received msg :", plaintext.decode('utf-8'))
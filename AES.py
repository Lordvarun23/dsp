from cryptography.hazmat.primitives.ciphers import algorithms,modes,Cipher
from cryptography.hazmat.primitives import padding

def ecnrypts(plain_text,key):
  encryptor = Cipher(algorithms.AES(key),modes.ECB())
  cipher = encryptor.encryptor()

  padding = padding.PKCS7(algorithms.AES.block_size).padder()
  pd = padding.update(plain_text.encode())+padding.finalize()

  cipher = cipher.update(pd)+cipher.finalize()

  return cipher

def decrypts(cipher_text,key):
  encryptor = Cipher(algorithms.AES(key),modes.ECB())
  cipher = encryptor.decryptor()

  plain = cipher.update(cipher_text)+cipher.finalize()
  
  pad = padding.PKCS7(algorithms.AES.block_size).unpadder()
  pd = pad.update(plain)+pad.finalize()

  return pd.decode()

key = os.urandom(32)
decrypts(encrypts("This is a secret message",key),key)

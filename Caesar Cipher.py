# Lab 1 - ITNE341 - Caesar Cipher 

def caesar_decrypt(ciphertext, shift):
   result = ""
   for char in ciphertext:
       if char.isalpha(): 
           base = ord('A') if char.isupper() else ord('a')
           result += chr((ord(char) + base + shift) % 26 + base)
       else:
           result += char
   return result
ciphertext = input("Enter the ciphertext: ")
print("\n ـــ Decryption Results : ـــ \n")
for shift in range(1, 27):
   plaintext = caesar_decrypt(ciphertext, shift)
   print(f"Shift {shift}: {plaintext}")








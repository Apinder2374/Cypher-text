from operator import index

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
n = len(alphabet)
shifted_alpha = []
m = len(text)


def encrypt(text,shift,alphabet):
    result = ""
    for letter in text:
        index = alphabet.index(letter)
        shifted_index = (index + shift) % 26
        result += alphabet[shifted_index]
    print(result)
    
        
def decrypt(text,shift,alphabet):
    result1 = ""
    for letter in text:
        index = alphabet.index(letter)
        shifted_alphabet = (index - shift) % 26
        result1 += alphabet[shifted_alphabet]
    print(result1)

if direction == "encode":
    encrypt(text, shift, alphabet)
elif direction == "decode":
    decrypt(text, shift, alphabet)
else:
    print("Invalid direction")

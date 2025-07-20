
# Ceaser Cipher
def ceaser(startTxt, shiftAmount, direction):
    endText = ""
    if direction == "decode":
        shiftAmount *= -1 # 5 * -1 = -5
    for letter in startTxt:
        if letter in alphabet:
            idx = alphabet.index(letter)
            newIdx = idx + shiftAmount
            endText += alphabet[newIdx]
        else:
            newIdx += letter
    print(f"Here's {direction}d result: {endText}")



shouldContinue = True
while shouldContinue:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: ")) % 26
    ceaser(text, shift, direction)
    result = input("Typpe 'yes' if yu want to go again, otherwise 'no': ")
    if result == "no":
        shouldContinue = False
        print("GoodBye!")


# def encryption(plainText, shiftNum):
#     encryptedText = ""
#     for letter in plainText:
#         if letter in alphabet:
#             index = alphabet.index(letter)
#             newIdx = index + shiftNum
#             newLetter = alphabet[newIdx]
#             encryptedText += newLetter
#     print(f"The encoded text is {encryptedText}")

# def decryption(encryptedText, shifNum):
#     plainText = ""
#     for letter in encryptedText:
#         index = alphabet.index(letter)
#         newIdx = index - shifNum
#         newLetter = alphabet[newIdx]
#         plainText += newLetter
#     print(f"The decoded text is {plainText}")


# if direction == "encode":
#     encryption(text, shift)
# elif direction == "decode":
#     decryption(text, shift)
# else:
#     print("Invalid Choice!")
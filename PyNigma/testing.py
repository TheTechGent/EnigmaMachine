"""
Testing string operations
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

A = "A"
B = "R"
pos_A = 0
pos_B = 17

print(alphabet[:pos_A] + B + alphabet[pos_A + 1:])
print(alphabet[:pos_B] + A + alphabet[pos_B + 1:])


# for letter in alphabet:

#     rotorspin = alphabet[1:] + alphabet[0]
#     alphabet = rotorspin
#     print(alphabet)


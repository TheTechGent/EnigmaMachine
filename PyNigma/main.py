"""
TODO:
    - Make this more robust so that it can deal with any case and spaces.
    - Give it a UI.
"""

from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma

# Separate components of the Enigma Machine
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
KB = Keyboard()
PB = Plugboard(["AR", "VE", "LY"])

# Setup Enigma Machine
ENIGMA = Enigma(B, I, II, III, PB, KB)

# Set rings
ENIGMA.set_rings((1, 1, 1))

# Set key
ENIGMA.set_key("AAA")

# Type message
message = "HELLOWORLD"
cipher_text = ""

# Encipher message
for letter in message:
    cipher_text = cipher_text + ENIGMA.encipher(letter)

print(cipher_text)
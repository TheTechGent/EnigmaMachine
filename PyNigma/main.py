"""
TODO:
    - Make this more robust so that it can deal with lettering of any case, spaces and mistakes.
    - backspaces will need to reverse the rotation of the rotor.
    - Give it a UI using pyqt.
"""

from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from components import e_rotors

# Separate components of the Enigma Machine
I = Rotor(e_rotors.I)
II = Rotor(e_rotors.II)
III = Rotor(e_rotors.III)
IV = Rotor(e_rotors.IV)
V = Rotor(e_rotors.V)
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
message = "HELLOJOE"
cipher_text = ""

# Encipher message
for letter in message:
    cipher_text = cipher_text + ENIGMA.encipher(letter)

print(cipher_text)

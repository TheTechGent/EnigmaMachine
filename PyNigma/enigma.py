from __future__ import annotations


class Enigma:

    def __init__(
        self,
        reflector: "Reflector",
        rotor1: "Rotor",
        rotor2: "Rotor",
        rotor3: "Rotor",
        plugboard: "Plugboard",
        keyboard: "Keyboard",
    ):
        self.reflector = reflector
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.plugboard = plugboard
        self.keyboard = keyboard

    def rotate_rotor(self) -> None:

        if (
            self.rotor2.left[0] == self.rotor2.notch
            and self.rotor3.left[0] == self.rotor3.notch
        ):
            self.rotor1.rotate()
            self.rotor2.rotate()
            self.rotor3.rotate()

        elif self.rotor2.left[0] == self.rotor2.notch:
            self.rotor1.rotate()
            self.rotor2.rotate()
            self.rotor3.rotate()

        elif self.rotor3.left[0] == self.rotor3.notch:
            self.rotor2.rotate()
            self.rotor3.rotate()

        else:
            self.rotor3.rotate()

    def set_rings(self, rings: tuple = (1, 1, 1)) -> None:
        self.rotor1.set_ring(rings[0])
        self.rotor2.set_ring(rings[1])
        self.rotor3.set_ring(rings[2])

    def set_key(self, key: str = "AAA") -> None:
        """
        Sets starting position of rotors. Requires three letters as str i.e."ABC" which sets rotors in order r1=A, r2=B, r3=C.
        """
        self.rotor1.rotate_to_letter(key[0])
        self.rotor2.rotate_to_letter(key[1])
        self.rotor3.rotate_to_letter(key[2])

    def encipher(self, letter: str) -> str:

        # rotate the rotors
        self.rotate_rotor()

        # signal passes through enigma machine, forward, reflect, then back.
        signal = self.keyboard.forward(letter)
        signal = self.plugboard.forward(signal)
        signal = self.rotor3.forward(signal)
        signal = self.rotor2.forward(signal)
        signal = self.rotor1.forward(signal)
        signal = self.reflector.reflect(signal)
        signal = self.rotor1.backward(signal)
        signal = self.rotor2.backward(signal)
        signal = self.rotor3.backward(signal)
        signal = self.plugboard.backward(signal)
        letter = self.keyboard.backward(signal)

        return letter

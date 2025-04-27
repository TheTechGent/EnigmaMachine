from components import e_rotors


class Rotor:
    """
    The rotors are a key element to the Enigma Machine. This is based on the 1949 Enigma 2, which had 5 rotors.
    These are defined here and can be selected:

    I = EKMFLGDQVZNTOWYHXUSPAIBRCJ, Q
    II = AJDKSIRUXBLHWTMCQGZNPYFVOE, E
    III = BDFHJLCPRTXVZNYEIWGAKMUSQO, V
    IV = ESOVPZJAYQUIRHXLNFTGKDCMWB, J
    V = VZBRGITYUPSDNHLXAWMJQOFECK, Z
    """

    def __init__(self, wiring: e_rotors) -> None:
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        match wiring:
            case e_rotors.I:
                self.right = e_rotors.value[0]
                self.notch = e_rotors.value[1]
            case e_rotors.II:
                self.right = e_rotors.value[0]
                self.notch = e_rotors.value[1]
            case e_rotors.III:
                self.right = e_rotors.value[0]
                self.notch = e_rotors.value[1]
            case e_rotors.IV:
                self.right = e_rotors.value[0]
                self.notch = e_rotors.value[1]
            case e_rotors.V:
                self.right = e_rotors.value[0]
                self.notch = e_rotors.value[1]

    def forward(self, signal: int) -> int:
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal: int) -> int:
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal

    def show(self) -> None:
        print(self.left)
        print(self.right)
        print("")

    def rotate(self, n: int = 1, forward: bool = True):
        for i in range(n):
            if forward:
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]
            else:
                self.left = self.left[25] + self.left[:25]
                self.right = self.right[25] + self.right[:25]

    def rotate_to_letter(self, letter: str):
        n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        self.rotate(n)

    def set_ring(self, n: int):

        # rotate the rotor backwards
        self.rotate(n - 1, forward=False)

        # adjust the turnover notch in relationship to the wiring
        n_notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(self.notch)
        self.notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(n_notch - (n - 1)) % 26]

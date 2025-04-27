class Plugboard:
    """
    In Enigma Machine this was used to swap letters. This class requires a list of string pairs i.e. ["AF", "WZ"]. Then swaps the first char with the second.
    """

    def __init__(self, pairs: list) -> None:
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for pair in pairs:

            A = pair[0]
            B = pair[1]
            pos_A = self.left.find(A)
            pos_B = self.left.find(B)
            self.left = self.left[:pos_A] + B + self.left[pos_A + 1 :]
            self.left = self.left[:pos_B] + A + self.left[pos_B + 1 :]

    def forward(self, signal: int) -> int:
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal: int) -> int:
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal

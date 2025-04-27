class Keyboard:
    """
    Keyboard and Lampboard
    """

    def __init__(self) -> None:
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def forward(self, letter: str) -> int:

        signal = self.alphabet.find(letter)

        return signal

    def backward(self, signal: int) -> str:

        letter = self.alphabet[signal]

        return letter

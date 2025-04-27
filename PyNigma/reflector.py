class Reflector:
    """
    Final part in the Enigma process, it bounces back the signal.
    """

    def __init__(self, wiring: str) -> None:
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring

    def reflect(self, signal: int) -> int:
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

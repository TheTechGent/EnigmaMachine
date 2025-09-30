from .configuration import e_reflectors


class Reflector:
    """
    Final stage of the Enigma encipher process, it bounces back the signal.
    There are three reflectors that can be selected.
    """

    def __init__(self, wiring: e_reflectors) -> None:  # type: ignore
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        match wiring:
            case e_reflectors.A:
                self.right = e_reflectors.A.value

            case e_reflectors.B:
                self.right = e_reflectors.B.value

            case e_reflectors.C:
                self.right = e_reflectors.C.value

    def reflect(self, signal: int) -> int:
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

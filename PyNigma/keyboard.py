class Keyboard:

    def __init__(self):
        pass

    def forward(self, letter):
         
         signal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
         
         return signal


    def backward(self, signal):

        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]     
    
        return letter
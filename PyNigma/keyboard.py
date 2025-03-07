"""
Keyboard and Lampboard
"""

class Keyboard:

    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 

    def forward(self, letter):
         
         signal = self.alphabet.find(letter)
         
         return signal


    def backward(self, signal):

        letter = self.alphabet[signal]     
    
        return letter
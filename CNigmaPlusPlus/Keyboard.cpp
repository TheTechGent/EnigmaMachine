#include "Keyboard.h"

Keyboard::Keyboard()
{
}

int Keyboard::Forward(char Letter)
{
    int Signal = Alphabet.find(Letter);
    
    return Signal;
}

char Keyboard::Backward(int Signal)
{
    char Letter = Alphabet[Signal];

    return Letter;
}

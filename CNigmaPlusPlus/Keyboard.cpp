#include "pch.h"
#include "Keyboard.h"

Keyboard::Keyboard(){}

size_t Keyboard::Forward(const char& Letter)
{
    const size_t Signal = Alphabet.find(Letter);
    
    return Signal;
}

char Keyboard::Backward(const size_t& Signal)
{
    const char Letter = Alphabet[Signal];

    return Letter;
}

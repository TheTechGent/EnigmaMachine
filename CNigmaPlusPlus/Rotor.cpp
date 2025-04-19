#include "pch.h"
#include "Rotor.h"

Rotor::Rotor(const E_Rotors& ChosenRotor) 
{
	switch (ChosenRotor)
	{
	case I: SetRotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'Q'); break;
	case II: SetRotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", 'E'); break;
	case III: SetRotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", 'V'); break;
	case IV: SetRotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", 'J'); break;
	case V: SetRotor("VZBRGITYUPSDNHLXAWMJQOFECK", 'Z'); break;
	}

}

void Rotor::SetRotor(const string& Wiring, const char& RingNotch)
{
	Notch = RingNotch;
	RightRotorWiring = Wiring;
}


size_t Rotor::Forward(const size_t& InSignal)
{
	const char Letter = RightRotorWiring[InSignal];
	const size_t OutSignal = LeftRotorLetters.find(Letter);

	return OutSignal;
}

size_t Rotor::Backward(const size_t& InSignal)
{
	const char Letter = LeftRotorLetters[InSignal];
	const size_t OutSignal = RightRotorWiring.find(Letter);

	return OutSignal;
}

void Rotor::ShowRotor()
{
	cout << RightRotorWiring << endl;
	cout << LeftRotorLetters << endl;
}

void Rotor::Rotate(const bool& Forward, const size_t& NumRotations)
{

	if (Forward)
	{
		for (size_t dex = NumRotations; dex != 0; dex--)
		{
			RightRotorWiring = RightRotorWiring.substr(1) + RightRotorWiring[0];
			LeftRotorLetters = LeftRotorLetters.substr(1) + LeftRotorLetters[0];
		}
	}
	else
	{
		for (size_t dex = NumRotations; dex != 0; dex--)
		{
			
			RightRotorWiring = RightRotorWiring[25] + RightRotorWiring;
			LeftRotorLetters = LeftRotorLetters[25] + LeftRotorLetters;
			RightRotorWiring.pop_back();
			LeftRotorLetters.pop_back();
		}
	}
	
}

void Rotor::RotateToLetter(const char& Letter)
{
	const size_t n = LeftRotorLetters.find(Letter);
	Rotate(n);
}

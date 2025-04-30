#include "pch.h"
#include "Rotor.h"

Rotor::Rotor(const ERotors& chosen_rotor) 
{
	switch (chosen_rotor)
	{
	case I: SetRotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'Q'); break;
	case II: SetRotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", 'E'); break;
	case III: SetRotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", 'V'); break;
	case IV: SetRotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", 'J'); break;
	case V: SetRotor("VZBRGITYUPSDNHLXAWMJQOFECK", 'Z'); break;
	}

}

void Rotor::SetRotor(const string& wiring, const char& ring_notch)
{
	notch = ring_notch;
	right_rotor_wiring = wiring;
}


size_t Rotor::Forward(const size_t& in_signal)
{
	const char letter = right_rotor_wiring[in_signal];
	const size_t out_signal = left_rotor_letters.find(letter);

	return out_signal;
}

size_t Rotor::Backward(const size_t& in_signal)
{
	const char letter = left_rotor_letters[in_signal];
	const size_t out_signal = right_rotor_wiring.find(letter);

	return out_signal;
}

void Rotor::ShowRotor() const
{
	cout << right_rotor_wiring << "\n";
	cout << left_rotor_letters << "\n";
}

char Rotor::GetCurrentRotorLetter() const
{
	 return left_rotor_letters[0];
}

void Rotor::Rotate(const bool& forward, const size_t& num_rotations)
{

	if (forward)
	{
		for (size_t dex = num_rotations; dex != 0; dex--)
		{
			right_rotor_wiring = right_rotor_wiring.substr(1) + right_rotor_wiring[0];
			left_rotor_letters = left_rotor_letters.substr(1) + left_rotor_letters[0];
		}
	}
	else
	{
		for (size_t dex = num_rotations; dex != 0; dex--)
		{
			
			right_rotor_wiring = right_rotor_wiring[25] + right_rotor_wiring;
			left_rotor_letters = left_rotor_letters[25] + left_rotor_letters;
			right_rotor_wiring.pop_back();
			left_rotor_letters.pop_back();
		}
	}
	
}

void Rotor::RotateToLetter(const char& letter)
{
	const size_t n = left_rotor_letters.find(letter);
	Rotate(n);
}

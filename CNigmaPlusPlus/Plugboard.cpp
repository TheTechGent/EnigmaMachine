#include "pch.h"
#include "Plugboard.h"

Plugboard::Plugboard(const vector<string>& LetterPairs)
{
	for (string Pair : LetterPairs)
	{
		char Letter1 = Pair[0];
		char Letter2 = Pair[1];

		size_t Pos1 = PlugboardAlphabet.find(Letter1);
		size_t Pos2 = PlugboardAlphabet.find(Letter2);

		if (Pos1 != string::npos && Pos2 != string::npos)
		{
			swap(PlugboardAlphabet[Pos1], PlugboardAlphabet[Pos2]);
		}
	}
}

size_t Plugboard::Forward(const size_t& InSignal)
{
	const char Letter = ReferenceAlphabet[InSignal];
	const size_t OutSignal = PlugboardAlphabet.find(Letter);

	return OutSignal;
}

size_t Plugboard::Backward(const size_t& InSignal)
{
	const char Letter = PlugboardAlphabet[InSignal];
	const size_t OutSignal = ReferenceAlphabet.find(Letter);

	return OutSignal;
}

void Plugboard::Show()
{
	cout << PlugboardAlphabet << endl;
}

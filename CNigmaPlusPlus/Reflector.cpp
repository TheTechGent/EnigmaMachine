#include "pch.h"
#include "Reflector.h"

Reflector::Reflector(const Reflectors& ChosenReflector = Reflectors::A)
{
	switch (ChosenReflector)
	{
	case A:
		SetReflector("EJMZALYXVBWFCRQUONTSPIKHGD");
		break;

	case B:
		SetReflector("YRUHQSLDPXNGOKMIEBFZCWVJAT");
		break;

	case C:
		SetReflector("FVPJIAOYEDRZXWGCTKUQSBNMHL");
		break;

	}
}

size_t Reflector::Reflect(const size_t& InSignal)
{
	const char Letter = RightReflectorWiring[InSignal];
	const size_t OutSignal = LeftReflectorLetters.find(Letter);

	return OutSignal;
}

void Reflector::SetReflector(const string& ChosenReflector)
{
	RightReflectorWiring = ChosenReflector;
}

#pragma once

/*
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
*/

enum Reflectors
{
	A,
	B,
	C
};

class Reflector
{

public:

	Reflector(const Reflectors& ChosenReflector);

	size_t Reflect(const size_t& InSignal);

	void SetReflector(const string& Reflector);

	string RightReflectorWiring;
	string LeftReflectorLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

};


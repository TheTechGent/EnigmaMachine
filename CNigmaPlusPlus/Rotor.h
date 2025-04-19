#pragma once

enum E_Rotors 
{
	I,
	II, 
	III,
	IV,
	V
};

class Rotor
{

public:

	Rotor(const E_Rotors& ChosenRotor);

	void SetRotor(const string& Wiring, const char& Notch);

	void ShowRotor();

	void Rotate(const bool& Forward = true, const size_t& NumRotations = 1);

	void RotateToLetter(const char& Letter);

	size_t Forward(const size_t& InSignal);

	size_t Backward(const size_t& InSignal);
	
	// Property Members

	string LeftRotorLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	string RightRotorWiring;
	char Notch;

};


#pragma once

#include "Keyboard.h"
#include "Plugboard.h"
#include "Rotor.h"
#include "Reflector.h"
#include "Logs.h"

class EnigmaMachine
{

public:

	EnigmaMachine(
		Reflector *reflector,
		Rotor *rotor1,
		Rotor *rotor2,
		Rotor *rotor3,
		Plugboard *plugboard,
		Keyboard *keyboard);

	void Run();

	char Encipher(const char& Letter);

private:

	void RotateRotor();

	Logs Log;

	// Enigma Components
	Reflector *REF;
	Rotor *R1;
	Rotor *R2;
	Rotor *R3;
	Plugboard *PB;
	Keyboard *KB;
};


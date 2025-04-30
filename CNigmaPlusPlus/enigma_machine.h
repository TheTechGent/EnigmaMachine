#pragma once

#include "Keyboard.h"
#include "Plugboard.h"
#include "Rotor.h"
#include "Reflector.h"
#include "Logs.h"

class EnigmaMachine
{

public:

	explicit EnigmaMachine(
		Reflector& reflector,
		Rotor& rotor_1,
		Rotor& rotor_2,
		Rotor& rotor_3,
		Plugboard& plugboard,
		Keyboard& keyboard);

	void Run() const;
	static void PrintMessages(const string& original_message, const string& enciphered_message);
	static void ClearConsole();
	char Encipher(char letter) const;

private:

	void RotateRotor() const;

	Logs log;

	// Enigma Components
	Reflector* const ref;
	Rotor* const r1;
	Rotor* const r2;
	Rotor* const r3;
	Plugboard* const pb;
	Keyboard* const kb;
};


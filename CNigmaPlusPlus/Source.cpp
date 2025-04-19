#include "pch.h"
#include "EnigmaMachine.h"
#include "Logs.h"

int main(int argc, char* argv[])
{
	// Initialise Enigma Machine Components and configure for desired message
	Keyboard *KB = new Keyboard();
	Plugboard *PB = new Plugboard({});
	Rotor *R1 = new Rotor(E_Rotors::I);
	Rotor *R2 = new Rotor(E_Rotors::II);
	Rotor *R3 = new Rotor(E_Rotors::III);
	Reflector *REF = new Reflector(Reflectors::B);

	// Initialise Enigma Machine (EM)
	EnigmaMachine EM(REF, R1, R2, R3, PB, KB);

	//R1.ShowRotor();
	//cout << endl;
	//R1.Rotate();
	//R1.ShowRotor();
	//cout << endl;
	//R1.Rotate(false);
	//R1.ShowRotor();

	// Run Console Program
	EM.Run();

	return 0;
}
#include "pch.h"
#include "enigma_machine.h"

int main(int argc, char* argv[])
{
	// Enigma Machine primary Components. These can be configured for different message enciphering.
	Keyboard kb;
	Plugboard pb({});
	Rotor r1(ERotors::I);
	Rotor r2(ERotors::II);
	Rotor r3(ERotors::III);
	Reflector ref(Reflectors::B);

	EnigmaMachine em(ref, r1, r2, r3, pb, kb);

	// Runs Console Program
	em.Run();

	return 0;
}
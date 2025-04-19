#include "pch.h"
#include "EnigmaMachine.h"

EnigmaMachine::EnigmaMachine(Reflector *reflector, Rotor *rotor1, Rotor *rotor2, Rotor *rotor3, Plugboard *plugboard, Keyboard *keyboard) : 
REF(reflector), R1(rotor1), R2(rotor2), R3(rotor3), PB(plugboard), KB(keyboard) 
{
}

void EnigmaMachine::Run()
{
	// Run console program.
	// TODO: Program backspace to remove a character from the messages.
	// - This is partially implemented but just realised that I would need to rotate the rotors back when I remove so as to get the correct encipher.

	bool Running = true;
	char EncipheredLetter;
	string EncipheredMessage = "";
	string TypedMessage = "";

	cout << "Type your message to encipher. Press esc to exit:\n";

	while (Running)
	{
		int TypedLetterNo = _getch();

		if (TypedLetterNo == 27) // esc
		{
			Running = false;
			break;
		}
		else if (TypedLetterNo == 32) // Space bar
		{
			TypedMessage += ' ';
			EncipheredMessage += ' ';
		}
		else if (TypedLetterNo == 8) // Backspace
		{
			TypedMessage.pop_back();
			EncipheredMessage.pop_back();
		}
		else if (isalpha(TypedLetterNo)) // A-Z
		{
			// clear console
			#ifdef _WIN32
				system("cls");
			#else		
				system("clear");
			#endif 

			TypedLetterNo = toupper(TypedLetterNo);
			char TypedLetter = static_cast<char>(TypedLetterNo);
			TypedMessage += TypedLetter;

			EncipheredLetter = Encipher(TypedLetter);
			EncipheredMessage += EncipheredLetter;

			cout << "In Letter: " << TypedMessage << "\n";
			cout << "Enciphered Message: " << EncipheredMessage << "\n";
		}
		else
		{
			// clear console
			#ifdef _WIN32
				system("cls");
			#else
				system("clear");

			#endif

				cout << "That is not a valid character - type a letter to encipher. Esc to exit.";

		}
	};
}

char EnigmaMachine::Encipher(const char& letter)
{

	RotateRotor();

	size_t Signal;

	Signal = KB->Forward(letter);
	Signal = PB->Forward(Signal);
	Signal = R3->Forward(Signal);
	Signal = R2->Forward(Signal);
	Signal = R1->Forward(Signal);
	Signal = REF->Reflect(Signal);
	Signal = R1->Backward(Signal);
	Signal = R2->Backward(Signal);
	Signal = R3->Backward(Signal);
	Signal = PB->Backward(Signal);
	const char Letter = KB->Backward(Signal);

	return Letter;
}

void EnigmaMachine::RotateRotor()
{
	int nRotation = 1;

	if (R3->LeftRotorLetters[0] == R3->Notch and R2->LeftRotorLetters[0] == R2->Notch)
	{
		R1->Rotate();
		R2->Rotate();
		R3->Rotate();

	}
	else if (R2->LeftRotorLetters[0] == R2->Notch)
	{
		R1->Rotate();
		R2->Rotate();
		R3->Rotate();
	}
	else if (R3->LeftRotorLetters[0] == R3->Notch)
	{
		R2->Rotate();
		R3->Rotate();
	}
	else
	{
		R3->Rotate();
	}

	cout << "Rotor 1 : " << "\n";
	R1->ShowRotor();
	cout << "Rotor 2 : " << endl;
	R2->ShowRotor();
	cout << "Rotor 3 : " << endl;
	R3->ShowRotor();
}


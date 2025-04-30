#include "pch.h"
#include "enigma_machine.h"

EnigmaMachine::EnigmaMachine(Reflector &reflector, Rotor &rotor_1, Rotor &rotor_2, Rotor &rotor_3, Plugboard &plugboard, Keyboard &keyboard) : 
ref(&reflector), r1(&rotor_1), r2(&rotor_2), r3(&rotor_3), pb(&plugboard), kb(&keyboard) 
{
}

void EnigmaMachine::PrintMessages(const string& original_message, const string& enciphered_message)
{
	cout << "\nTyped Message: " << original_message << "\n";
	cout << "Enciphered Message: " << enciphered_message << "\n";
}

void EnigmaMachine::Run() const
{
	// Run console program.
	// TODO: Program backspace to remove a character from the messages.
	// - This is partially implemented but the rotors need to be rotated back when a letter is removed.

	bool running = true;
	string original_message = "";
	string enciphered_message = "";

	cout << "Type your message to encipher. Press esc to exit:\n";

	while (running)
	{
		int typed_letter_no = _getch();

		if (typed_letter_no == 27) // esc
		{
			running = false;
			break;
		}
		else if (typed_letter_no == 32) // Space bar
		{
			original_message += ' ';
			enciphered_message += ' ';
		}
		else if (typed_letter_no == 8) // Backspace
		{
			if (!original_message.empty() && !enciphered_message.empty())
			{
				original_message.pop_back();
				enciphered_message.pop_back();
				ClearConsole();
				PrintMessages(original_message, enciphered_message);
			}
		}
		else if (isalpha(typed_letter_no)) // A-Z
		{
			 
			ClearConsole();

			typed_letter_no = toupper(typed_letter_no);
			const char typed_letter = static_cast<char>(typed_letter_no);
			original_message += typed_letter;
			const char enciphered_letter = Encipher(typed_letter);
			enciphered_message += enciphered_letter;

			PrintMessages(original_message, enciphered_message);
		}
		else
		{
			ClearConsole();
			cout << "That is not a valid character - type a letter to encipher. Esc to exit.";

		}
	}
}

void EnigmaMachine::ClearConsole()
{
	#ifdef _WIN32
		system("cls");
	#else
		system("clear");

	#endif
}

char EnigmaMachine::Encipher(char letter) const
{

	RotateRotor();

	size_t signal = kb->Forward(letter);
	signal = pb->Forward(signal);
	signal = r3->Forward(signal);
	signal = r2->Forward(signal);
	signal = r1->Forward(signal);
	signal = ref->Reflect(signal);
	signal = r1->Backward(signal);
	signal = r2->Backward(signal);
	signal = r3->Backward(signal);
	signal = pb->Backward(signal);
	const char enciphered_letter = kb->Backward(signal);

	return enciphered_letter;
}

void EnigmaMachine::RotateRotor() const
{
	//int n_rotation = 1;

	if (r3->left_rotor_letters[0] == r3->notch){
		if (r2->left_rotor_letters[0] == r2->notch){
			r1->Rotate();
		}
		r2->Rotate();
	}
	r3->Rotate();


	/*if (r3->left_rotor_letters[0] == r3->notch and r2->left_rotor_letters[0] == r2->notch)
	{
		r1->Rotate();
		r2->Rotate();
		r3->Rotate();

	}
	else if (r2->left_rotor_letters[0] == r2->notch)
	{
		r1->Rotate();
		r2->Rotate();
		r3->Rotate();
	}
	else if (r3->left_rotor_letters[0] == r3->notch)
	{
		r2->Rotate();
		r3->Rotate();
	}
	else
	{
		r3->Rotate();
	}*/

	cout << "Rotor 1 : " << r1->GetCurrentRotorLetter() << " | ";
	cout << "Rotor 2 : " << r2->GetCurrentRotorLetter() << " | ";
	cout << "Rotor 3 : " << r3->GetCurrentRotorLetter() << " | ";
}


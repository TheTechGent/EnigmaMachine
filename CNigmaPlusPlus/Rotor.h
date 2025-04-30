#pragma once

enum ERotors : uint8_t
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
	explicit Rotor(const ERotors& chosen_rotor);

	void SetRotor(const string& wiring, const char& ring_notch);
	void ShowRotor() const;
	void Rotate(const bool& forward = true, const size_t& num_rotations = 1);
	void RotateToLetter(const char& letter);
	size_t Forward(const size_t& in_signal);
	size_t Backward(const size_t& in_signal);
	char GetCurrentRotorLetter() const;

	string left_rotor_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	string right_rotor_wiring;
	char notch;

};


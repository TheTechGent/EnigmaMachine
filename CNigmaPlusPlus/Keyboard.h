#pragma once

class Keyboard
{

public:

	Keyboard();

	size_t Forward(const char& Letter);

	char Backward(const size_t& Signal);

private:

	string Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

};


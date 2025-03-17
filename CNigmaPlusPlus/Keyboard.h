#pragma once
#include <iostream>

class Keyboard
{

	std::string Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

public:

	Keyboard();

	int Forward(char Letter);

	char Backward(int Signal);

};


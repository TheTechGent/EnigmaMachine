#include <iostream>
#include "Keyboard.h"

int main(int argc, char* argv[])
{
	Keyboard KB = Keyboard();

	std::cout << KB.Forward('A') << std::endl;
	std::cout << KB.Backward(0) << std::endl;

	return 0;
}
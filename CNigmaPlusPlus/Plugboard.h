#pragma once


class Plugboard
{

public:

	Plugboard(const vector<string>& LetterPairs);

	size_t Forward(const size_t& Signal);

	size_t Backward(const size_t& Signal);

	void Show();

private:

	string PlugboardAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	string ReferenceAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
};


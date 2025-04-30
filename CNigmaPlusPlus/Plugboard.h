#pragma once


class Plugboard
{

public:

	explicit Plugboard(const vector<string> &letter_pairs);

	size_t Forward(const size_t& signal);

	size_t Backward(const size_t& Signal);

	void Show() const;

private:

	string PlugboardAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	string ReferenceAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
};


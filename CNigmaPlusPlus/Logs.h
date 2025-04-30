#pragma once

enum class ERotationsLog : uint8_t
{
	rotor1_rotated = 1,
	rotor2_rotated = 2,
	rotor3_rotated = 3
};

class Logs
{

public:

	explicit Logs();

	void AddToRotorHistory(const vector<ERotationsLog>& rotor_history_step);
	void ShowRotorHistory() const;
	vector<ERotationsLog> GetRotorHistory(const bool& remove_entry=true);
	
private:

	static string ToString(const ERotationsLog& log);

	int rotor_history_key = 1;
	map<int, vector<ERotationsLog>> rotor_history;
};


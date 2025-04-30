#include "pch.h"
#include "Logs.h"

Logs::Logs()
= default;

void Logs::AddToRotorHistory(const vector<ERotationsLog>& rotor_history_step)
{
	
	rotor_history.insert(make_pair(rotor_history_key, rotor_history_step));
	
	rotor_history_key++;
}

vector<ERotationsLog> Logs::GetRotorHistory(const bool& remove_entry)
{
	vector<ERotationsLog> rotor_history_current_step;

	if (!rotor_history.empty() and remove_entry)
	{
		const auto last_entry = prev(rotor_history.end());
		rotor_history_current_step = last_entry->second;
		rotor_history.erase(last_entry);
	}
	else if (!rotor_history.empty())
	{
		const auto last_entry = prev(rotor_history.end());
		rotor_history_current_step = last_entry->second;
	}
	return rotor_history_current_step;
}

void Logs::ShowRotorHistory() const
{
	for (const auto& pair : rotor_history)
	{
		cout << "Entry: " << pair.first << "\n";
		const vector<ERotationsLog>& current_rotor_line = pair.second;
		for (const auto& log : current_rotor_line)
		{
			cout << ToString(log) << "\n";
		}
	}
	
}

string Logs::ToString(const ERotationsLog& log)
{
	switch (log)
	{
	case ERotationsLog::rotor1_rotated: return "Rotor 1 - Rotated";
	case ERotationsLog::rotor2_rotated: return "Rotor 2 - Rotated";
	case ERotationsLog::rotor3_rotated: return "Rotor 3 - Rotated";
	}

	return "Unknown";
}

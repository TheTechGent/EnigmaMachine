#pragma once

enum E_RotationsLog
{
	Rotor1_Rotated = 1,
	Rotor2_Rotated = 2,
	Rotor3_Rotated = 3
};

class Logs
{

public:

	Logs();

	void AddToRotationHistory(vector<E_RotationsLog> RHStep);

	vector<E_RotationsLog> GetLatestRotationHistory(const bool &RemoveEntry=true);

	void ShowRotationHistory();

private:

	int RHIndex = 1;

	map<int, vector<E_RotationsLog>> RHistory;
};


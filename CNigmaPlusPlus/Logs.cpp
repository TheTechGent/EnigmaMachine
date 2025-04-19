#include "pch.h"
#include "Logs.h"

Logs::Logs()
{
}

void Logs::AddToRotationHistory(vector<E_RotationsLog> RHStep)
{
	
	RHistory.insert(make_pair(RHIndex,RHStep));
	
	RHIndex++;
}

vector<E_RotationsLog> Logs::GetLatestRotationHistory(const bool& RemoveEntry)
{
	vector<E_RotationsLog> RHCurrentStep;

	if (!RHistory.empty() and RemoveEntry)
	{
		auto LastEntry = prev(RHistory.end());
		vector<E_RotationsLog> RHCurrentStep = LastEntry->second;
		RHistory.erase(LastEntry);
	}
	else if (!RHistory.empty())
	{
		auto LastEntry = prev(RHistory.end());
		vector<E_RotationsLog> RHCurrentStep = LastEntry->second;
	}
	return RHCurrentStep;
}

void Logs::ShowRotationHistory()
{
	for (int i; i < RHistory.size(); )
	{
		vector<ERotationLog> CurrentRLine = RHistory.at(i);
	}
	
}

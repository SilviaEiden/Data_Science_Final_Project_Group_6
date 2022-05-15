SELECT travel.index,
	travel."Agency",
	travel."Agency Type",
	travel."Distribution Channel",
	travel."Product Name",
	travel."Claim",
	travel."Duration",
	travel."Destination",
	travel."Age",
	money."Net Sales",
	money."Commision (in value)"
INTO travel_insurance_clean FROM travel INNER JOIN money ON travel.index = money.index;

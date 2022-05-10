travel
-
index int pk
Agency varchar
"Agency Type" varchar
"Distribution Channel" varchar
"Product Name" varchar
Claim int
Duration int
Destination varchar
Age int

money
-
index int pk fk - travel.index
"Net Sales" float
"Commision (in value)" float

travel_agency
-
index int pk fk - travel.index
Agency varchar
"Distribution Channel" varchar
"Product Name" varchar
Claim int
Duration int
Destination varchar
Age int

airlines
-
index int pk fk - travel.index
Agency varchar
"Distribution Channel" varchar
"Product Name" varchar
Claim int
Duration int
Destination varchar
Age int

online
-
index int pk fk - travel.index
Agency varchar
"Agency Type" varchar
"Product Name" varchar
Claim int
Duration int
Destination varchar
Age int

offline
-
index int pk fk - travel.index
Agency varchar
"Agency Type" varchar
"Product Name" varchar
Claim int
Duration int
Destination varchar
Age int
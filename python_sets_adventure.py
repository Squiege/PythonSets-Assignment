# Task 1

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

my_flights = set(our_routes)
other_flights = set(competitor_routes)
check_routes = my_flights.intersection(other_flights)
print(f"The common routes are: ", check_routes)

odd_routes = my_flights.difference(other_flights)
print(f"The uncommon routes are: ", odd_routes)

no_route = my_flights.symmetric_difference(other_flights)
print(f"These are the flights that we don't share: ", no_route)
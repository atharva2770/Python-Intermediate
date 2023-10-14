#### A city has N Tram stations numbered from 1 to N  that are connected to one another and form a circle.
# You are given an array ticket_cost  where ticket_cost[i] is the cost of a ticket
# between the stops number i and (i + 1) % N. The Tram can travel in both directions
# i.e. clockwise and anti-clockwise.

# Return the minimum cost to travel between the given start and finish station.
#
# You are given an integer N where N represents the total number of the tram stations,
# an integer start which represents the start station, and an integer finish which represents the finish station.
# You are given an array of positive integers  ticket_cost where ticket_cost[i] represents the ticket cost
# between the station number i and (i + 1) % N.


def solve(N, start, finish, Ticket_cost):
   counter1 = 0
   counter2 = 0

   st = min(start , finish)
   fs = max(start , finish)

   for i in range(N):
       Ticket_cost[0] = 1
       if (i >= st-1 and i < fs-1):
           counter1 = counter1 + Ticket_cost[i]
       else:
           counter2 = counter2 + Ticket_cost[i]

    if (counter1<counter2):
        return counter1
    else:
        return counter2

N = int(input())
start = int(input())
finish = int(input())
Ticket_cost = list(map(int, input().split()))

out_ = solve(N, start, finish, Ticket_cost)
print(out_)
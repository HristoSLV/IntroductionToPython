halls = int(input())
halls_capacity = int(input())
number_of_viewers = int(input())

enough_capacity = halls * halls_capacity >= number_of_viewers
print(enough_capacity)

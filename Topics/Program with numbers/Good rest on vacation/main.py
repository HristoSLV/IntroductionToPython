# put your python code here
duration_in_days = int(input())
food_cost_day = int(input())
one_way_flight = int(input())
one_hotel_night_cost = int(input())

total_food_cost = food_cost_day * duration_in_days
total_flight_cost = one_way_flight * 2
total_hotel_cost = one_hotel_night_cost * (duration_in_days - 1)

total_vacation_cost = total_food_cost + total_flight_cost + total_hotel_cost
print(total_vacation_cost)

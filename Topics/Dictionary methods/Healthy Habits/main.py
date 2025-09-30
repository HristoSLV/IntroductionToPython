# # the list "walks" is already defined
# # your code here
# walks = [
#     {"day": "Monday", "distance": 2000},
#     {"day": "Tuesday", "distance": 3000},
#     {"day": "Wednesday", "distance": 3500},
#     {"day": "Thursday", "distance": 2500},
#     {"day": "Friday", "distance": 2500},
#     {"day": "Saturday", "distance": 1000},
#     {"day": "Sunday", "distance": 5600}]
#
# sum_total = 0
# index = len(walks)
# for i in range(index):
#     sum_total += walks[i]["distance"]
#
# mean = sum_total // index
# print(walks[5]["distance"])

print(sum(walk["distance"] for walk in walks) // len(walks))

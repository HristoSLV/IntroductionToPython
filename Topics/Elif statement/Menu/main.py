def order(orders):
    if orders == "pizza":
        return "Margherita, Four Seasons, Neapolitan, Vegetarian, Spicy"
    elif orders == "salad":
        return "Caesar salad, Green salad, Tuna salad, Fruit salad"
    elif orders == "soup":
        return "Chicken soup, Ramen, Tomato soup, Mushroom cream soup"
    return "Sorry, we don't have it on the menu"


user_input = input()
print(order(user_input))

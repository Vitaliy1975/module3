import random

def get_numbers_ticket(min, max, quantity):
    if min<1:
        return []
    elif max>1000:
        return []
    elif quantity<=min or quantity>=max:
        return []
    big_list=range(min,max+1)
    random_list=random.sample(big_list,quantity)
    random_list.sort()
    return random_list

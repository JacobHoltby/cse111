import math

def compute_tip(total, percentge):
    return total * percentge



def prompt_percentage():
    percentage = input('What percentage would you like to tip?')
    return percentage

print(compute_tip(5, .01))
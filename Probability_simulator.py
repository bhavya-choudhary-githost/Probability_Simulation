import random
#initial statistics
pulls = int(input("Enter number of pulls to stimulate:" ))
pity = 0
banner_5stars = 0
standard_5stars = 0
next5star_guarantee = False

def five_star():
    global pity, banner_5stars, standard_5stars, next5star_guarantee
    if random.random() < 0.5:
        banner_5stars += 1
        next5star_guarantee = False

    elif next5star_guarantee == True:
        banner_5stars += 1
        next5star_guarantee = False

    else:
        standard_5stars += 1
        next5star_guarantee = True
    pity = 0

for pull in range(pulls):
    if pity > 73:
        chance = (pity-73)*0.06 + 0.006
    if pity <= 73:
        chance = 0.06

    if random.random() <= chance:
        five_star()

print(banner_5stars)
        

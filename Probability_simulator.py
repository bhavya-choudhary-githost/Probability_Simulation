import random
print()
#initial statistics
pulls = int(input("Enter number of pulls to stimulate: " ))
pity = 0
banner_5stars = 0
standard_5stars = 0
next5star_guarantee = False

def five_star():
    global pity, banner_5stars, standard_5stars, next5star_guarantee

    if next5star_guarantee == True:
        banner_5stars += 1
        next5star_guarantee = False

    elif random.random() < 0.5:
        banner_5stars += 1
        next5star_guarantee = False

    else:
        standard_5stars += 1
        next5star_guarantee = True
    pity = 0

for pull in range(pulls):
    if pity > 73:
        chance = (pity-73)*0.06 + 0.006
    else:
        chance = 0.006

    if random.random() <= chance:
        five_star()
    else:
        pity += 1

print()
print(f'banner 5 stars: {banner_5stars}')
print()
print(f'standard 5 stars: {standard_5stars}')
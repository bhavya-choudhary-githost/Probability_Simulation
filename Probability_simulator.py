import random

def pull_simulation(pulls):
    pity = 0
    banner_5stars = 0
    standard_5stars = 0
    chance_5star = 0
    next5star_guarantee = False
    
    for pull in range(pulls):
        if pity > 73:
            chance_5star += (pity-73) * 0.06 + 0.006
        else:
            chance_5star = 0.006

        if random.random() < chance_5star:
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
        else:
            pity += 1

    return banner_5stars, standard_5stars        
   

def main():
    pulls = int(input("Enter number of pulls: "))
#times = int(input("Enter number of times to run simulation: "))
    banner_5stars, standard_5stars = pull_simulation(pulls)
    print()
    print(banner_5stars, standard_5stars)


if __name__  == "__main__":
    main()


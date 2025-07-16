import random

def pull_simulation(pulls):
    pity = 0
    banner_5stars = 0
    standard_5stars = 0
    next5star_guarantee = False
    
    for pull in range(pulls):
        if pity > 73:
            chance_5star = (pity-73) * 0.06 + 0.006
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
    times = int(input("Enter number of times to run simulation: "))
    total_banner_5stars = 0
    total_standard_5stars = 0

    for _ in range(times):
        banner_5stars, standard_5stars = pull_simulation(pulls)
        total_banner_5stars += banner_5stars
        total_standard_5stars += standard_5stars
        print()
        print(f"Banner 5★: {banner_5stars}, Standard 5★: {standard_5stars}")

    print(f"\nAverage Banner 5★: {total_banner_5stars / times}")
    print(f"Average Standard 5★: {total_standard_5stars / times}")



if __name__  == "__main__":
    main()


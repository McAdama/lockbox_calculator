#! python3

import random
import locale
import numpy as np
locale.setlocale(locale.LC_ALL,'')


salesgoal = float(input("What's the sales goal (units sold)?\n"))
gem_price = float(input("What's the direct purchase price of the item (in in-game currency)?\n"))
lb_droprate = float(input("Whats the item drop chance from a lockbox?\n"))

# Future Dev - to allow calculations for other games
    # cur_pack = float(input("How much in-game currency (IGC) you are purchasing?\n"))
    # cur_pack_cost = float(input("What is the USD cost of the currency pack?\n"))
    # igc_cost = cur_pack_cost / cur_pack
gem_cost = .0125
usd_price = gem_price * gem_cost
direct_total = 0

def revCalc(goal):
# Calculate the direct revenue sales, if the shop sold the item directly; specify the number of units sold to determine gross revenue
    sold = 0
    rev = 0
    while sold < goal:
        sold += 1
        rev = sold * usd_price
    # Print out results
    print("\nPer Item Cost: " + str(locale.currency(usd_price)) +
        "\nTotal Direct Purchase Revenue: " + str(locale.currency(rev, grouping=True)) +
        "\n# Items Acquired: " + str(sold))   

def lockRev(goal, droprate, lockkey=99.6):
# Calculate revenue if item is held behind lockbox, specify the target number of units sold to determine gross revenue
# Lock-key is guild wars 2 specific - avg of gem cost per lock-key # 1 pack - 125, # 5 pack cost per - 90, # 25 pack cost per - 84
    rev = 0
    lockbox = 0
    win = 0
    loss = 0
    all_rolls = []
    usd_lockkey = lockkey * gem_cost
    while win < goal:
        lockbox += 1
        roll = random.uniform(0.000, 100.000)
        if roll < droprate:
            win += 1
        else:
            loss += 1
        rev = lockbox * usd_lockkey
        all_rolls.append(roll)
    # Print out results 
    print("Per Item Cost: " + str(locale.currency((rev/win), grouping=True)) +
          "\nLock Boxes Purchased: " + str(lockbox) +
          "\nTotal Lockbox Purchase Revenue: " + str(locale.currency(rev, grouping=True)) +
          "\n# Items Acquired: " + str(win) +
          "\n# Losses: " + str(loss) +
          "\n\nMean: " + str(np.mean(all_rolls)) +
          "\nStandard Dev: " + str(np.std(all_rolls)) +
          "\nCoefficient of Variation: " + str((np.mean(all_rolls))/(np.std(all_rolls))))
          

revCalc(salesgoal)
print("\n")
lockRev(salesgoal,lb_droprate)
print("\n")

    # House advantage is probability of win added to probability of losing and multiplied by total customer spend
    # so Roulette - (18/38 X 1) + (20/30 X -1) = -5.26%, if betting a dollar the house edge is -5.26 * bet * # of rounds = $0.53
    # def house_adv(win,loss,lockkey):
    # total = win + loss
    # winProb = win / total
    # lossProb = loss / total
    # monies = lockkey * total 
    # houseedge = (winProb - lossProb) * -1
    # profit = houseedge * monies
    # print(locale.currency(profit)) """



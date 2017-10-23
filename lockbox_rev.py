#! python3

import random
import locale

locale.setlocale(locale.LC_ALL,'')
salesgoal = float(input("What's the sales goal (units sold)?\n"))
gem_price = float(input("What's the direct purchase price (in in-game currency)?\n"))
lb_droprate = float(input("Whats the lockbox drop chance?\n"))
cur_pack = float(input("What is the size of the currency pack you are purchasing?\n"))
cur_pack_cost = float(input("What is the cost of the currency pack?\n"))
gem_cost = cur_pack_cost / cur_pack
dol_price = gem_price * gem_cost
direct_total = 0

def revCalc(goal):
    global direct_total
    sold = 0
    rev = 0
    while sold < goal:
        sold += 1
        rev = sold * dol_price
    print("\nPer Item Cost: " + str(locale.currency(dol_price)) +
        "\nTotal Direct Purchase Revenue: " + str(locale.currency(rev, grouping=True)) +
        "\n# Items Acquired: " + str(sold))   
    direct_total = sold
   

def lockRev(goal, droprate, lockkey=99.6):
    sold = 0
    rev = 0
    lockbox = 0
    win = 0
    loss = 0
    dol_lockkey = lockkey * gem_cost
    while sold < goal:
        lockbox += 1
        if random.uniform(0.000, 100.000) < droprate:
            sold += 1
            win += 1
        else:
            loss += 1
        rev = lockbox * dol_lockkey

    print("Per Item Cost: " + str(locale.currency((rev/sold), grouping=True)) +
          "\nLock Boxes Purchased: " + str(lockbox) +
          "\nTotal Lockbox Purchase Revenue: " + str(locale.currency(rev, grouping=True)) +
          "\n# Items Acquired: " + str(sold) +
          "\n# Losses: " + str(loss))

revCalc(salesgoal)
print("\n")
print("Validation Direct Total Sold: " + str(direct_total)) 
lockRev(salesgoal,lb_droprate)


# 1 pack - 125
# 5 pack cost per - 90
# 25 pack cost per - 84

def house_adv(win,loss,lockkey):
    total = win + loss
    winProb = win / total
    lossProb = loss / total
    monies = lockkey * total 
    houseedge = (winProb - lossProb) * -1
    profit = houseedge * monies
    print(winProb)
    print(lossProb)
    print(total)
    print(monies)
    print(houseedge)
    print(locale.currency(profit))


    # House advantage is probability of win added to probability of losing and multiplied by total customer spend
    # so Roulette - (18/38 X 1) + (20/30 X -1) = -5.26%, if betting a dollar the house edge is -5.26 * bet * # of rounds = $0.53

#def probablility(): 
    # event category divided by total space

#def stddev(): 
    # Take the avlues and find the mean, then substract the mean from the individual values, then square the result. Divide by sample size - 1


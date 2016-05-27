# Noah Cote
# Population Simulator
# main.py

from random import *
from math import *

def main():
    print("Population Simulator")
    print("created by Noah Cote")
    print()
    print("This program will demonstrate the changes a population of people will face,")
    print("based upon chance and location.")
    print()
    print("You will be given the choice of selecting location, starting population, growth rate, and time frame.")
    print("Along with being given a choice you may random all the options.")
    check = "y"
    while check[0] == "y" or check[0] == "Y": # While loop to run multiple times
        loc, sp, gr, tf = basicdata() # gets data
        routing(loc, sp, gr, tf) # hands off data to routing
        check = input("Would you like to run it again(Yes/No)?")

########### BASIC INFO BELOW #################


def basicdata():
    loc = basicloc()  # data is organized in functions for error handling
    print("Location Saved.")
    print()
    sp = basicpop()
    print("Starting Population: ", sp)
    print("Starting Population Saved.")
    print()
    gr = basicgrowthrate()
    print("Growth Rate Option Saved.")
    print()
    tf = 100
    print("The time frame is set to 100 years.")
    print()
    print("Options Completed.")
    return loc, sp, gr, tf


def basicloc():  # Location Options
    print("{0:10}".format("Location Options:"))
    print("{0:10}{1:10}".format("1.", "Coastal"))
    print("{0:10}{1:10}".format("2.", "Mountains"))
    print("{0:10}{1:10}".format("3.", "Plains"))
    print("{0:10}{1:10}".format("4.", "Islands"))
    print("{0:10}{1:10}".format("5.", "Random"))
    loc = input("Select which location(1-5): ")  # uses a plain input for better error handling
    if loc == "1" or loc == "2" or loc == "3" or loc == "4" or loc == "5":  # if it is those as a sting int them
        loc = int(loc)
        if loc >= 1 and loc < 5:  # checks if it is okay, not <= to 5 because that is seperate
            return loc
        elif loc == 5:  # has random
            loc = randrange(1, 4)
            return loc
        else:
            print("The number you entered is invalid, a random location will be decided for you.")
            # ^if it is none do this
            loc = randrange(1, 4)
            return loc
    elif loc.lower() == "bill":  # easter egg
        print("Nice try Mr. F, but its going to work.")
        print("Assignment will be random.")
        loc = randrange(1, 4)
        return loc
    else:  # if anything else possibly goes wrong
        print("The number you entered is invalid, a random location will be decided for you.")
        loc = randrange(1, 4)
        return loc


def basicpop():  # Starting Population
    print("{0:10}".format("Starting Population Options:"))
    print("{0:10}{1:10}".format("1.", "Custom Amount"))
    print("{0:10}{1:10}".format("2.", "Random"))
    tsp = input("Select which option(1-2): ")
    if tsp == "1" or tsp == "2":  # same error handling as above
        tsp = int(tsp)
        if tsp == 1:
            sp = eval(input("Enter custom population amount: "))
            sp = int(sp)
            if sp > 0:
                return sp
            else:
                print("The number you entered is not valid, it will default to random.")
                sp = randrange(2, 501)
                return sp
        elif tsp == 2:
            sp = randrange(2, 501)
            return sp
        else:
            print("You entered something wrong so it will default to random.")
            sp = randrange(2, 501)
            return sp
    elif tsp.lower() == "bill":
        print("Nice try Mr. F, but its going to work.")
        print("Assignment will be random.")
        sp = randrange(2, 501)
        return sp
    else:
        print("You entered something wrong so it will default to random.")
        sp = randrange(2, 501)
        return sp


def basicgrowthrate():  # Growth Rate
    print("{0:10}".format("Growth Rate Options:"))
    print("{0:10}{1:10}".format("1.", "Decelerated"))
    print("{0:10}{1:10}".format("2.", "Normal"))
    print("{0:10}{1:10}".format("3.", "Accelerated"))
    ogr = input("Select which option(1-3): ")  # same error handling as above
    if ogr == "1" or ogr == "2" or ogr == "3":
        ogr = int(ogr)
        if ogr == 1:
            gr = .005  # decelerated
            return gr
        elif ogr == 2:
            gr = .0113  # normal based off human growth rate
            return gr
        elif ogr == 3:
            gr = .020  # accelerated based off peak human growth rate
            return gr
        else:
            print("You entered something wrong so it will default to normal.")
            gr = .0113  # defaults to normal
            return gr
    elif ogr.lower == "bill":
        print("Nice try Mr. F, but its going to work.")
        gr = .0113
        return gr
    else:
        print("You entered something wrong so it will default to normal.")
        gr = .0113
        return gr

########### BASIC INFO ABOVE #################


def routing(loc, sp, gr, tf):
    stopper = True  # to start
    cy = 1  # for set first year
    print("{0:<10}{1:<10}".format("Year:", cy))
    print("{0:<10}{1:<10}".format("Population:", sp))
    print()
    while stopper == True:  # lets it up to run to last year
        cy, endreason, timemod, timemodreason = timeprogression(cy)
        locreason, locmod = location(loc)
        sp = sp + timemod + locmod  # adds modifiers and population
        sp = growthrate(gr, sp, cy) # finds the new population
        sp = round(sp) # Rounds because you can't have half a person
        presentation(cy, timemod, timemodreason, locreason, locmod, sp) #sends it out to be printed
        if cy == tf: # ending messages
            print("That was 100 years. Your Populations results are above.")
            stopper = False # stopper set to false to get out of loop
        elif endreason == "Your population has fallen into peril, this is the end.":
            print("Your population made it", cy, "years.")
            stopper = False
        elif sp <= 0:
            print("Your population died out.")
            stopper = False
        else:
            stopper = True # set true to continue


def presentation(cy, timemod, timemodreason, locreason, locmod, sp):
    print("{0:<15}{1:^20}".format("Year:", cy))
    print("{0:<15}{1:^20}{2:<5}".format("Time Modifiers:", timemod, timemodreason))
    print("{0:<10}{1:^11}{2:<10}".format("Location Modifiers:", locmod, locreason))
    print("{0:<15}{1:^20}".format("Population:", sp))
    print("*************************************************")

def timeprogression(cy): #keeps track of time
        cy = cy + 1 # adds the year
        ereason = randomend(cy) #to see if pop will end
        mod, reason = randomtime() #times advancement modifier
        return cy, ereason, mod, reason #sends data to routing to be printed and used


def location(loc):
    if loc == 1:  # coastal
        crgood = ["Fishing was good this year!", "New fishing tech!", "More beach real estate!", "House Boats welcome!",
                  "Permanent Beachgoers!"]
        crbad = ["Fish Shortage.", "Tsunami.", "Earthquake.", "Hurricane.", "Volcano."]
        goodbad = randrange(0, 1000) #set to a higher range because 50% chance was not random enough
        if goodbad >= 500: #good if above or equal to 500
            greason = randrange(0, 4) #randoms to see whaat the reason is
            reason = crgood[greason] #takes the random and ties it to the list
            mod = randrange(0, 100) #the bonus pop from the modifier
            return reason, mod
        else: #if its lower than 500 its bad
            greason = randrange(0, 4)
            reason = crbad[greason]
            mod = randrange(-100, 0) #negitive throughout
            return reason, mod

    elif loc == 2:  # Mountians
        mrgood = ["Gold Rush!", "Silver Rush!", "More Ski Resort real estate!", "Mountain Men welcome!",
                  "Hunting was good this year!"]
        mrbad = ["Mud Slide.", "Bad ski year.", "Earthquake.", "Cold is the silent killer.", "Wildfire."]
        goodbad = randrange(0, 1000)
        if goodbad >= 500:
            greason = randrange(0, 4)
            reason = mrgood[greason]
            mod = randrange(0, 100)
            return reason, mod
        else:
            greason = randrange(0, 4)
            reason = mrbad[greason]
            mod = randrange(-100, 0)
            return reason, mod

    elif loc == 3:  # Plains
        prgood = ["Farming was good this year!", "New farming tech!", "More real estate development!!",
                  "Ranchers welcome!", "Cattle Boom!"]
        prbad = ["Flooding", "Blight.", "Crop Shortages.", "Tornado.", "Over farming."]
        goodbad = randrange(0, 1000)
        if goodbad >= 500:
            greason = randrange(0, 4)
            reason = prgood[greason]
            mod = randrange(0, 100)
            return reason, mod
        else:
            greason = randrange(0, 4)
            reason = prbad[greason]
            mod = randrange(-100, 0)
            return reason, mod

    elif loc == 4:  # islands
        irgood = ["Fishing was good this year!", "New fishing tech!", "More beach real estate!", "House Boats welcome!",
                  "Permanent Beachgoers!"]
        irbad = ["Fish Shortage.", "Tsunami.", "Earthquake.", "Hurricane.", "Volcano."]
        goodbad = randrange(0, 1000)
        if goodbad >= 500:
            greason = randrange(0, 4)
            reason = irgood[greason]
            mod = randrange(0, 100)
            return reason, mod
        else:
            greason = randrange(0, 4)
            reason = irbad[greason]
            mod = randrange(-100, 0)
            return reason, mod

    else:
        print("Something went wrong.(Location)")


def growthrate(gr, currentpop, cy):
    if cy == 1: #adds a person and a half if its the first year.
        currentpop = currentpop + 1.5
        return currentpop
    else:
        goodbad = randrange(0, 1000) #same random chance as above for wheather the pop will grow or shrink
        if goodbad >= 500:
            base = currentpop
            base = (base*gr)+base
            return base
        else:
            base = currentpop
            base = (base * -gr)+base
            base = abs(base)
            return base


def randomtime():  # random function for time
    reasonsgood=["A better way of farming has been discovered!", "People have begun to immigrate!",
                 "New land development is underway!", "Baby Boom!", "Golden Year!"]
    reasonsbad=["Food Shortages.", "Mass emigration.", "Lack of housing.", "Economic Recession.", "Illness."]
    goodbad = randrange(0,1000)  # decides whether bad or good modifier
    if goodbad >= 500:  # if good
        goodreason = randrange(0, 4)
        goodreason = reasonsgood[goodreason]
        mod =  randrange(0, 100)
        return mod, goodreason
    else:  # if bad
        badreason = randrange(0, 4)
        badreason = reasonsbad[badreason]
        mod = randrange(-100, 0)
        return mod, badreason


def randomend(cy): #to see if the pop will die out early
        if cy < 20:
            cy = cy * 10000000000 #finds upper end of chance
            first = randrange(0, cy)
            second = randrange(0, cy)
            if first == second: #if the two equal then the pop will die out. As time goes on the chances increase
                endreason = "Your population has fallen into peril, this is the end."
                return endreason
            else:
                endreason = "Your population is safe for now."
                return endreason
        elif cy >= 20 and cy < 40:
            cy = cy * 100000000
            first = randrange(0, cy)
            second = randrange(0, cy)
            if first == second:
                endreason = "Your population has fallen into peril, this is the end."
                return endreason
            else:
                endreason = "Your population is safe for now."
                return endreason
        elif cy >= 40 and cy < 60:
            cy = cy*1000000
            first = randrange(0, cy)
            second = randrange(0, cy)
            if first == second:
                endreason = "Your population has fallen into peril, this is the end."
                return endreason
            else:
                endreason = "Your population is safe for now."
                return endreason
        elif cy >= 60 and cy < 80:
            cy = cy*10000
            first = randrange(0, cy)
            second = randrange(0, cy)
            if first == second:
                endreason = "Your population has fallen into peril, this is the end."
                return endreason
            else:
                endreason = "Your population is safe for now."
                return endreason
        elif cy >= 80 and cy <= 99:
            cy = cy*100
            first = randrange(0, cy)
            second = randrange(0, cy)
            if first == second:
                endreason = "Your population has fallen into peril, this is the end."
                return endreason
            else:
                endreason = "Your population is safe for now."
                return endreason
        elif cy == 100: #if it reaches the end its dafe
            endreason = "Your population is safe forever!"
            return endreason

        else:
            endreason = "Something is very wrong here.(randomtime,end)"
            return endreason
main()

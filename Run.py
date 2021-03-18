# Run.py
# ITP 115, Spring 2020 Final project
# Run this file in order to start the restaurant simulation program

import datetime
import time

from Menu import Menu
from Waiter import Waiter
from RestaurantHelper import RestaurantHelper


def main():
    RESTAURANT_NAME = "FINAL SUFFERINGS "
    restaurantTime = datetime.datetime(2020, 5, 1, 5, 0)

    # Create the Menu object
    menu = Menu("menu.csv")
    # create the waiter object using the Menu object we just created
    waiter = Waiter(menu)
    print("Welcome to " + RESTAURANT_NAME + "!")
    print(RESTAURANT_NAME + " is now open for dinner.\n")

    for i in range(21):
        print("\n~~~ It is currently", restaurantTime.strftime("%H:%M PM"), "~~~")
        restaurantTime += datetime.timedelta(minutes=15)

        possibleDiner = RestaurantHelper.randomDinerGenerator()
        if possibleDiner is not None:
             print("\n" + possibleDiner.getterName() + " welcome, please be seated!")
            # we have a diner to add to the waiter's list of diners
             waiter.addDiner(possibleDiner)   # Make sure to keep this line inside the if-statement on line 34!
        waiter.changeStatus()  # Keep this line outside of the if-statement
        time.sleep(2)

    print("\n~~~ ", RESTAURANT_NAME, "is now closed. ~~~")
    # After the restaurant is closed, progress any diners until everyone has left
    while waiter.getNumDiners():
        print("\n~~~ It is currently", restaurantTime.strftime("%H:%M PM"), "~~~")
        restaurantTime += datetime.timedelta(minutes=15)
        waiter.changeStatus()
        time.sleep(2)

    print("Goodbye!")

main()

#DOOOOONE
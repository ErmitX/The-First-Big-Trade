import time
import random

def type_text(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.008)
    print()

def money(value):
    return "${:,.2f}".format(value)

print("=" * 65)
print("                      THE FIRST BIG TRADE")
print("=" * 65)
print()

cash = 1250.00
confidence = 60
risk = 0

type_text("Eddie has NZT.")
type_text("He has knowledge.")
type_text("But knowledge means nothing if he cannot turn it into money.")
print()

type_text("He opens his laptop.")
type_text("Stock charts fill the screen.")
print()

type_text("Before NZT, Eddie saw random numbers.")
type_text("Now he sees patterns.")
print()

print("Starting capital:", money(cash))
print()

type_text("Three companies catch his attention.")
print()

print("1. A technology company")
print("2. A pharmaceutical company")
print("3. A financial company")

while True:
    choice = input("\nChoose an investment: ")

    if choice in ["1", "2", "3"]:
        break

    print("Choose 1, 2, or 3.")

print()

if choice == "1":
    type_text("Eddie studies the technology company.")
    type_text("The numbers tell a story.")
    risk = 25
    multiplier = 2.8

elif choice == "2":
    type_text("Eddie studies the pharmaceutical company.")
    type_text("The company is waiting for approval.")
    risk = 45
    multiplier = 4.2

else:
    type_text("Eddie studies the financial company.")
    type_text("The market has underestimated it.")
    risk = 35
    multiplier = 3.4

print()
type_text("Eddie doesn't hesitate.")
type_text("He puts most of his money into the trade.")

investment = cash * 0.85
cash -= investment

print()
print("Investment:", money(investment))
print("Remaining cash:", money(cash))
print("Risk level:", risk, "%")
pause = input("\nPress ENTER to watch the market...")

print()

for hour in range(1, 7):
    movement = random.randint(-3, 8)

    if movement < 0:
        type_text("Market movement: " + str(movement) + "%")
    else:
        type_text("Market movement: +" + str(movement) + "%")

    time.sleep(0.5)

print()
type_text("Eddie refreshes the page.")
time.sleep(1)

result = random.randint(1, 100)

if result > risk:
    profit = investment * (multiplier - 1)
    cash += investment + profit

    type_text("The trade worked.")
    type_text("Eddie just made a fortune.")

    print()
    print("Profit:", money(profit))
    print("Total wealth:", money(cash))

else:
    loss = investment * 0.65
    cash += investment - loss

    type_text("The market turns against him.")
    type_text("NZT couldn't predict everything.")

    print()
    print("Loss:", money(loss))
    print("Total wealth:", money(cash))

print()
type_text("Eddie closes the laptop.")
type_text("This was only the beginning.")

if cash > 5000:
    print()
    print("ENDING: THE TRADER")
else:
    print()
    print("ENDING: THE LESSON")
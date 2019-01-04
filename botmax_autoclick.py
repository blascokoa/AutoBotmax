import time
import pyautogui
import random

"""
AutoClick Bot for automate trading on exchanges where there isn't available an api to trade
Use this bot don't ensure you make profits. 
Credits of the bot to @dblama
"""


def main():
    pyautogui.PAUSE = random.uniform(0.2, 0.5)
    pyautogui.FAILSAFE = True

    print("------------------- AUTOBOTMAX -------------------")
    print("-------------- Developed by @dblama --------------")
    time.sleep(1)
    loops = int(input("How many loops do you want to do?:"))
    print(f"Ok, AutoBotMax will run {loops} loops of buy-sell")
    time.sleep(0.2)
    print("Now we will configurate the coordinates of the buttons...")
    time.sleep(1)

    # BUY Options:
    input("Put the cursor on the FIRST SELL ORDER ON THE BOOK and press ENTER")
    buy_price_x, buy_price_y = pyautogui.position()
    print(f"Coordinate recorded: {buy_price_x},{buy_price_y}")
    input("Put the cursor on the BUY ORDER SIZE and press ENTER")
    buy_size_x, buy_size_y = pyautogui.position()
    print(f"Coordinate recorded: {buy_size_x},{buy_size_y}")
    input("Put the cursor on the BUY BUTTON and press ENTER")
    buy_button_x, buy_button_y = pyautogui.position()
    print(f"Coordinate recorded: {buy_button_x},{buy_button_y}")

    # SELL Options
    input("Put the cursor on the BOOK ORDER SELL and press ENTER")
    sell_price_x, sell_price_y = pyautogui.position()
    print(f"Coordinate recorded: {sell_price_x},{sell_price_y}")
    input("Put the cursor on the SELL ORDER SIZE and press ENTER")
    sell_size_x, sell_size_y = pyautogui.position()
    print(f"Coordinate recorded: {sell_size_x},{sell_size_y}")
    input("Put the cursor on the SELL BUTTON and press ENTER")
    sell_button_x, sell_button_y = pyautogui.position()
    print(f"Coordinate recorded: {sell_button_x},{sell_button_y}")
    secs_between_clicks = random.uniform(0.1, 0.5)
    secs_between_clicks = 0
    clicks = 1

    for i in range(loops):
        # Buy serie

        pyautogui.click(x=buy_price_x, y=buy_price_y, clicks=clicks, interval=secs_between_clicks, button='left')
        time.sleep(random.uniform(0.2, 0.5))
        pyautogui.click(x=buy_size_x, y=buy_size_y, clicks=clicks, interval=secs_between_clicks, button='left')
        time.sleep(random.uniform(0.2, 0.5))
        pyautogui.click(x=buy_button_x, y=buy_button_y, clicks=clicks, interval=secs_between_clicks, button='left')
        # Sell serie
        time.sleep(random.uniform(0.2, 0.5))
        pyautogui.click(x=sell_price_x, y=sell_price_y, clicks=clicks, interval=secs_between_clicks, button='left')
        time.sleep(random.uniform(0.2, 0.5))
        pyautogui.click(x=sell_size_x, y=sell_size_y, clicks=clicks, interval=secs_between_clicks, button='left')
        time.sleep(random.uniform(0.2, 0.5))
        pyautogui.click(x=sell_button_x, y=sell_button_y, clicks=clicks, interval=secs_between_clicks, button='left')
        time.sleep(random.uniform(0.2, 0.5))


if __name__ == '__main__':
    main()

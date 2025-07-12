import pywhatkit
import time
import pyautogui  # optional: for pressing Enter if message doesn't send automatically
from get_tesla_stock import get_stock # Getting the stock info
from get_tesla_news import get_tesla_news_rss

stock_info = get_stock()
news_info = get_tesla_news_rss()
# Send message instantly
pywhatkit.sendwhatmsg_instantly("+919354352191", f"Stock : {stock_info}/n{news_info}", wait_time=10, tab_close=True)

# Wait and press Enter (optional — sometimes needed to trigger send)
time.sleep(10)
import pyautogui
pyautogui.press("enter")

""""

# You want to check whether a web page loads within 3 seconds (performance test condition).
#
# load_time = 5.6
# ⚠️ Page load too slow: 5.6 seconds

load_time = float(input("Enter API response in sec: "))

# Performance threshold (3 seconds)
if load_time < 0:
    print("Enter a valid response time")
elif load_time > 30:
    print("Very Poor Performance")
else:
    if load_time <= 3:
        print(f"✅ Page loaded successfully in {load_time} seconds")
    else:
        print(f"⚠️ Page Timeout")

"""



# Question 3 :
#
# Simulate a page loading check using a while loop.
# If page_loaded becomes True within 5 seconds, print success; else timeout.
#
# Hint: Use a counter (like wait_time) and break c
import time
import random

wait_time = 0
page_loaded = False


def api_response():
    return random.choice([False, True])


while wait_time < 5:
    page_loaded = api_response()
    if page_loaded:
        print(f"✅ Page loaded successfully in {wait_time + 1} seconds.")
        break
    else:
        print(f"⏳ Checking... (second {wait_time + 1})")
        time.sleep(1)  # wait for 1 second
        wait_time += 1

if not page_loaded:
    print("❌ Timeout! Page failed to load within 5 seconds.")
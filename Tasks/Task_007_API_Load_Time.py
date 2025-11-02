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
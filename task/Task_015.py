#Simulate a page loading check using a while loop.
#If page_loaded becomes True within 5 seconds, print success; else timeout.
import time

#Hint: Use a counter (like wait_time) and break condition.

wait_time = 0

while wait_time < 5:
    print(f"Waiting for page loads,({wait_time+1} sec)")
    time.sleep(1)
    wait_time+= 1

    if wait_time == 3:
        print("Success")
        break
    else:
        print("⏰ Timeout! Page did not load within 5 seconds.")

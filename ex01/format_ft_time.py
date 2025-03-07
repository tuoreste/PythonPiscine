import time
import datetime

s = time.time()
scientific = "{:2e}".format(s)
print("Seconds since January 1, 1970: " + f"{s:,}" + " or " + scientific + " in scientific notation")

today = datetime.datetime.now()
print(today.strftime("%b %d, %Y"))

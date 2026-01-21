import time
import datetime

seconds = time.time()
now = datetime.datetime.now()

print(f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation")
# ,.4f = comma thousands + 4 decimals
# .2e  = scientific notation with 2 decimals

print(now.strftime("%b %d %Y"))
# strftime = string from time
#   It takes a time/date object and turns it into a formatted string.
# %b = brief month (Oct, Dec…)
# %d = day with zero (01–31)
# %Y = full year (2025)
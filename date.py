1.
from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Subtract five days from the current date
new_date = current_date - timedelta(days=5)

# Print the new date
print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Date 5 days ago:", new_date.strftime("%Y-%m-%d"))

2.
from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Calculate the dates for yesterday and tomorrow
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)

# Print the results
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", current_date.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

3.
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Drop microseconds by replacing with zero
current_datetime = current_datetime.replace(microsecond=0)

# Print the datetime without microseconds
print("Datetime without microseconds:", current_datetime)
4.
from datetime import datetime

# Define two dates
date1 = datetime(2023, 10, 15, 12, 0, 0)
date2 = datetime(2023, 10, 20, 15, 30, 0)

# Calculate the time difference in seconds
time_difference = (date2 - date1).total_seconds()

print(f"The difference between the two dates is {time_difference} seconds.")


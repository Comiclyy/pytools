import datetime
import pytz

# Set the timezone
tz = pytz.timezone('US/Eastern')

# Get the current time with the timezone set
current_time = datetime.datetime.now(tz)

# Format the time and date outputs
formatted_time = current_time.strftime('%-I:%M %p')
formatted_date = current_time.strftime('%Y-%m-%d')

# Print the formatted time and date with prefixes
print('TIME:', formatted_time)
print('DATE:', formatted_date)

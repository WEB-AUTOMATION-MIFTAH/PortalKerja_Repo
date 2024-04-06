from datetime import datetime, timedelta

# Get the current local time
current_time = datetime.now()

# Add 7 hours to the current time to convert it to UTC+7
utc_plus_7_time = current_time + timedelta(hours=7)

# Format the time as required (YYYY-MM-DDTHH:MM:SSZ)
formatted_time = utc_plus_7_time.strftime('%Y-%m-%dT%H:%M:%SZ')

# Read the original report file
with open('report_template.html', 'r') as file:
    report_content = file.read()

# Replace the placeholder with the formatted time
modified_report = report_content.replace('2024-01-28T12:00:00Z', formatted_time)

# Write the modified report to a new file
with open('report_action.html', 'w') as file:
    file.write(modified_report)

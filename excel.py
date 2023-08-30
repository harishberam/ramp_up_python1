import pandas as pd

# Read Excel file
data = pd.read_excel("emp_wfh_wfo.xlsx")

# Clean column names by stripping whitespace
data.columns = data.columns.str.strip()

# Calculate WFH and WFO counts for today (Aug 28, 2023)
wfh_count_today = (data['aug28,2023'] == 'WFH').sum()
wfo_count_today = (data['aug28,2023'] == 'WFO').sum()
print(wfo_count_today)
print(wfh_count_today)

# Calculate WFH and WFO counts for the previous 5 days (Aug 23 - Aug 28)
previous_days_columns = ['aug23,2023','aug24,2023','aug25,2023','aug26,2023','aug27,2023']
wfh_count_previous_days = data[previous_days_columns].apply(lambda col: (col == 'WFH').sum()).sum()
wfo_count_previous_days = data[previous_days_columns].apply(lambda col: (col == 'WFO').sum()).sum()

# Find employee IDs who haven't filled attendance in all today and previous 5 days
missing_all_days = data[data[['aug23,2023','aug24,2023','aug25,2023','aug26,2023','aug27,2023','aug28,2023']].isnull()]
missing_all_days = data[missing_all_days.all(axis=1)]['emp id']
missing = missing_all_days.tolist()

# Print results
print("WFH Count on Current Date:", wfh_count_today)
print("WFO Count on Current Date:", wfo_count_today)
print("WFH Count for Previous 5 Days:", wfh_count_previous_days)
print("WFO Count for Previous 5 Days:", wfo_count_previous_days)
print("Employees Missed All Days:", missing)


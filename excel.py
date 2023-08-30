import pandas as pd
import datetime

def current_date():
    return datetime.datetime.now().strftime("%d%b%Y")
print(current_date())
print("current_date: ",type(current_date()),current_date())
df=pd.read_csv(r"Excel_details.csv",sep="\t")
# df=pd.read_excel(r"C:\Users\VenkataHarish B-3270\Downloads\Emp_details.xlsx")
columns=list(df.columns)
split_column=columns[0].split(",")

values=df.values.tolist()
print(len(values))
list_of_values=[]
for value in values:
    list_of_values.append(value[0].split(","))

def how_many_marked_wfo_and_wfh(data):
    wfo_and_wfh_count=0
    for i in range(len(values)):
        current_day=current_date()

        if current_day in data:
            current_day_index=data.index(current_day)


            if list_of_values[i][current_day_index]=="WFH" or list_of_values[i][current_day_index]=="WFO":

                wfo_and_wfh_count = wfo_and_wfh_count + 1
    return wfo_and_wfh_count



print("how_many_marked_wfo_and_wfh: ",how_many_marked_wfo_and_wfh(split_column))
def marked_data_from_previous_5_days():
    index_of_current_date=split_column.index(current_date())
    previous_5_days_marked_wfo_and_wfh=0
    for value in list_of_values:
        len_of_list=[col for col in value[1:index_of_current_date+1:] if col=="WFH" or col=="WFO"]
        previous_5_days_marked_wfo_and_wfh +=len(len_of_list)
    return previous_5_days_marked_wfo_and_wfh
print("working_employee_previous_5days: ",marked_data_from_previous_5_days())
def get_employee_who_not_filled_on_current_day():
    index_of_current_date=split_column.index(current_date())
    employess=[]
    current_day_index=split_column.index(current_date())
    for value in list_of_values:

        data=[val[current_day_index] for val in list_of_values if current_date() in split_column]
        if data[0] =="":
            employess.append(value[0])

    return employess

print("marked_data_from_previous_5days: ",marked_data_from_previous_5_days())

print("employee_not_filled_on_current_day: ",get_employee_who_not_filled_on_current_day())

def get_employee_who_not_filled_on_current_day():
    index_of_current_date = split_column.index(current_date())
    employess = []

    for value in list_of_values:
        if value[index_of_current_date] == '""': employess.append(value[0])
    return f"details of employess who are not filled attendance given in list format {employess}"


# Print the list of employees who have not filled in their status for the current day

print(get_employee_who_not_filled_on_current_day())
def employee_who_not_filled_on_previous_5_days():
    index_of_current_date = split_column.index(current_date())

    for value in list_of_values:
        emp_list=[value[0] for col in value[index_of_current_date-1:index_of_current_date-6:-1] if col=='""']
        print(emp_list)
employee_who_not_filled_on_previous_5_days()


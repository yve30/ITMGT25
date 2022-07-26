import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

data_path = './transaction-data-adhoc-analysis.json'
transactional_data = pd.read_json(data_path)
transactional_data

transactional_data['transaction_date'] = pd.to_datetime(transactional_data['transaction_date'], format="%Y/%m/%d")
transactional_data['month'] = pd.DatetimeIndex(transactional_data['transaction_date']).month

transactional_data

## 1
def quantity(name):
    product_name = name[name.index(",",name.index(",")+1):]
    return product_name

def item(name):
    product_name = name[name.index(",")+1:name.index(",",name.index(",")+1)]
    return product_name

transactional_data['transaction_items'] = transactional_data['transaction_items'].str.split(';')
transactional_data = transactional_data.explode('transaction_items').reset_index(drop=True)

transactional_data['total_number'] = transactional_data['transaction_items'].apply(quantity).str.replace('[^0-9]','', regex = True)
transactional_data['transaction_items'] = transactional_data['transaction_items'].apply(item)
transactional_data['total_number'] = transactional_data['total_number'].astype(int)

order_quantity = transactional_data.groupby([transactional_data.transaction_date.dt.month,'transaction_items'])['total_number'].sum().unstack(level=0)

''' [1.1] Breakdown of the count of each item sold per month '''
order_quantity.columns = ['January', 'February', 'March', 'April', 'May', 'June']
display(order_quantity)

''' [1.2] Breakdown of the total sale value per item per month '''
prices = [1299, 1500, 150, 799, 1990, 199, 500]
order_quantity["sale_value"] = prices

for i in list(order_quantity.keys())[:-1]:
        order_quantity[i] = order_quantity['sale_value']*order_quantity[i]
order_quantity


## [2] Repeater, Inactive, Engaged

status_df = transactional_data.pivot_table('total_number', ['name'], "month", aggfunc="count", fill_value = 0)

status_df["January"] = status_df[1].astype(int)
status_df["February"] = status_df[2].astype(int)
status_df["March"] = status_df[3].astype(int)
status_df["April"] = status_df[4].astype(int)
status_df["May"] = status_df[5].astype(int)
status_df["June"] = status_df[6].astype(int)

status_df

def month_bracket_1(January):
    if January > 0:
        status1 = "First Purchase"
    else:
        status1 = "No Transaction"
    return status1

def month_bracket_2(January, February):
    if January > 0 and February == 0:
        status2 = "Inactive"
    elif January > 0 and February > 0:
        status2 = "Repeater"
    elif January == 0 and February > 0:
        status2 = "First Purchase"
    elif January == 0 and February == 0:
        status2 = "No Transaction"
    else:
        status2 = "Engaged"
    return status2
        
def month_bracket_3(January, February, March):
    if January == 0 and February == 0 and March == 0:
        status3 = "No Transaction"
    elif January == 0 and February > 0 and March > 0:
        status3 = "Repeater"
    elif January > 0 and February == 0 and March == 0:
        status3 = "Inactive"
    elif January == 0 and February > 0 and March == 0:
        status3 = "Inactive"
    elif January > 0 and February > 0 and March == 0:
        status3 = "Inactive"
    else: 
        status3 = "Engaged"
    return status3

def month_bracket_4(January, February, March, April):
    if January == 0 and February == 0 and March == 0 and April == 0:
        status4 = "No Transaction"
        
    elif January == 0 and February > 0 and March > 0 and April > 0:
        status4 = "Repeater"
    elif January == 0 and February == 0 and March > 0 and April > 0:
        status4 = "Repeater"
    elif January > 0 and February == 0 and March > 0 and April > 0:
        status4 = "Repeater"
        
    elif January > 0 and February == 0 and March == 0 and April == 0:
        status4 = "Inactive"
    elif January == 0 and February > 0 and March == 0 and April == 0:
        status4 = "Inactive"
    elif January == 0 and February == 0 and March > 0 and April == 0:
        status4 = "Inactive"
    elif January > 0 and February > 0 and March == 0 and April == 0:
        status4 = "Inactive"
    elif January > 0 and February == 0 and March > 0 and April == 0:
        status4 = "Inactive"
    elif January == 0 and February > 0 and March > 0 and April == 0:
        status4 = "Inactive"
    elif January > 0 and February > 0 and March > 0 and April == 0:
        status4 = "Inactive"
        
    else:
        status4 = "Engaged"
    return status4

def month_bracket_5(January, February, March, April, May):
    if January == 0 and February == 0 and March == 0 and April == 0 and May == 0: 
        status5 = "No Transaction"
        
    elif January > 0 and February == 0 and March == 0 and April > 0 and May > 0:
        status5 = "Repeater"
    elif January == 0 and February > 0 and March == 0 and April > 0 and May > 0:
        status5 = "Repeater"
    elif January == 0 and February == 0 and March > 0 and April > 0 and May > 0:
        status5 = "Repeater"
    elif January > 0 and February > 0 and March == 0 and April > 0 and May > 0:
        status5 = "Repeater"
    elif January > 0 and February == 0 and March > 0 and April > 0 and May > 0:
        status5 = "Repeater"
    elif January == 0 and February > 0 and March > 0 and April > 0 and May > 0:
        status5 = "Repeater"
    elif January == 0 and February == 0 and March == 0 and April > 0 and May > 0:
        status5 = "Repeater"
        
    elif January > 0 and February == 0 and March == 0 and April == 0 and May == 0:
        status5  = "Inactive"
    elif January == 0 and February > 0 and March == 0 and April == 0 and May == 0:
        status5 = "Inactive"
    elif January == 0 and February == 0 and March > 0 and April == 0 and May == 0:
        status5 = "Inactive"
    elif January == 0 and February == 0 and March == 0 and April > 0 and May == 0:
        status5 = "Inactive"
    elif January > 0 and February > 0 and March == 0 and April == 0 and May == 0:
        status5 = "Inactive"    
    elif January > 0 and February == 0 and March > 0 and April == 0 and May == 0:
        status5 = "Inactive"
    elif January > 0 and February == 0 and March == 0 and April > 0 and May == 0:
        status5 = "Inactive"
    elif January == 0 and February > 0 and March > 0 and April == 0 and May == 0:
        status5 = "Inactive"
    elif January == 0 and February > 0 and March == 0 and April > 0 and May == 0:
        status5 = "Inactive"
    elif January == 0 and February == 0 and March > 0 and April > 0 and May == 0:
        status5 = "Inactive"
    elif January == 0 and February > 0 and March > 0 and April > 0 and May == 0:
        status5 = "Inactive"
    elif January > 0 and February == 0 and March > 0 and April > 0 and May == 0:
        status5 = "Inactive"
    elif January > 0 and February > 0 and March == 0 and April > 0 and May == 0:
        status5 = "Inactive"
    elif January > 0 and February > 0 and March > 0 and April == 0 and May == 0:
        status5 = "Inactive"   
    elif January > 0 and February > 0 and March > 0 and April > 0 and May == 0:
        status5 = "Inactive"
        
    else:
        status5 = "Engaged"
    return status5

def month_bracket_6(January, February, March, April, May,June):
    if  January == 0 and February == 0 and March == 0 and April == 0 and May == 0 and June == 0:
        status6 = "No Transaction"
        
    elif January > 0 and February > 0 and March > 0 and April == 0 and May > 0 and June > 0:
        status6 = "Repeater"
    elif January > 0 and February > 0 and March == 0 and April == 0 and May > 0 and June > 0:
        status6 = "Repeater"
    elif January > 0 and February == 0 and March == 0 and April == 0 and May > 0 and June > 0:
        status6 = "Repeater"
    elif January == 0 and February == 0 and March == 0 and April == 0 and May > 0 and June > 0:
        status6 = "Repeater"
    elif January == 0 and February == 0 and March == 0 and April > 0 and May > 0 and June > 0:
        status6 = "Repeater"
    elif January == 0 and February == 0 and March > 0 and April > 0 and May > 0 and June > 0:
        status6 = "Repeater"
    elif January == 0 and February > 0 and March > 0 and April > 0 and May > 0 and June > 0:
        status6 = "Repeater"
    elif January == 0 and February > 0 and March > 0 and April == 0 and May > 0 and June > 0:
        status6 = "Repeater"
    elif January > 0 and February == 0 and March == 0 and April > 0 and May > 0 and June > 0:
        status6 = "Repeater"
    elif January > 0 and February == 0 and March > 0 and April == 0 and May > 0 and June > 0:
        status6 = "Repeater"
    elif January == 0 and February > 0 and March == 0 and April > 0 and May > 0 and June > 0:
        status6 = "Repeater"
        
    elif January > 0 and February == 0 and March == 0 and April == 0 and May == 0 and June == 0:
        status6 = "Inactive"
    elif January == 0 and February > 0 and March == 0 and April == 0 and May == 0 and June == 0:
        status6 = "Inactive"
    elif January == 0 and February == 0 and March > 0 and April == 0 and May == 0 and June == 0:
        status6 = "Inactive"
    elif January == 0 and February == 0 and March == 0 and April > 0 and May == 0 and June == 0:
        status6 = "Inactive"
    elif January == 0 and February == 0 and March == 0 and April == 0 and May > 0 and June == 0:
        status6 = "Inactive"
    elif January > 0 and February > 0 and March == 0 and April == 0 and May == 0 and June == 0:
        status6 = "Inactive"
    elif January > 0 and February == 0 and March > 0 and April == 0 and May == 0 and June == 0:
        status6 = "Inactive"
    elif January > 0 and February == 0 and March == 0 and April > 0 and May == 0 and June == 0:
        status6 = "Inactive"
    elif January > 0 and February == 0 and March == 0 and April == 0 and May > 0 and June == 0:
        status6 = "Inactive"
    elif January == 0 and February > 0 and March > 0 and April == 0 and May == 0 and June == 0:
        status6 = "Inactive"
    elif January == 0 and February > 0 and March == 0 and April > 0 and May == 0 and June == 0:
        status6 = "Inactive"
    elif January == 0 and February > 0 and March == 0 and April == 0 and May > 0 and June == 0:
        status6 = "Inactive"
    elif January == 0 and February == 0 and March > 0 and April == 0 and May > 0 and June == 0:
        status6 = "Inactive"
    elif January == 0 and February == 0 and March > 0 and April > 0 and May == 0 and June == 0:
        status6 = "Inactive"
    elif January == 0 and February == 0 and March == 0 and April > 0 and May > 0 and June == 0:
        status6 = "Inactive"
    elif January > 0 and February > 0 and March > 0 and April == 0 and May == 0 and June == 0:
        status6 = "Inactive"
    elif January > 0 and February > 0 and March == 0 and April > 0 and May == 0 and June == 0:
        status6 = "Inactive"
    elif January > 0 and February > 0 and March == 0 and April == 0 and May > 0 and June == 0:
        status6 = "Inactive"
    elif January > 0 and February == 0 and March > 0 and April == 0 and May > 0 and June == 0:
        status6 = "Inactive"
    elif January > 0 and February == 0 and March == 0 and April > 0 and May > 0 and June == 0:
        status6 = "Inactive"
    elif January == 0 and February == 0 and March > 0 and April > 0 and May > 0 and June == 0:
        status6 = "Inactive"
    elif January == 0 and February > 0 and March == 0 and April > 0 and May > 0 and June == 0:
        status6 = "Inactive"
    elif January == 0 and February > 0 and March > 0 and April == 0 and May > 0 and June == 0:
        status6 = "Inactive"
    elif January == 0 and February > 0 and March > 0 and April > 0 and May == 0 and June == 0:
        status6 = "Inactive"
    elif January > 0 and February == 0 and March > 0 and April > 0 and May == 0 and June == 0:
        status6 = "Inactive"
    elif January > 0 and February > 0 and March > 0 and April > 0 and May == 0 and June == 0:
        status6 = "Inactive"
    elif January > 0 and February > 0 and March > 0 and April == 0 and May > 0 and June == 0:
        status6 = "Inactive"
    elif January > 0 and February > 0 and March == 0 and April > 0 and May > 0 and June == 0:
        status6 = "Inactive"
    elif January > 0 and February == 0 and March > 0 and April > 0 and May > 0 and June == 0:
        status6 = "Inactive"
    elif January == 0 and February > 0 and March > 0 and April > 0 and May > 0 and June == 0:
        status6 = "Inactive"
        
    else:
        status6 = "Engaged"
    return status6

status_df["January_Status"] = status_df.apply(lambda x: month_bracket_1(x["January"]), axis=1)
status_df["February_Status"] = status_df.apply(lambda x: month_bracket_2(x["January"], x["February"]), axis=1)
status_df["March_Status"] = status_df.apply(lambda x: month_bracket_3(x["January"], x["February"], x["March"]), axis=1)
status_df["April_Status"] = status_df.apply(lambda x: month_bracket_4(x["January"], x["February"], x["March"], x["April"]), axis=1)
status_df["May_Status"] = status_df.apply(lambda x: month_bracket_5(x["January"], x["February"], x["March"], x["April"], x["May"]), axis=1)
status_df["June_Status"] = status_df.apply(lambda x: month_bracket_6(x["January"], x["February"], x["March"], x["April"], x["May"],x["June"]), axis=1)

a = status_df.loc[:, "January_Status"].value_counts()
b = status_df.loc[:, "February_Status"].value_counts()
c = status_df.loc[:, "March_Status"].value_counts()
d = status_df.loc[:, "April_Status"].value_counts()
e = status_df.loc[:, "May_Status"].value_counts()
f = status_df.loc[:, "June_Status"].value_counts()

final_status = pd.concat([a, b, c, d, e, f], axis = 1).fillna(0)
final_status.astype(int)

columns = ["January_Status", "February_Status", "March_Status", "April_Status", "May_Status", "June_Status"]
index = ["Repeater", "Inactive", "Engaged"]

customer_status = pd.DataFrame(data = final_status, index = index, columns = columns)
customer_status.astype(int)

#[1.1] Bar Graph

order_quantity.transpose().reset_index(level=0).rename(columns={'index': 'Month'}).plot(x="Month", y=["Beef Chicharon","Gummy Vitamins","Gummy Worms", "Kimchi and Seaweed", "Nutrional Milk", "Orange Beans", "Yummy Vegetables"], kind="bar",figsize=(12,7))
plt.show()

#Line Graph that shows Lola Tamis' Monthly Sales

a = order_quantity['January'].sum()
b = order_quantity['February'].sum()
c = order_quantity['March'].sum()
d = order_quantity['April'].sum()
e = order_quantity['May'].sum()
f = order_quantity['June'].sum()

x = ("1", "2", "3", "4", "5", "6")
y = [a,b,c,d,e,f]
plt.plot(x, y, '#DDA0DD')
plt.ylabel("Total Sales in Millions")
plt.xlabel("Month")
plt.title("Lola Tamis Monthly Sales")
plt.show()
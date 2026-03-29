import pandas as pd
from database import get_connection
from queries import total_transactions_over_years
from queries import total_amount_over_years
from queries import top_10_states_transaction_amount
from queries import transaction_type_distribution
from queries import state_year_transaction_amount
from queries import top_device_brands
from queries import device_brand_percentage
from queries import device_brand_growth
from queries import top_brand_each_state
from queries import top_device_brands
from queries import lowest_insurance_states
from queries import top_states_insurance_value
from queries import insurance_quarterly_trend
from queries import top_districts_transaction_value
from queries import lowest_districts_transaction_value
from queries import transaction_quarterly_trend
from queries import avg_transaction_value_district
from queries import  high_transaction_activity_districts
from queries import highest_user_engagement_states
from queries import highest_user_pincode
from queries import  highest_district_user_engagement
from queries import user_growth_trend
from queries import lowest_user_engagement_states
from database import get_connection
from queries import  get_states,state_transaction_trend
from queries import get_districts, district_transaction_trend
from database import get_connection
 



def get_transactions_df():
    conn = get_connection()
    cursor = conn.cursor()

    data = total_transactions_over_years(cursor)

    df = pd.DataFrame(data, columns=["Year", "Transactions"])
    df["Transactions"] = df["Transactions"].astype(float)
    cursor.close()
    conn.close()

    return df



def get_amount_df():
    conn = get_connection()
    cursor = conn.cursor()

    data = total_amount_over_years(cursor)

    df = pd.DataFrame(data, columns=["Year", "Total_Amount"])
    df["Total_Amount"] = df["Total_Amount"].astype(float)

    cursor.close()
    conn.close()

    return df

def get_top_states_df():
    conn = get_connection()
    cursor = conn.cursor()

    data = top_10_states_transaction_amount(cursor)

    df = pd.DataFrame(data, columns=["State", "Total_Amount"])
    df["Total_Amount"] = df["Total_Amount"].astype(float)

    cursor.close()
    conn.close()

    return df

def get_transaction_type_df():
    conn = get_connection()
    cursor = conn.cursor()

    data = transaction_type_distribution(cursor)

    df = pd.DataFrame(data, columns=["Transaction_type", "Total_Transactions"])
    df["Total_Transactions"] = df["Total_Transactions"].astype(float)

    cursor.close()
    conn.close()

    return df

def get_state_trend_df():
    conn = get_connection()
    cursor = conn.cursor()

    data = state_year_transaction_amount(cursor)

    df = pd.DataFrame(data, columns=["State","Year","Total_Amount"])
    df["Total_Amount"] = df["Total_Amount"].astype(float)

    cursor.close()
    conn.close()

    return df

# case study:2
def get_device_brand_df():
    conn = get_connection()
    cursor = conn.cursor()

    data = top_device_brands(cursor)

    df = pd.DataFrame(data, columns=["Brand","Total_Users"])
    df["Total_Users"] = df["Total_Users"].astype(float)

    cursor.close()
    conn.close()

    return df

def get_device_percentage_df():
    conn = get_connection()
    cursor = conn.cursor()

    data = device_brand_percentage(cursor)

    df = pd.DataFrame(data, columns=["Brand","Avg_Percentage"])
    df["Avg_Percentage"] = df["Avg_Percentage"].astype(float)

    cursor.close()
    conn.close()

    return df

def get_device_growth_df():

    conn = get_connection()
    cursor = conn.cursor()

    data = device_brand_growth(cursor)

    df = pd.DataFrame(data, columns=[
        "Year",
        "Brand",
        "Total_Users"
    ])

    df["Year"] = df["Year"].astype(int)
    df["Total_Users"] = df["Total_Users"].astype(float)

    cursor.close()
    conn.close()

    return df

def get_top_brand_state_df():

    conn = get_connection()
    cursor = conn.cursor()

    data = top_brand_each_state(cursor)

    df = pd.DataFrame(data, columns=[
        "State",
        "Brand",
        "Total_Users"
    ])

    df["Total_Users"] = df["Total_Users"].astype(float)

    # Get top brand for each state
    df_top = (
        df.sort_values("Total_Users", ascending=False)
        .drop_duplicates("State")
    )

    df_top = df_top.sort_values("Total_Users", ascending=True)

    cursor.close()
    conn.close()

    return df_top


def get_top_device_brands_df():

    conn = get_connection()
    cursor = conn.cursor()

    data = top_device_brands(cursor)

    df = pd.DataFrame(data, columns=[
        "Brand",
        "Total_Users"
    ])

    df["Total_Users"] = df["Total_Users"].astype(float)

    cursor.close()
    conn.close()

    return df


from queries import insurance_growth_over_years

#case study:3
def get_insurance_growth_df():

    conn = get_connection()
    cursor = conn.cursor()

    data = insurance_growth_over_years(cursor)

    df = pd.DataFrame(data, columns=[
        "Year",
        "Total_Policies",
        "Total_Insurance_Value"
    ])

    df["Year"] = df["Year"].astype(int)
    df["Total_Policies"] = df["Total_Policies"].astype(float)
    df["Total_Insurance_Value"] = df["Total_Insurance_Value"].astype(float)

    cursor.close()
    conn.close()

    return df

import pandas as pd
from database import get_connection
from queries import top_states_insurance_policies


def get_top_states_insurance_df():

    conn = get_connection()
    cursor = conn.cursor()

    data = top_states_insurance_policies(cursor)

    df = pd.DataFrame(data, columns=[
        "State",
        "Total_Policies"
    ])

    df["Total_Policies"] = df["Total_Policies"].astype(float)

    cursor.close()
    conn.close()

    return df

def get_lowest_insurance_states_df():

    conn = get_connection()
    cursor = conn.cursor()

    data = lowest_insurance_states(cursor)

    df = pd.DataFrame(data, columns=[
        "State",
        "Total_Policies"
    ])

    df["Total_Policies"] = df["Total_Policies"].astype(float)

    cursor.close()
    conn.close()

    return df

def get_top_states_insurance_value_df():
    conn = get_connection()
    cursor = conn.cursor()
    data = top_states_insurance_value(cursor)
    df = pd.DataFrame(data, columns=["State","Total_Policies","Total_Insurance_Value"])
    df["Total_Policies"] = df["Total_Policies"].astype(float)
    df["Total_Insurance_Value"] = df["Total_Insurance_Value"].astype(float)
    cursor.close()
    conn.close()
    return df

def get_insurance_quarterly_df():
    conn = get_connection()
    cursor = conn.cursor()
    data = insurance_quarterly_trend(cursor)
    
    df = pd.DataFrame(
        data,
        columns=["Year", "Quarter", "Total_Policies", "Total_Insurance_Value"]
    )
    
    # Create Year-Quarter column
    df["Year_Quarter"] = df["Year"].astype(str) + "-Q" + df["Quarter"].astype(str)
    df = df[["Year_Quarter","Total_Policies","Total_Insurance_Value"]]
    
    cursor.close()
    conn.close()
    
    return df


#case study4:
def get_top_districts_transaction_df():
    
    conn = get_connection()
    cursor = conn.cursor()
    
    data = top_districts_transaction_value(cursor)
    
    df = pd.DataFrame(
        data,
        columns=["State","District","Total_Transaction_Value"]
    )
    
    cursor.close()
    conn.close()
    
    return df

def get_lowest_districts_transaction_df():

    conn = get_connection()
    cursor = conn.cursor()

    data = lowest_districts_transaction_value(cursor)

    df = pd.DataFrame(
        data,
        columns=["State","District","Total_Transaction_Value"]
    )

    cursor.close()
    conn.close()

    return df

def get_transaction_quarterly_df():

    conn = get_connection()
    cursor = conn.cursor()

    data = transaction_quarterly_trend(cursor)

    df = pd.DataFrame(
        data,
        columns=["Year","Quarter","Total_Transaction_Value"]
    )

    # Create Year-Quarter column
    df["Year_Quarter"] = df["Year"].astype(str) + "-Q" + df["Quarter"].astype(str)
    df = df[["Year_Quarter","Total_Transaction_Value"]]

    cursor.close()
    conn.close()

    return df

def get_avg_transaction_district_df():

    conn = get_connection()
    cursor = conn.cursor()

    data = avg_transaction_value_district(cursor)

    df = pd.DataFrame(
        data,
        columns=["State","District","Avg_Transaction_Value"]
    )

    cursor.close()
    conn.close()

    return df

def get_high_transaction_activity_df():

    conn = get_connection()
    cursor = conn.cursor()

    data = high_transaction_activity_districts(cursor)

    df = pd.DataFrame(
        data,
        columns=[
            "State",
            "District",
            "Total_Transactions",
            "Total_Transaction_Value",
            "Avg_Transaction_Value"
        ]
    )

    cursor.close()
    conn.close()

    return df


# case study :5
def get_highest_user_engagement_df():

    conn = get_connection()
    cursor = conn.cursor()

    data = highest_user_engagement_states(cursor)

    df = pd.DataFrame(
        data,
        columns=["State","Engagement_Ratio"]
    )

    cursor.close()
    conn.close()

    return df

def get_highest_user_pincode_df():

    conn = get_connection()
    cursor = conn.cursor()

    data = highest_user_pincode(cursor)

    df = pd.DataFrame(
        data,
        columns=["State","Pincode","Total_Users"]
    )

    # convert pincode to string
    df["Pincode"] = df["Pincode"].astype(str)

    cursor.close()
    conn.close()

    return df

def get_highest_district_engagement_df():

    conn = get_connection()
    cursor = conn.cursor()

    data = highest_district_user_engagement(cursor)

    df = pd.DataFrame(
        data,
        columns=["State","District","Engagement_Ratio"]
    )

    cursor.close()
    conn.close()

    return df

def get_user_growth_df():

    conn = get_connection()
    cursor = conn.cursor()

    data = user_growth_trend(cursor)

    df = pd.DataFrame(
        data,
        columns=["Year","Quarter","Total_Users"]
    )

    df["Year_Quarter"] = df["Year"].astype(str) + "-Q" + df["Quarter"].astype(str)

    cursor.close()
    conn.close()

    return df

def get_lowest_user_engagement_df():

    conn = get_connection()
    cursor = conn.cursor()

    data = lowest_user_engagement_states(cursor)

    df = pd.DataFrame(
        data,
        columns=[
            "State",
            "Total_Users",
            "Total_App_Opens",
            "Engagement_Ratio"
        ]
    )

    # sort by lowest engagement
    df = df.sort_values(by="Engagement_Ratio", ascending=True)

    cursor.close()
    conn.close()

    return df

def get_states_list():

    conn = get_connection()
    cursor = conn.cursor()

    data = get_states(cursor)

    states = [row[0] for row in data]

    cursor.close()
    conn.close()

    return states


def get_state_transaction_df(state):

    conn = get_connection()
    cursor = conn.cursor()

    data = state_transaction_trend(cursor, state)

    df = pd.DataFrame(
        data,
        columns=["Year", "Total_Transactions"]
    )

    cursor.close()
    conn.close()

    return df

# get district list
def get_districts_list(state):

    conn = get_connection()
    cursor = conn.cursor()

    data = get_districts(cursor, state)

    districts = [row[0] for row in data]

    cursor.close()
    conn.close()

    return districts


# get district transaction dataframe
def get_district_transaction_df(state, district):

    conn = get_connection()
    cursor = conn.cursor()

    data = district_transaction_trend(cursor, state, district)

    df = pd.DataFrame(data, columns=[
        "Year",
        "Total_Transactions"
    ])

    cursor.close()
    conn.close()

    return df
    

    

def total_transactions_over_years(cursor):
    cursor.execute("""
        SELECT Year, SUM(Transaction_count)
        FROM aggregated_transaction
        GROUP BY Year
        ORDER BY Year;
    """)
    return cursor.fetchall()

def total_amount_over_years(cursor):
    cursor.execute("""
        SELECT year, SUM(transaction_amount)
        FROM aggregated_transaction
        GROUP BY year
        ORDER BY year;
    """)
    return cursor.fetchall()

def top_10_states_transaction_amount(cursor):
    cursor.execute("""
        SELECT State,
               SUM(Transaction_amount) AS Total_Amount
        FROM aggregated_transaction
        GROUP BY State
        ORDER BY Total_Amount DESC
        LIMIT 10;
    """)
    return cursor.fetchall()

def transaction_type_distribution(cursor):
    cursor.execute("""
        SELECT Transaction_type,
               SUM(Transaction_count) AS Total_Transactions
        FROM aggregated_transaction
        GROUP BY Transaction_type
        ORDER BY Total_Transactions DESC;
    """)
    return cursor.fetchall()

def state_year_transaction_amount(cursor):
    cursor.execute("""
        SELECT State, Year,
        SUM(Transaction_amount) AS Total_Amount
        FROM aggregated_transaction
        GROUP BY State, Year
        ORDER BY State, Year;
    """)
    return cursor.fetchall()


#case study:2
def top_device_brands(cursor):
    cursor.execute("""
        SELECT User_brand,
        SUM(User_count) AS Total_Users
        FROM aggregated_users
        GROUP BY User_brand
        ORDER BY Total_Users DESC
        LIMIT 10;
    """)
    return cursor.fetchall()

def device_brand_percentage(cursor):
    cursor.execute("""
        SELECT User_brand,
        AVG(User_percentage) AS Avg_User_Percentage
        FROM aggregated_users
        GROUP BY User_brand
        ORDER BY Avg_User_Percentage DESC
        LIMIT 10;
    """)
    return cursor.fetchall()

def device_brand_growth(cursor):

    query = """
    SELECT Year,
           User_brand,
           SUM(User_count) AS Total_Users
    FROM aggregated_users
    GROUP BY Year, User_brand
    ORDER BY Year
    """

    cursor.execute(query)
    return cursor.fetchall()

def top_brand_each_state(cursor):
    query = """
    SELECT State,
           User_brand,
           SUM(User_count) AS Total_Users
    FROM aggregated_users
    WHERE User_brand != 'Others'
    GROUP BY State, User_brand
    ORDER BY State, Total_Users DESC
    """
    cursor.execute(query)
    return cursor.fetchall()

def top_device_brands(cursor):

    query = """
    SELECT User_brand,
           SUM(User_count) AS Total_Users
    FROM aggregated_users
    WHERE User_brand != 'Others'
    GROUP BY User_brand
    ORDER BY Total_Users DESC
    LIMIT 10
    """

    cursor.execute(query)
    return cursor.fetchall()

#case study:3
def insurance_growth_over_years(cursor):

    query = """
    SELECT  
        Year,
        SUM(Insurance_count) AS Total_Policies,
        SUM(Insurance_amount) AS Total_Insurance_Value
    FROM aggregated_insurance
    GROUP BY Year
    ORDER BY Year
    """

    cursor.execute(query)
    return cursor.fetchall()

def top_states_insurance_policies(cursor):

    query = """
    SELECT 
        State,
        SUM(Insurance_count) AS Total_Policies
    FROM map_insurance
    GROUP BY State
    ORDER BY Total_Policies DESC
    LIMIT 10
    """

    cursor.execute(query)
    return cursor.fetchall()

def lowest_insurance_states(cursor):

    query = """
    SELECT 
        State,
        SUM(Insurance_count) AS Total_Policies
    FROM map_insurance
    GROUP BY State
    ORDER BY Total_Policies ASC
    LIMIT 10
    """

    cursor.execute(query)
    return cursor.fetchall()

def top_states_insurance_value(cursor):
    query = """ 
    SELECT 
        State,
        SUM(Insurance_count) AS Total_Policies,
        SUM(Insurance_amount) AS Total_Insurance_Value
    FROM map_insurance
    GROUP BY State
    ORDER BY Total_Insurance_Value DESC
    LIMIT 10
    """
    cursor.execute(query)
    return cursor.fetchall()


def insurance_quarterly_trend(cursor):
    query = """ 
    SELECT 
        Year,
        Quarter,
        SUM(Insurance_count) AS Total_Policies,
        SUM(Insurance_amount) AS Total_Insurance_Value
    FROM aggregated_insurance
    GROUP BY Year, Quarter
    ORDER BY Year, Quarter
    """
    cursor.execute(query)
    return cursor.fetchall()

#case study 4
def top_districts_transaction_value(cursor):
    query = """
    SELECT 
        State,
        District,
        SUM(Transaction_amount) AS Total_Transaction_Value
    FROM map_transaction
    GROUP BY State, District
    ORDER BY Total_Transaction_Value DESC
    LIMIT 10
    """
    
    cursor.execute(query)
    return cursor.fetchall()

def lowest_districts_transaction_value(cursor):

    query = """
    SELECT 
        State,
        District,
        SUM(Transaction_amount) AS Total_Transaction_Value
    FROM map_transaction
    GROUP BY State, District
    ORDER BY Total_Transaction_Value ASC
    LIMIT 10
    """

    cursor.execute(query)
    return cursor.fetchall()


def transaction_quarterly_trend(cursor):

    query = """
    SELECT 
        Year,
        Quarter,
        SUM(Transaction_amount) AS Total_Transaction_Value
    FROM aggregated_transaction
    GROUP BY Year, Quarter
    ORDER BY Year, Quarter
    """

    cursor.execute(query)
    return cursor.fetchall()

def avg_transaction_value_district(cursor):

    query = """
    SELECT 
        State,
        District,
        SUM(Transaction_amount) / SUM(Transaction_count) AS Avg_Transaction_Value
    FROM map_transaction
    GROUP BY State, District
    ORDER BY Avg_Transaction_Value DESC
    LIMIT 10
    """

    cursor.execute(query)
    return cursor.fetchall()

def high_transaction_activity_districts(cursor):

    query = """
    SELECT 
        State,
        District,
        SUM(Transaction_count) AS Total_Transactions,
        SUM(Transaction_amount) AS Total_Transaction_Value,
        SUM(Transaction_amount)/SUM(Transaction_count) AS Avg_Transaction_Value
    FROM map_transaction
    GROUP BY State, District
    ORDER BY Total_Transactions DESC
    LIMIT 10
    """

    cursor.execute(query)
    return cursor.fetchall()

#case study 5
def highest_user_engagement_states(cursor):

    query = """
    SELECT 
        State,
        SUM(App_opens) / SUM(Registered_user) AS Engagement_Ratio
    FROM map_users
    GROUP BY State
    ORDER BY Engagement_Ratio DESC
    LIMIT 10
    """

    cursor.execute(query)
    return cursor.fetchall()


def highest_user_pincode(cursor):

    query = """
    SELECT 
        State,
        Pincode,
        SUM(Registered_user) AS Total_Users
    FROM top_users_pincode
    GROUP BY State, Pincode
    ORDER BY Total_Users DESC
    LIMIT 10
    """

    cursor.execute(query)
    return cursor.fetchall()

def highest_district_user_engagement(cursor):

    query = """
    SELECT 
        State,
        District,
        SUM(App_opens) / SUM(Registered_user) AS Engagement_Ratio
    FROM map_users
    GROUP BY State, District
    ORDER BY Engagement_Ratio DESC
    LIMIT 10
    """

    cursor.execute(query)
    return cursor.fetchall()


def user_growth_trend(cursor):

    query = """
    SELECT 
        Year,
        Quarter,
        SUM(Registered_user) AS Total_Users
    FROM map_users
    GROUP BY Year, Quarter
    ORDER BY Year, Quarter
    """

    cursor.execute(query)
    return cursor.fetchall()


def lowest_user_engagement_states(cursor):

    query = """
    SELECT 
        State,
        SUM(Registered_user) AS Total_Users,
        SUM(App_opens) AS Total_App_Opens,
        SUM(App_opens) / SUM(Registered_user) AS Engagement_Ratio
    FROM map_users
    GROUP BY State
    ORDER BY Engagement_Ratio ASC
    LIMIT 10
    """

    cursor.execute(query)
    return cursor.fetchall()

# queries.py

def get_states(cursor):

    query = """
    SELECT DISTINCT State
    FROM map_transaction
    ORDER BY State
    """

    cursor.execute(query)
    return cursor.fetchall()


def state_transaction_trend(cursor, state):

    query = """
    SELECT 
        Year,
        SUM(Transaction_count) AS Total_Transactions
    FROM map_transaction
    WHERE State = %s
    GROUP BY Year
    ORDER BY Year
    """

    cursor.execute(query, (state,))
    return cursor.fetchall()

# get districts for selected state
def get_districts(cursor, state):

    query = """
    SELECT DISTINCT District
    FROM map_transaction
    WHERE State = %s
    ORDER BY District
    """

    cursor.execute(query, (state,))
    return cursor.fetchall()


# district transaction trend
def district_transaction_trend(cursor, state, district):

    query = """
    SELECT
        Year,
        SUM(Transaction_count) AS Total_Transactions
    FROM map_transaction
    WHERE State = %s AND District = %s
    GROUP BY Year
    ORDER BY Year
    """

    cursor.execute(query, (state, district))
    return cursor.fetchall()




from database import get_connection

def get_map_data():   

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT 
        State,
        SUM(Transaction_count) AS transaction_count,
        SUM(Transaction_amount) AS transaction_amount
    FROM aggregated_transaction
    GROUP BY State
    """

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data  



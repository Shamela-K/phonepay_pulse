import streamlit as st
import plotly.express as px
import pandas as pd
from analysis import get_transactions_df
from analysis import get_amount_df
from analysis import get_top_states_df
from analysis import get_transaction_type_df
from analysis import get_state_trend_df
from analysis import get_device_brand_df
from analysis import get_device_percentage_df
from analysis import get_device_growth_df
from analysis import get_top_brand_state_df
from analysis import get_top_device_brands_df
from analysis import get_insurance_growth_df
from analysis import get_top_states_insurance_df
from analysis import get_lowest_insurance_states_df
from analysis import get_top_states_insurance_value_df
from analysis import get_insurance_quarterly_df
from analysis import get_top_districts_transaction_df
from analysis import get_lowest_districts_transaction_df
from analysis import get_transaction_quarterly_df
from analysis import get_avg_transaction_district_df
from analysis import get_high_transaction_activity_df
from analysis import get_highest_user_engagement_df
from analysis import get_highest_user_pincode_df
from analysis import get_highest_district_engagement_df
from analysis import get_user_growth_df
from analysis import get_lowest_user_engagement_df
from queries import get_map_data

from analysis import (
    get_states_list,
    get_state_transaction_df,
    get_districts_list,
    get_district_transaction_df
)

# -----------------------
# SIDEBAR NAVIGATION
# -----------------------
page = st.sidebar.selectbox(
    "Navigation",
    ["Home", "Analysis"]
)

# -----------------------
# HOME PAGE
# -----------------------
if page == "Home":
    st.title("PhonePe Pulse")
    st.write("Welcome to the PhonePe Pulse Dashboard")
    
 
    st.markdown("<h1 style='text-align:center; color:brown;'>India Transactions Dashboard</h1>", unsafe_allow_html=True)


    df = pd.read_csv(
    "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/"
    "e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")


    india_geojson = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/" \
                "e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"

# --- Rename columns to match transactions (so later real CSV works directly) ---
    df.rename(columns={
    'state': 'State',
    'active cases': 'Transaction_Count'
    }, inplace=True)

# --- Add a placeholder Transaction_Amount column ---
    df['Transaction_Amount'] = df['Transaction_Count'] * 500  # Example multiplier for demo

# --- Plotly choropleth with hover info ---
    fig = px.choropleth(
    df,
    geojson=india_geojson,
    featureidkey='properties.ST_NM',
    locations='State',
    color='Transaction_Count',
    hover_data={
        'State': True,
        'Transaction_Count': True,
        'Transaction_Amount': True
    },
    color_continuous_scale='Blues',
    title="India Transaction Overview"
)

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0})

# --- Show map in Streamlit ---
    st.plotly_chart(fig, use_container_width=True)
# -----------------------
# ANALYSIS PAGE
# -----------------------
elif page == "Analysis":

    st.title("Business Case Studies")

    case_study = st.selectbox(
        "Select Case Study",
        [
            "Decoding Transaction Dynamics on PhonePe",
            "Device Dominance and User Engagement Analysis",
            "Insurance Penetration and Growth Potential Analysis",
            "Transaction Analysis for Market Expansion",
            "User Engagement and Growth Strategy",
            "Overall Analysis"
        ]
    )

    # =========================
    # CASE STUDY 1
    # =========================
    if case_study == "Decoding Transaction Dynamics on PhonePe":

        #Query:1
        df = get_transactions_df()
        st.markdown(
        "<h3 style='color:red;'>Transaction Trends Overview</h2>",
        unsafe_allow_html=True
        )

       
        fig = px.line(
            df,
            x="Year",
            y="Transactions",
            markers=True,
            title="Total Transactions Over Years",color_discrete_sequence=["#3826BC"])

        st.plotly_chart(fig, use_container_width=True)
        
       
        #Query:2
        df2 = get_amount_df()
        st.markdown(
        "<h3 style='color:red;'>Total Transaction Amount Over Years</h3>",
        unsafe_allow_html=True
        )

        fig2 = px.line(
            df2, 
            x="Year",
            y="Total_Amount",
            markers=True,
            title="Total Transactions Amount Over Years",color_discrete_sequence=["#FF4B4B"])

        st.plotly_chart(fig2, use_container_width=True)

        #Query:3
        df3 = get_top_states_df()

        st.markdown(
            "<h3 style='color:red;'>Top 10 States by Transaction Amount</h3>",
            unsafe_allow_html=True
        )

        colors = [
            "#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A",
            "#19D3F3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"
        ]

        fig3 = px.bar(
            df3,
            x="State",
            y="Total_Amount",
            color="State",
            color_discrete_sequence=colors
        )

        fig3.update_layout(
            template="plotly_white",
            xaxis_tickangle=-45
        )
        st.plotly_chart(fig3, use_container_width=True)


        #Query:4
        df4 = get_transaction_type_df()

        st.markdown(
        "<h3 style='color:red;'>Transaction Type Distribution</h3>",
         unsafe_allow_html=True
        )
        colors = [
        "#636EFA",  # blue
        "#EF553B",  # red
        "#00CC96",  # green
        "#AB63FA",  # purple
        "#FFA15A"   # orange
        ]
        
        fig4 = px.pie(
        df4,
        names="Transaction_type",
        values="Total_Transactions",
        title="Transaction Type Distribution",
        hole=0.4,
        color_discrete_sequence=colors
        )
        fig4.update_traces(textinfo="percent")
        st.plotly_chart(fig4, use_container_width=True)
        

        #Query:5
        df5 = get_state_trend_df()

        top_states = df5.groupby("State")["Total_Amount"].sum().sort_values(ascending=False).head(5)

        top_states_list = list(top_states.index)

        df_top = df5[df5["State"].isin(top_states_list)]

        st.markdown(
        "<h3 style='color:red;'>Top 5 States Transaction Trend</h3>",
        unsafe_allow_html=True
        )

        fig5 = px.line(
        df_top,
        x="Year",
        y="Total_Amount",
        color="State",
        markers=True
        )

        st.plotly_chart(fig5, use_container_width=True)


    elif case_study == "Device Dominance and User Engagement Analysis":   
        st.markdown(
        "<h3 style='color:#FF4B4B;'>Top Device Brands by Registered Users</h2>",
        unsafe_allow_html=True
        )

        df1 = get_device_brand_df()

        fig1 = px.bar(
        df1,
        x="Brand",
        y="Total_Users",
        color="Brand",
        title="Top Device Brands by Registered Users"
        )

        fig1.update_layout(
        template="plotly_white",
        xaxis_tickangle=-45
        )

        st.plotly_chart(fig1, use_container_width=True)

        #Query:2
        df2 = get_device_percentage_df()

        st.markdown(
        "<h3 style='color:red;'>Device Brand Market Share</h3>",
        unsafe_allow_html=True)

        colors = [
        "#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A",
        "#19D3F3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"]

        fig2 = px.pie(
        df2,
        names="Brand",
        values="Avg_Percentage",
        hole=0.4,
        color_discrete_sequence=colors)

        fig2.update_traces(textinfo="percent")

        st.plotly_chart(fig2, use_container_width=True)

        #query:3
        st.markdown(
        "<h3 style='color:red;'>Device Brand Usage Growth Over Years</h3>",
        unsafe_allow_html=True)

        # Get dataframe
        df = get_device_growth_df()


        #  Dropdown menu
        brand_list = sorted(df["Brand"].unique())

        selected_brand = st.selectbox(
        "Select Device Brand",
        brand_list)


        # Filter dataframe
        filtered_df = df[df["Brand"] == selected_brand]


        # Line chart
        fig = px.line(
        filtered_df,
        x="Year",
        y="Total_Users",
        markers=True,
        title=f"{selected_brand} User Growth Over Years")

        fig.update_traces(
        marker=dict(size=7),
        line=dict(width=3))

        fig.update_layout(
        template="plotly_white",
        width=900,
        height=500)


        st.plotly_chart(fig, use_container_width=True)

    
        df4 = get_top_brand_state_df()

        st.markdown(
       "<h3 style='color:red;'>Top Device Brand in Each State</h3>",
        unsafe_allow_html=True)

        fig4 = px.bar(
        df4,
        y="State",
        x="Total_Users",
        color="Brand",
        orientation="h")

        fig4.update_layout(
        template="plotly_white",
        width=1000,
        height=600)

        st.plotly_chart(fig4, use_container_width=True)

        
        # Query 5:


        df5 = get_top_device_brands_df()

        st.markdown(
        "<h3 style='color:red;'>Top 10 Device Brands Comparison</h3>",
        unsafe_allow_html=True)

        fig5 = px.bar(
        df5,
        x="Brand",
        y="Total_Users",
        text="Total_Users",
        color="Brand",
        color_discrete_sequence=px.colors.qualitative.Set3)

        fig5.update_layout(
        title="Top Device Brands by Registered Users",
        title_x=0.5,
        template="plotly_white",
        width=900,
        height=500,
        xaxis_title="Device Brand",
        yaxis_title="Total Users",
        bargap=0.25)

        fig5.update_traces(textposition="outside")

        st.plotly_chart(fig5, use_container_width=True)

        #case study:3
    elif case_study == "Insurance Penetration and Growth Potential Analysis":
        
        df = get_insurance_growth_df()

        st.markdown(
        "<h3 style='color:red;'>Insurance Adoption Growth Over Years</h3>",
        unsafe_allow_html=True)

        fig = px.line(
        df,
        x="Year",
        y="Total_Policies",
        markers=True,
        line_shape="spline",
        color_discrete_sequence=["#2E86AB"])

        fig.update_traces(
        marker=dict(size=9),
        line=dict(width=3))

        fig.update_layout(
        template="plotly_white",
        width=900,
        height=500)
        st.metric("Total Policies", f"{df['Total_Policies'].sum():,.0f}")
        st.metric("Total Insurance Value", f"₹{df['Total_Insurance_Value'].sum():,.0f}")
        st.plotly_chart(fig, use_container_width=True)


       

        df2 = get_top_states_insurance_df()

        st.markdown(
        "<h3 style='color:red;'>Top States by Insurance Adoption</h3>",
        unsafe_allow_html=True )

        fig = px.bar(
        df2,
        x="State",
        y="Total_Policies",
        text="Total_Policies",
        color="State",
        color_discrete_sequence=px.colors.qualitative.Bold)

        fig.update_layout(
        title="Top States by Insurance Adoption",
        title_x=0.5,
        template="plotly_white",
        width=1000,
        height=600,
        bargap=0.25,
        xaxis_tickangle=-45 )

        fig.update_traces(textposition="outside")

        st.plotly_chart(fig, use_container_width=True)


        df3 = get_lowest_insurance_states_df()

        st.markdown(
        "<h3 style='color:#D62728;'>States with Lowest Insurance Adoption</h3>",
        unsafe_allow_html=True)

        fig3 = px.bar(
        df3,
        x="State",
        y="Total_Policies",
        text="Total_Policies",
        color="State",
        color_discrete_sequence=px.colors.qualitative.Bold)

        fig3.update_layout(
        title="States with Lowest Insurance Adoption",
        title_x=0.5,
        template="plotly_white",
        width=1000,
        height=600,
        bargap=0.25,
        xaxis_tickangle=-45)

        fig3.update_traces(textposition="outside")

        st.plotly_chart(fig3, use_container_width=True)

        df4 = get_top_states_insurance_value_df()

        st.markdown("<h3 style='color:red;'>Top States by Insurance Value</h3>", unsafe_allow_html=True)

        fig4 = px.bar(
        df4,
        x="State",
        y="Total_Insurance_Value",
        text="Total_Insurance_Value",
        color="State",
        color_discrete_sequence=px.colors.qualitative.Bold,
        width=1000,
        height=600)

        fig4.update_layout(
        title="Top States by Insurance Value",
        title_x=0.5,
        template="plotly_white",
        bargap=0.25,
        xaxis_tickangle=-45,
        plot_bgcolor="#F8F9FA",
        paper_bgcolor="#FFFFFF")

        fig4.update_traces(textposition="outside")

        st.plotly_chart(fig4, use_container_width=True)

        df5 = get_insurance_quarterly_df()

        st.markdown("<h3 style='color:red;'>Insurance Adoption Trend by Quarter</h3>", unsafe_allow_html=True)

        fig5 = px.line(
        df5,
        x="Year_Quarter",
        y="Total_Insurance_Value",
        markers=True,
        title="Insurance Value Growth by Quarter",
        line_shape="spline",
        color_discrete_sequence=["#2E86AB"],
        width=950,
        height=500)

        fig5.update_traces(
        marker=dict(size=9),
        line=dict(width=2),
        text=df5["Total_Insurance_Value"],
        textposition="top center")

        fig5.update_layout(
        title_x=0.5,
        template="plotly_white",
        plot_bgcolor="#F8F9FA",
        paper_bgcolor="#FFFFFF",
        font=dict(size=14))

        fig5.update_xaxes(showgrid=True, gridcolor="lightgray", tickangle=-45)
        fig5.update_yaxes(showgrid=True, gridcolor="lightgray")

        st.plotly_chart(fig5, use_container_width=True)

     #case study:4
    elif case_study == "Transaction Analysis for Market Expansion":
        # Query 1: Top Districts by Transaction Value
        df1 = get_top_districts_transaction_df()

        st.markdown(
        "<h3 style='color:red;'>Top Districts by Transaction Value</h3>",
        unsafe_allow_html=True)

        fig1 = px.bar(
        df1,
        x="District",
        y="Total_Transaction_Value",
        color="State",
        text="Total_Transaction_Value",
        color_discrete_sequence=px.colors.qualitative.Set2)

        fig1.update_layout(
        title="Top Districts by Transaction Value",
        title_x=0.5,
        template="plotly_white",
        width=1000,
        height=550,
        xaxis_title="District",
        yaxis_title="Total Transaction Value",
        xaxis_tickangle=-45,
        bargap=0.25,
        plot_bgcolor="#F8F9FA",
        paper_bgcolor="#FFFFFF")

        fig1.update_traces(textposition="outside")

        st.plotly_chart(fig1, use_container_width=True)   

        # Query 2: Lowest Performing Districts

        df2 = get_lowest_districts_transaction_df()

        st.markdown(
        "<h3 style='color:red;'>Lowest Performing Districts</h3>",
        unsafe_allow_html=True)

        fig2 = px.bar(
        df2,
        y="District",
        x="Total_Transaction_Value",
        color="State",
        orientation="h",
        text="Total_Transaction_Value",
        color_discrete_sequence=px.colors.qualitative.Pastel)

        fig2.update_layout(
        title="Lowest Performing Districts by Transaction Value",
        title_x=0.5,
        template="plotly_white",
        width=1000,
        height=550,
        xaxis_title="Total Transaction Value",
        yaxis_title="District",
        bargap=0.25,
        plot_bgcolor="#F8F9FA",
        paper_bgcolor="#FFFFFF")

        fig2.update_traces(textposition="outside")

        st.plotly_chart(fig2, use_container_width=True)

        # Query 3: Quarterly Transaction Growth Trend

        df3 = get_transaction_quarterly_df()

        st.markdown(
        "<h3 style='color:red;'>Quarterly Transaction Growth Trend</h3>",
        unsafe_allow_html=True)

        fig3 = px.line(
        df3,
        x="Year_Quarter",
        y="Total_Transaction_Value",
        markers=True,
        line_shape="spline",
        color_discrete_sequence=["#1f77b4"])

        fig3.update_traces(
        marker=dict(size=6),
        line=dict(width=3),
        text=df3["Total_Transaction_Value"],
        textposition="top center")

        fig3.update_layout(
        title="Quarterly Transaction Growth Trend",
        title_x=0.5,
        template="plotly_white",
        width=950,
        height=500,
        xaxis_title="Year & Quarter",
        yaxis_title="Total Transaction Value",
        xaxis_tickangle=-45,
        plot_bgcolor="#F8F9FA",
        paper_bgcolor="#FFFFFF",
        font=dict(size=14))

        fig3.update_xaxes(showgrid=True, gridcolor="lightgray")
        fig3.update_yaxes(showgrid=True, gridcolor="lightgray")

        st.plotly_chart(fig3, use_container_width=True)


        # Query 4: Average Transaction Value per District

        df4 = get_avg_transaction_district_df()

        st.markdown(
        "<h3 style='color:red;'>Top Districts by Average Transaction Value</h3>",
        unsafe_allow_html=True)

        fig4 = px.bar(
        df4,
        x="Avg_Transaction_Value",
        y="District",
        color="State",
        orientation="h",
        title="Top Districts by Average Transaction Value",
        color_discrete_sequence=px.colors.qualitative.Set2
        )

        fig4.update_layout(
        title_x=0.5,
        template="plotly_white",
        width=1500,
        height=650,
        bargap=0.25,
        plot_bgcolor="#F8F9FA",
        paper_bgcolor="#FFFFFF")

        st.plotly_chart(fig4, use_container_width=True)


        # Query 5: High Transaction Count but Lower Value Districts

        df5 = get_high_transaction_activity_df()

        st.markdown(
        "<h3 style='color:red;'>High Transaction Activity Districts</h3>",
        unsafe_allow_html=True)

        fig5 = px.bar(
        df5,
        x="Total_Transactions",
        y="District",
        color="State",
        orientation="h",
        title="Top Districts by Transaction Activity",
        color_discrete_sequence=px.colors.qualitative.Set2)

        fig5.update_layout(
        title_x=0.5,
        template="plotly_white",
        width=1000,
        height=550,
        xaxis_title="Total Transactions",
        yaxis_title="District",
        bargap=0.25,
        plot_bgcolor="#F8F9FA",
        paper_bgcolor="#FFFFFF",
        font=dict(size=14))

        st.plotly_chart(fig5, use_container_width=True)

        #case study:5
    elif case_study == "User Engagement and Growth Strategy":

        # Query 1: States with Highest User Engagement
        df1 = get_highest_user_engagement_df()

        st.markdown(
        "<h3 style='color:red;'>States with Highest User Engagement</h3>",
        unsafe_allow_html=True)

        fig1 = px.bar(
        df1,
        x="State",
        y="Engagement_Ratio",
        color="State",
        title="States with Highest User Engagement",
        color_discrete_sequence=px.colors.qualitative.Bold)

        fig1.update_layout(
        title_x=0.5,
        template="plotly_white",
        width=950,
        height=600,
        xaxis_tickangle=-45,
        bargap=0.25,
        plot_bgcolor="#F8F9FA",
        paper_bgcolor="#FFFFFF",
        font=dict(size=14))

        st.plotly_chart(fig1, use_container_width=True)   


        df2 = get_highest_user_pincode_df()

        st.markdown(
        "<h3 style='color:red;'>Top Pincode Areas by Registered Users</h3>",
        unsafe_allow_html=True)

        fig2 = px.bar(
        df2,
        x="Total_Users",
        y="Pincode",
        color="State",
        orientation="h",
        title="Top Pincode Areas by Registered Users",
        color_discrete_sequence=px.colors.qualitative.Set2)

        fig2.update_layout(
        title_x=0.5,
        template="plotly_white",
        width=1000,
        height=550,
        xaxis_title="Total Registered Users",
        yaxis_title="Pincode",
        bargap=0.25,
        plot_bgcolor="#F8F9FA",
        paper_bgcolor="#FFFFFF",
        font=dict(size=14))

        st.plotly_chart(fig2, use_container_width=True)


        # Query 3: Districts with Highest User Engagement

        df3 = get_highest_district_engagement_df()

        st.markdown(
        "<h3 style='color:red;'>Districts with Highest User Engagement</h3>",
        unsafe_allow_html=True)

        fig3 = px.bar(
        df3,
        x="Engagement_Ratio",
        y="District",
        color="State",
        orientation="h",
        title="Districts with Highest PhonePe User Engagement",
        color_discrete_sequence=px.colors.qualitative.Set2)

        fig3.update_layout(
        title_x=0.5,
        template="plotly_white",
        width=1000,
        height=550,
        xaxis_title="Engagement Ratio",
        yaxis_title="District",
        bargap=0.25,
        plot_bgcolor="#F8F9FA",
        paper_bgcolor="#FFFFFF",
        font=dict(size=14))

        st.plotly_chart(fig3, use_container_width=True)

        # Query 4: User Growth Trend by Year and Quarter

        df4 = get_user_growth_df()

        st.markdown(
        "<h3 style='color:red;'>User Growth Trend Over Time</h3>",
        unsafe_allow_html=True)

        fig4 = px.line(
        df4,
        x="Year_Quarter",
        y="Total_Users",
        markers=True,
        title="User Growth Trend Over Time",
        line_shape="spline",
        color_discrete_sequence=["#2E86AB"])

        fig4.update_layout(
        title_x=0.5,
        template="plotly_white",
        width=950,
        height=500,
        xaxis_tickangle=-45,
        plot_bgcolor="#F8F9FA",
        paper_bgcolor="#FFFFFF",
        font=dict(size=14))

        fig4.update_traces(
        marker=dict(size=7),
        line=dict(width=3))

        fig4.update_xaxes(showgrid=True, gridcolor="lightgray")
        fig4.update_yaxes(showgrid=True, gridcolor="lightgray")

        st.plotly_chart(fig4, use_container_width=True)

        # Query 5: States with Low Engagement

        df5 = get_lowest_user_engagement_df()

        st.markdown(
        "<h3 style='color:red;'>States with Lowest User Engagement</h3>",
        unsafe_allow_html=True)

        fig5 = px.bar(
        df5,
        x="State",
        y="Engagement_Ratio",
        color="State",
        title="States with Lowest User Engagement",
        color_discrete_sequence=px.colors.qualitative.Set2)

        fig5.update_layout(
        title_x=0.5,
        template="plotly_white",
        width=950,
        height=600,
        xaxis_tickangle=-45,
        bargap=0.25,
        plot_bgcolor="#F8F9FA",
        paper_bgcolor="#FFFFFF",
        font=dict(size=14))

        st.plotly_chart(fig5, use_container_width=True)



       
    elif case_study == "Overall Analysis":
        st.markdown(
        "<h3 style='color:red;'>State- District- wise Transaction analysis</h3>",
        unsafe_allow_html=True)


    # ---------- STATE DROPDOWN ----------
        states = get_states_list()

        selected_state = st.selectbox(
        "Select State",
        states ,
        key="state_select")

      # ---------- STATE CHART ----------
        df_state = get_state_transaction_df(selected_state)

        fig1 = px.line(
        df_state,
        x="Year",
        y="Total_Transactions",
        markers=True,
        title=f"Transaction Trend in {selected_state}" )

        st.plotly_chart(fig1, use_container_width=True,key="state_chart")

        st.markdown("---")
        # ---------- DISTRICT DROPDOWN ----------
      
        districts = get_districts_list(selected_state)
        selected_district = st.selectbox(
        "Select District",
        districts ,
        key="district_select" )
        df_district = get_district_transaction_df(selected_state, selected_district)
        
        df_district["Year"] = df_district["Year"].astype(str)
        # ---------- DISTRICT CHART ----------
        fig2 = px.bar(
        df_district,
        x="Year",
        y="Total_Transactions",
        title=f"Transaction Trend in {selected_district}, {selected_state}"
        )

        fig2.update_layout(
        xaxis_title="Year",
        yaxis_title="Total Transactions",
        template="plotly_white",
        height = 450)

        st.plotly_chart(fig2, use_container_width=True,key="district_chart")

PhonePe Data Analysis and Insights
🚀 Project Overview

This project analyzes PhonePe digital payment data to uncover insights on:

Transaction growth and trends
User engagement and device usage
Insurance adoption patterns
Regional performance and market expansion opportunities

The goal is to provide actionable insights for business strategy and growth.

🎯 Objectives
Track transaction trends over time
Identify top-performing states and districts
Analyze user engagement patterns
Study device brand dominance
Understand insurance adoption trends
Highlight growth opportunities for PhonePe
🗂 Data Source

Data extracted from the PhonePe Pulse GitHub Repository https://github.com/PhonePe/pulse
 organized by:

Year → Quarter → State → District → Pin code
JSON files converted to tabular format using Python
Stored in a SQL database (12 tables) for efficient querying
🛠 Tools & Technologies
Python – Data analysis
Pandas – Data cleaning & processing
MySQL – Querying
Matplotlib & Seaborn – Visualizations
Plotly – Interactive charts
Streamlit – Dashboard
📊 Visualizations
Line Charts → Trends over time
Bar Charts → Comparisons across states/devices
Pie/Donut Charts → Distribution analysis
Horizontal Bar Charts → Rankings

💡 Key Insights & Recommendations

1. Transaction Dynamics
Transactions and transaction values steadily increased → reflects growing adoption
Recommendation: Retain users, expand in emerging states, promote high-value transactions
Maharashtra, Karnataka, Telangana lead in transaction amounts → strong infrastructure
Recommendation: Target top states, boost low-performing regions
P2P and Merchant payments dominate → daily usage
Recommendation: Enhance top category UX, incentivize underutilized types

2. Device Dominance
Xiaomi, Samsung, Vivo dominate users → app optimization required
Recommendation: Focus testing and updates on top brands, collaborate with manufacturers
Device usage increasing → rising smartphone penetration
Recommendation: Continue mobile-first strategies and enhance app features

3. Insurance Penetration
Insurance adoption growing gradually → increasing awareness
Certain states lead in policy adoption and value → high-value purchases
Recommendation: Target campaigns, strengthen insurer partnerships, promote premium products
Seasonal trends observed
Recommendation: Launch campaigns during peak quarters

4. Market Expansion
Few districts contribute most transaction value → high engagement areas
Some districts show frequent low-value transactions → small payments dominate
Recommendation: Focus expansion in high-value districts, introduce micro-payment offers

5. User Engagement
High engagement in certain states/districts → loyal users
Some states show low engagement despite registrations
Recommendation: Launch campaigns, offers, and beta testing in high-engagement areas; improve engagement in low-performing regions

📈 Dashboard

Interactive Streamlit dashboard includes:

Transaction trends and maps
Device brand usage analysis
Insurance growth and regional performance
User engagement metrics

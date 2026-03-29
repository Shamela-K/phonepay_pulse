from database import get_connection
from queries import total_transactions_over_years

conn = get_connection()
cursor = conn.cursor()

data = total_transactions_over_years(cursor)

print(data)

cursor.close()
conn.close()

from queries import state_transaction_trend

print("Import successful")
from queries import state_transaction_trend
print("Import successful")
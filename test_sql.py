import pyodbc

connection = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=DevOpsAI;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

print("Connected successfully!")

connection.close()
import pyodbc

print("ABOUT TO CONNECT TO SQL SERVER")
print("SERVER: host.docker.internal,1433")
print("DATABASE: DevOpsAI")
print("USER: devops_app")

connection = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=host.docker.internal,1433;"
    "DATABASE=DevOpsAI;"
    "UID=devops_app;"
    "PWD=Nitha@12345;"
    "TrustServerCertificate=yes;"
)

print("Connected successfully!")

connection.close()
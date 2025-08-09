import psycopg2

#Database connection parameters
conn = psycopg2.connect(
    dbname="project",
    user="postgres",
    password="Password",
    host="localhost",  # Change to your server if needed
    port="5432"  # Default PostgreSQL port
)

#Create a cursor to execute queries
cur = conn.cursor()

#Execute a simple query
cur.execute("SELECT * FROM users")

#Fetch and print the result
print(cur.fetchall())


#Close connection
cur.close()
conn.close()
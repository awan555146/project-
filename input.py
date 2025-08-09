import psycopg2

try:
    # 1. Connect to the database
    conn = psycopg2.connect(
        dbname="project",
        user="postgres",
        password="Password",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    # 2. Get data from user (or from somewhere else)
    name = input("Enter name: ")
    email = input("Enter email: ")

    # 3. Write SQL query to insert data
    insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"

    # 4. Execute the query
    cur.execute(insert_query, (name, email))

    # 5. Commit the changes
    conn.commit()
    print("Data inserted successfully.")

except Exception as e:
    print("Error:", e)

finally:
    # 6. Close connection
    if cur:
        cur.close()
    if conn:
        conn.close()

import mysql.connector


def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Ramune7913,/",
            database = "sakila"
        )
        print("Connection successful!")
        return connection
    except mysql.connector.Error as err:
        print(f"Connection error: {err}")
        return None


def execute_query(query):
    connection = connect_to_database()
    if not connection:
        return None

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Query execution error: {err}")
        return None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def daugiausiaiCustomeriu():
    query = """
        SELECT 
            store.store_id,
            COUNT(cust.customer_id) AS customer_count
        FROM 
            store
        JOIN 
            customer cust ON store.store_id = cust.store_id
        GROUP BY 
            store.store_id
        ORDER BY 
            customer_count DESC
        LIMIT 1
    """
    result = execute_query(query)
    if result:
        store_id, customer_count = result[0]
        return store_id, customer_count
    else:
        return None, None


def daugiausiaiIsnuomotuFilmu():
    query = """
        SELECT 
            store.store_id,
            COUNT(invent.inventory_id) AS film_count
        FROM 
            store
        JOIN 
            inventory invent ON store.store_id = invent.store_id
        GROUP BY 
            store.store_id
        ORDER BY 
            film_count DESC
        LIMIT 1
    """
    result = execute_query(query)
    if result:
        store_id, film_count = result[0]
        return store_id, film_count
    else:
        return None, None


def DidziausiaApyvarta(limit=2):
    query = f"""
        SELECT 
            store.store_id,
            SUM(payment.amount) AS revenue
        FROM 
            store
        JOIN 
            staff ON store.manager_staff_id = staff.staff_id
        JOIN 
            payment ON staff.staff_id = payment.staff_id
        GROUP BY 
            store.store_id
        ORDER BY 
            revenue DESC
        LIMIT {limit}
    """
    results = execute_query(query)
    return results

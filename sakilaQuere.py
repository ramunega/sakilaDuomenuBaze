print("1.atvaizduoti visus customerius")

import mysql.connector

hostname = "localhost"
username = "root"
password = "Ramune7913,/"
database = "sakila"

connection = None
cursor = None

try:
    connection = mysql.connector.connect(host=hostname, port=3306, user=username, password=password, database=database)
    print("Connection successful!")

    cursor = connection.cursor()
    query = "SELECT * FROM actor" # Replace with your desired query
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Surname: {row[2]}") # Access column data by index

except mysql.connector.Error as err:
    print(f"Connection error: {err}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
print("Connection closed.")

print("2.atvaizduoti visus customerius ir stulpelį kuriame būtų atvaizduota kiek pinigų kiekvienas jų yra išleidęs nuomai, ir kiek filmų nuomavesis")

import mysql.connector

hostname = "localhost"
username = "root"
password = "Ramune7913,/"
database = "sakila"

connection = None
cursor = None

try:
    connection = mysql.connector.connect(host=hostname, port=3306, user=username, password=password, database=database)
    print("Connection successful!")
    cursor = connection.cursor()
    query = """
        SELECT 
            cust.customer_id,
            cust.first_name,
            cust.last_name,
            SUM(pay.amount) AS isleistaSuma,
            COUNT(DISTINCT rent.rental_id) AS IsnuomotiFilmai
        FROM 
            customer cust
        JOIN 
            payment pay ON cust.customer_id = pay.customer_id
        JOIN 
            rental rent ON cust.customer_id = rent.customer_id
        GROUP BY 
            cust.customer_id, cust.first_name, cust.last_name
        ORDER BY 
            cust.customer_id
    """
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        customer_id, first_name, last_name, isleistaSuma, IsnuomotiFilmai = row
        print(f"Customer ID: {customer_id}, Vardas: {first_name} {last_name}, Isleista Suma: {isleistaSuma}, Isnuomotu filmu kiekis: {IsnuomotiFilmai}")

except mysql.connector.Error as err:
    print(f"Connection error: {err}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print("Connection closed.")

print("3.atvaizduoti aktorius ir keliuose filmuose jie yra filmavesi")

import mysql.connector

hostname = "localhost"
username = "root"
password = "Ramune7913,/"
database = "sakila"

connection = None
cursor = None

try:
    connection = mysql.connector.connect(host=hostname, port=3306, user=username, password=password, database=database)
    print("Connection successful!")
    cursor = connection.cursor()
    query = """
        SELECT 
            actor.actor_id,
            actor.first_name,
            actor.last_name,
            GROUP_CONCAT(film.title ORDER BY film.title SEPARATOR ', ') AS films_starred_in
        FROM 
            actor actor
        JOIN 
            film_actor filmactor ON actor.actor_id = filmactor.actor_id
        JOIN 
            film film ON filmactor.film_id = film.film_id
        GROUP BY 
            actor.actor_id, actor.first_name, actor.last_name
        ORDER BY 
            actor.actor_id
    """

    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        actor_id, first_name, last_name, films_starred_in = row
        print(f"Aktoriaus id: {actor_id}, Vardas: {first_name} {last_name}")
        print(f"Filmai kuriose vaidino: {films_starred_in}")

except mysql.connector.Error as err:
    print(f"Connection error: {err}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print("Connection closed.")

print("4.atvaizduoti visus filmus ir kiek aktorių juose vaidino")

import mysql.connector

hostname = "localhost"
username = "root"
password = "Ramune7913,/"
database = "sakila"

connection = None
cursor = None

try:
    connection = mysql.connector.connect(host=hostname, port=3306, user=username, password=password, database=database)
    print("Connection successful!")
    cursor = connection.cursor()
    query = """
        SELECT 
            film.film_id,
            film.title,
            COUNT(filmactor.actor_id) AS aktoriu_kiekis
        FROM 
            film film
        LEFT JOIN 
            film_actor filmactor ON film.film_id = filmactor.film_id
        GROUP BY 
            film.film_id, film.title
        ORDER BY 
            film.film_id
    """
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        film_id, title, aktoriu_kiekis = row
        print(f"Filmo ID: {film_id}, Pavadinimas: {title}, Aktoriu kiekis: {aktoriu_kiekis}")

except mysql.connector.Error as err:
    print(f"Connection error: {err}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print("Connection closed.")

print("5.-------------------------------------------------------------------------------------------------------------")

from function import (
    daugiausiaiCustomeriu,
    daugiausiaiIsnuomotuFilmu,
    DidziausiaApyvarta
)

def main():
    print("5.1. nustatyti kuris nuomos punktas: turi daugiau customerių")
    store_id, customer_count = daugiausiaiCustomeriu()
    if store_id is not None and customer_count is not None:
        print(f"Parduotuve turinti daugiausiai klientu: {store_id}, Klientu skaicius: {customer_count}")
    else:
        print()

    print("5.2. nustatyti kuris nuomos punktas: išnuomavo daugiau(ir kiek kiekvienas) filmų")
    store_id, film_count = daugiausiaiIsnuomotuFilmu()
    if store_id is not None and film_count is not None:
        print(f"Parduotuve isnuomojanti daugiausiai filmu: {store_id}, Filmu skaicius: {film_count}")
    else:
        print()

    print("5.3.nustatyti kuris nuomos punktas: kiek sugeneravo pajamų")
    top_stores = DidziausiaApyvarta(limit=2)
    if top_stores:
        for store_id, revenue in top_stores:
            print(f"Store ID: {store_id}, Apyvarta: {revenue}")
    else:
        print()

if __name__ == "__main__":
    main()
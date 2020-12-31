import psycopg2
from Iris import iris_list2

connection = psycopg2.connect(
    host="localhost",
    port="5432",
    database="Iris",
    user="postgres",
    password="4210375756")
cursor = connection.cursor()
for item in iris_list2:
    insert_query = "insert into iris_table (sepal_length,sepal_width,petal_length,petal_width,variety) values {}".format(
        tuple(item.lst))
    cursor.execute(insert_query)
connection.commit()
connection.close()

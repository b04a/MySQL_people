import mysql.connector

# Подключение к базе данных SELECT * FROM users;
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Оставь пустым, если пароль не был установлен
    database="my_database"
)

cursor = conn.cursor()

# Выполнение запроса (например, выбор всех баз данных)
cursor.execute("SELECT * FROM users")

# Выводим результат
for db in cursor:
    print(db)

# Закрываем соединение
cursor.close()
conn.close()
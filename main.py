import mysql.connector

# Подключение к базе данных SELECT * FROM users;
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Оставь пустым, если пароль не был установлен
    database="my_database"
)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS people (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        height INT
    )
""")


# Закрываем соединение
cursor.close()
conn.close()
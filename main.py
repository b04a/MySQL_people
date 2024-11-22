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

name = input("Input name people: ").split()
age = input("Input age people: ").split()
height = input("Input height people: ").split()

for i in range(len(name)):
    cursor.execute("""
        INSERT INTO people (name, age, height) VALUES (%s, %s, %s)
        """, (f"{name[i]}", int(age[i]), int(height[i])))


# Подтверждение изменений
conn.commit()

# Выборка данных
cursor.execute("SELECT * FROM people")
for (id, name, age, height) in cursor:
    print(f"ID: {id}, Name: {name}, Age: {age}, height: {height}")

# Закрытие соединения
cursor.close()
conn.close()
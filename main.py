import mysql.connector

# Подключение к базе данных
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Оставь пустым, если пароль не был установлен
    database="my_database",
)

cursor = conn.cursor()

# Выборка данных
cursor.execute("SELECT * FROM people")
for id, name, age, height in cursor:
    print(f"ID: {id}, Name: {name}, Age: {age}, height: {height}")

# Выполнение запроса на сумму возраста
cursor.execute(
    """
SELECT SUM(age) AS total_sum
FROM people;
"""
)

# Получение результата запроса
result = cursor.fetchone()  # Получаем первую строку результата
total_sum = result[0] if result else 0  # Если результат пустой, возвращаем 0
print(f"Total sum of ages: {total_sum}")

cursor.execute(
    """
SELECT AVG(height) AS average_value
FROM people;
"""
)

result_height = cursor.fetchone()
average_value = float(result_height[0]) if result_height else 0.0
print(f"AVG by age people: {average_value}")

# Закрытие соединения
cursor.close()
conn.close()

# Используем официальный Python-образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем файлы проекта
COPY src /app/src

# Устанавливаем команду по умолчанию
CMD ["pytest", "src/tests"]


# Используем базовый образ Ubuntu
FROM ubuntu:latest

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем содержимое текущей директории в контейнер
COPY . /app

# Устанавливаем Python и необходимые зависимости
RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Устанавливаем переменную окружения для UTF-8
ENV PYTHONUTF8=1

# Указываем команду для проверки
CMD echo "Hi, I'm inside"

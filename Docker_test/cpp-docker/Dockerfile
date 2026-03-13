# ---- Этап 1: сборка ----
FROM gcc:latest AS build
# Устанавливаем рабочую директорию
WORKDIR /app
# Копируем исходный код
COPY hello.cpp .
# Компилируем статически, чтобы не зависеть от динамических библиотек
RUN g++ -static -o hello hello.cpp
# ---- Этап 2: финальный образ ----
FROM alpine:latest
# Копируем скомпилированный бинарник из первого этапа
COPY --from=build /app/hello /usr/local/bin/hello
# Запускаем приложение
CMD ["hello"]
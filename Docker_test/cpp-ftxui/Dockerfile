# ---- Этап 1: сборка ----
FROM ubuntu:22.04 AS build
# Устанавливаем необходимые пакеты для сборки
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    && rm -rf /var/lib/apt/lists/*
# Создаём рабочую директорию
WORKDIR /app
# Копируем исходники
COPY main.cpp CMakeLists.txt ./
# Собираем проект
RUN mkdir build && cd build && \
    cmake .. && \
    make
# ---- Этап 2: финальный образ ----
FROM ubuntu:22.04
# Устанавливаем только необходимые рантайм-библиотеки
RUN apt-get update && apt-get install -y \
    libstdc++6 \
    && rm -rf /var/lib/apt/lists/*
# Копируем собранный бинарник из этапа сборки
COPY --from=build /app/build/ftxui_demo /usr/local/bin/ftxui_demo
# Запускаем приложение
CMD ["ftxui_demo"]
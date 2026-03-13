# Используем SDK для сборки
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
# Копируем файлы проекта и восстанавливаем зависимости
COPY ["MyApp.csproj", "."]
RUN dotnet restore "MyApp.csproj"
# Копируем весь код и публикуем приложение
COPY . .
RUN dotnet publish "MyApp.csproj" -c Release -o /app/publish
# Финальный образ с рантаймом
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS runtime
WORKDIR /app
COPY --from=build /app/publish .
# Открываем порт
EXPOSE 80
# Запускаем приложение
ENTRYPOINT ["dotnet", "MyApp.dll"]
var app = WebApplication.Create(args);
// Определяем маршрут для корневого URL
app.MapGet("/", () => "Hello from Docker! Привет из Docker!");
// Запускаем приложение, слушая порт 80 на всех интерфейсах
app.Run("http://*:80");
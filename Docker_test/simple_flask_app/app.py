from flask import Flask

# Создаём экземпляр приложения
app = Flask(__name__)

# Определяем маршрут для главной страницы
@app.route('/')
def hello():
    return "Hello, Docker! Привет из Flask!"

# Эндпоинт для проверки работоспособности (healthcheck)
@app.route('/health')
def health():
    return {"status": "healthy"}, 200

# Запускаем приложение, если файл выполняется напрямую
if __name__ == '__main__':
    # Важно: слушаем на всех интерфейсах (0.0.0.0), чтобы контейнер был доступен снаружи
    app.run(host='0.0.0.0', port=5000, debug=True)
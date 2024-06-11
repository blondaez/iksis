module.exports = {
    proxy: "localhost:8000", // Ваш локальный сервер, например, Django или Flask
    files: ["./**/*.{html,css,js,scss}"], // Файлы, за которыми нужно следить
    port: 3000, // Порт, на котором будет запущен BrowserSync
    open: false, // Не открывать автоматически новый браузер
    notify: false // Отключить уведомления
};

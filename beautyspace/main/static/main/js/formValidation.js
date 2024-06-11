$(document).ready(function() {
    $("signup-form").submit(function(event) {
        var surname = $("#id_surname").val();
        var name = $("#id_name").val();
        var patronymic = $("#id_patronymic").val();
        var phone_number = $("#id_phone_number").val();

        if (surname === "" || name === "" || patronymic === "" || phone_number === "") {
            Swal.fire({
                icon: 'error',
                text: 'Пожалуйста, заполните все поля формы.'
            });
            event.preventDefault();
            return false;
        }

        var namePattern = /^[А-Я][а-яё]*$/;
        if (!namePattern.test(surname) || !namePattern.test(name) || !namePattern.test(patronymic)) {
            Swal.fire({
                icon: 'error',
                text: 'Пожалуйста, корректно заполните поля с фамилией, именем и отчеством.'
            });
            event.preventDefault();
            return false;
        }

        var phonePattern = /^(\+?7|8)-?(\d{10}|\(\d{3}\)\d{3}-?\d{2}-?\d{2}|\d{3}-?\d{3}-?\d{2}-?\d{2})$/;
        if (!phonePattern.test(phone_number)) {
            Swal.fire({
                icon: 'error',
                text: 'Пожалуйста, введите корректный номер телефона.'
            });
            event.preventDefault();
            return false;
        }

        return true;
    });
});

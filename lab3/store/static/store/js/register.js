validateUsername();
validateEmail();
validateName('first');
validateName('last');

function validateUsername() {
    const username = document.getElementById('id_username');
    const usernameRegEx = /^[a-z0-9_]{3,30}$/

    username.addEventListener('input', function () {
        if (username.validity.tooShort) {
            username.setCustomValidity('Username is too short')
        } else if (username.validity.tooLong) {
            username.setCustomValidity('Username is too long')
        } else if (!usernameRegEx.test(username.value)) {
            username.setCustomValidity('Incorrect username')
        } else {
            username.setCustomValidity('')
        }
    })
}

function validateEmail() {
    const email = document.getElementById('id_email');

    email.addEventListener('input', function () {
        if (email.validity.typeMismatch) {
            email.setCustomValidity('Not a valid email address');
        } else {
            email.setCustomValidity('')
        }
    })
}

function validateName(inputId) {
    const name = document.getElementById(`id_${inputId}_name`);
    const nameRegEx = /^[A-Z][a-z]+$/

    name.addEventListener('input', function () {
        if (name.value.trim() !== '') {
            if (!nameRegEx.test(name.value)) {
                name.setCustomValidity(`Invalid ${inputId} name`);
            } else {
                name.setCustomValidity('')
            }
        }
    })
}
function goToLogin() {
    fetch('/login', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            window.location.href = data.redirect;
        })
        .catch(error => console.error('Error:', error));
}

function goToRegister() {
    fetch('/register', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            window.location.href = data.redirect;
        })
        .catch(error => console.error('Error:', error));
}

function submitAnmeldung() {
    var benutzername = document.getElementById('benutzername').value;
    var passwort = document.getElementById('passwort').value;

    $.ajax({
        type: 'POST',
        url: '/check_anmeldung',
        data: { 'benutzername': benutzername, 'passwort': passwort },
        success: function(response) {
            if (response.success) {
                alert(response.message);
                window.location.href = response.redirect;
            } else {
                alert(response.message);
            }
        },
        error: function(error) {
            console.log(error);
        }
    });
}
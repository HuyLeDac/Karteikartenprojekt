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
const form = document.getElementById('post-form');

form.addEventListener('submit', function(event) {

    event.preventDefault();

    const form_data = new FormData(event.target)

    const email = form_data.get('email')
    const password = form_data.get('password')

    if (!email || !password) {
        alert("Os campos 'Email' e 'Password' precisam estar preenchidos!")
        return
    }

    console.log("Email:", email)
    console.log("Password:", password)

})
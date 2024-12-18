document.getElementById('signup-form').addEventListener('submit', async function (e) {
    e.preventDefault(); // Prevent the default form submission

    const full_name = document.getElementById('full_name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const role = document.getElementById('role').value; // Get role from the dropdown

    try {
        const response = await fetch('http://127.0.0.1:8000/api/signup/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                full_name: fullName,   // Check this variable
                email: email,
                password: password,
                role: role
            })
        });
        

        const data = await response.json();
        console.log("DEBUG: Backend Response", data);

        if (response.ok) {
            alert("Signup successful!");
            window.location.href = 'login.html'; // Redirect to login page
        } else {
            alert('Error: ' + data.error);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Something went wrong!');
    }
});
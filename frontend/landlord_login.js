document.getElementById('landlord-login-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('http://127.0.0.1:8000/api/login/landlord/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password, role: 'landlord' }) // Include role
        });

        const data = await response.json();
        console.log('Server Response:', data);

        if (response.ok) {
            alert('Landlord login successful!');
            window.location.href = 'landlord_dashboard.html';
        } else {
            alert(`Error: ${data.error}`);
        }
    } catch (error) {
        console.error('Fetch Error:', error);
        alert('Something went wrong!');
    }
});

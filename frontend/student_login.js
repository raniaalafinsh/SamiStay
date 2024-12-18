document.getElementById('student-login-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('http://127.0.0.1:8000/api/login/student/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password, role: 'student' }) // Include role
        });

        const data = await response.json();
        console.log('Server Response:', response.status, data); // Log response status and data

        if (response.ok) {
            alert('Student login successful!');
            window.location.href = 'student_dashboard.html';
        } else {
            alert(`Error: ${data.error}`); // Display specific error message
        }
    } catch (error) {
        console.error('Fetch Error:', error);
        alert('Something went wrong!'); // Generic error
    }
});

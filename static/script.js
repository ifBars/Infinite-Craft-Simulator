function generateWord() {
    let prompt = document.getElementById('prompt').value.trim();

    if (prompt === '') {
        alert('Please enter a word prompt.');
        return;
    }

    fetch('/generate_word', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'prompt': prompt })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to generate word.');
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('wordResult').innerHTML = '<strong>Generated Word:</strong><br>' + data.word;
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to generate word. Please try again later.');
    });
}

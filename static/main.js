document.addEventListener('DOMContentLoaded', () => {
  // Get the form and the output element
  const form = document.getElementById('form');
  const output = document.getElementById('output');

  // Handle the form submission
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const input = document.getElementById('input').value;

    // Send a POST request to the backend with the input text
    fetch('/api', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ input })
    })
      .then(response => response.json())
      .then((data) => {
        // Display the generated text in the output element
        output.innerHTML = data.output;
      });
  });
});

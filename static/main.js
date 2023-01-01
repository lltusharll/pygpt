document.addEventListener('DOMContentLoaded', () => {
  // Get the form and the output element
  const form = document.getElementById('form');
  const output = document.getElementById('output');

  // Handle the form submission
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const input = document.getElementById('input').value;

    // Send a GET request to the backend with the input text in the query string
    fetch(`/api?input=${input}`, {
      method: 'GET',  // Use the GET method
    })
      .then(response => response.json())
      .then((data) => {
        // Display the generated text in the output element
        output.innerHTML = data.output;
      });
  });
});

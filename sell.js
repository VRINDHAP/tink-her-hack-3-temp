// Get references to the DOM elements
const sellForm = document.getElementById('sellForm');
const sellButton = document.getElementById('sellButton');
const booksList = document.getElementById('books');

// Function to handle the "Sell" button click
sellButton.addEventListener('click', function () {
    // Get input values
    const bookTitle = document.getElementById('bookTitle').value;
    const author = document.getElementById('author').value;
    const genre = document.getElementById('genre').value;
    const price = document.getElementById('price').value;

    // Validate input fields
    if (bookTitle && author && genre && price) {
        // Create a new list item for the book
        const bookItem = document.createElement('li');
        bookItem.textContent = `Title: ${bookTitle}, Author: ${author}, Genre: ${genre}, Price: ${price}`;

        // Add the book to the list
        booksList.appendChild(bookItem);

        // Clear the form
        sellForm.reset();
        alert('Book added to the list for sale!');
    } else {
        alert('Please fill out all the fields.');
    }
});
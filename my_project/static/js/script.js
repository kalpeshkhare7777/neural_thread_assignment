// static/js/script.js
document.addEventListener('DOMContentLoaded', function() {
    // Get the generate button
    var generateBtn = document.querySelector('.btn');

    // Add click event listener to the generate button
    generateBtn.addEventListener('click', function() {
        // Make an AJAX request to the Flask server to execute model.py
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/run_model');
        xhr.send();

        // Refresh the page after a delay of 5 seconds
        setTimeout(function() {
            window.location.href = '/refresh';
        }, 5000); // 5000 milliseconds = 5 seconds
    });
});

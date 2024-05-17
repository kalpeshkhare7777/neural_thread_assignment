// static/js/script.js
document.addEventListener('DOMContentLoaded', function() {
    // Get the generate button
    var generateBtn = document.getElementById('generateBtn');

    // Add click event listener to the generate button
    generateBtn.addEventListener('click', function() {
        // Refresh the page by navigating to the /refresh route


        // After a delay of 0.5 seconds, fetch the image
        setTimeout(function() {
            // Create a new image element
            var img = document.createElement('img');
            
            // Set the src attribute to the generate_butterfly endpoint
            img.src = 'http://127.0.0.1:8000/generate_butterfly';

            // Append the image to the butterflyImage div
            var butterflyImage = document.getElementById('butterflyImage');
            butterflyImage.innerHTML = '';
            butterflyImage.appendChild(img);
        }, 500); // 500 milliseconds = 0.5 seconds
    });
});

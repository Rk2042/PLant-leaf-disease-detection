submitButton.addEventListener('click', function () {
    const file = imageInput.files[0];
    if (file) {
        const formData = new FormData();
        formData.append('image', file);

        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            model1Result.textContent = `Model 1 Prediction: ${data.model1_prediction}`;
            model2Result.textContent = `Model 2 Prediction: ${data.model2_prediction}`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});

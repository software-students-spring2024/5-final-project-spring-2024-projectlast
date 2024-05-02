document.addEventListener('DOMContentLoaded', function() {
    const exerciseForm = document.querySelector('form');
    
    if (exerciseForm) {
        exerciseForm.addEventListener('submit', function(event) {
            const type = document.getElementById('type').value;
            const duration = document.getElementById('duration').value;
            if (type === "" || duration <= 0) {
                event.preventDefault(); // Prevent form submission
                alert('Please enter valid exercise type and duration.');
            } else {
                const confirmSubmit = confirm('Are you sure you want to log this exercise?');
                if (!confirmSubmit) {
                    event.preventDefault(); // Prevent form submission
                }
            }
        });
    }
});

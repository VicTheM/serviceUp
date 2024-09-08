async function updateProfile(method) {
    const form = document.getElementById('editProfileForm');
    const formData = new FormData(form);

    const queryParams = new URLSearchParams();
    formData.forEach((value, key) => {
      if (value) {
        queryParams.append(key, value);
      }
    });

    try {
      const response = await fetch(`/profile/edit?${queryParams.toString()}`, {
        method: method, // POST or PUT based on button clicked
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      // Profile updated successfully, show message and refresh
      showSuccessMessage();

    } catch (error) {
      console.error('Error updating profile:', error);
    }
  }

async function deleteService() {
  const service = document.getElementById('service').value;
  if (!service) {
    alert('Please enter a service to delete.');
    return;
  }

  const queryParams = new URLSearchParams();
  queryParams.append('service', service);

  try {
    const response = await fetch(`/profile/edit?${queryParams.toString()}`, {
      method: 'DELETE',
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    // Service deleted successfully, show message and refresh
    showSuccessMessage();

  } catch (error) {
    console.error('Error deleting service:', error);
  }
}


function showSuccessMessage() {
  const successMessage = document.getElementById('successMessage');
  successMessage.style.display = 'block';

  // Wait for 2 seconds, then refresh the page
  setTimeout(() => {
    location.reload();
  }, 2000);
}

async function hireProfessional(email) {
  try {
    // Send a POST request with the user's email as a query parameter
    const response = await fetch(`/action/hire?email=${encodeURIComponent(email)}`, {
      method: 'POST',
    });

    // Check if the request was successful
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    // Log the response
    const result = await response.json();
    console.log('Hire response:', result);

    // Show the hire message after successful request
    const hireMessage = document.getElementById('hireMessage');
    hireMessage.style.display = 'block';  // Display the success message

  } catch (error) {
    console.error('Error hiring professional:', error);
  }
}
  

async function review(email) {
  // Prevent form submission from reloading the page
  event.preventDefault();

  try {
    // Get the review message from the form
    const reviewMessage = document.getElementById('review').value;

    // Create form data to send with the POST request
    const formData = new FormData();
    formData.append('review', reviewMessage);

    // Send POST request with the email as a query parameter and review message in the body
    const response = await fetch(`/action/review?email=${encodeURIComponent(email)}`, {
      method: 'POST',
      body: formData
    });

    // Check if the request was successful
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    // Log the response (optional)
    const result = await response.json();
    console.log('Review response:', result);

    // Display the success message
    const reviewSuccess = document.getElementById('reviewSuccess');
    reviewSuccess.style.display = 'block';

    // Refresh the page after a short delay (e.g., 1 second)
    setTimeout(() => {
      location.reload();
    }, 2000); // 1 second delay

  } catch (error) {
    console.error('Error submitting review:', error);
  }
}
  
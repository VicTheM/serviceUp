const availableServices = require('./services').availableServices;

console.log(availableServices)

function search(service) {
    return filter(s => s.toLowerCase().includes(service.toLowerCase()));
}

function showSuggestions() {
    let searchInput = document.getElementById('searchInput').value;
    let suggestionsDiv = document.getElementById('suggestions');
    suggestionsDiv.innerHTML = ''; // clear previous suggestions

    if (searchInput) {
        let matches = search(searchInput);
        if (matches.length > 0) {
            suggestionsDiv.style.display = 'block';
            matches.forEach(service => {
                let suggestionItem = document.createElement('div');
                suggestionItem.textContent = service;
                suggestionItem.onclick = function() {
                    document.getElementById('searchInput').value = service;
                    suggestionsDiv.innerHTML = '';
                    suggestionsDiv.style.display = 'none';
                };
                suggestionsDiv.appendChild(suggestionItem);
            });
        } else {
            suggestionsDiv.style.display = 'none';
        }
    } else {
        suggestionsDiv.style.display = 'none';
    }
}

function handleSearch(event) {
    event.preventDefault();
    let searchInput = document.getElementById('searchInput').value;
    let matchedService = find(s => s.toLowerCase() === searchInput.toLowerCase());
    
    if (matchedService) {
        const baseUrl = '/action/search';
        const params = new URLSearchParams({ service: matchedService });
        fetch(`${baseUrl}?${params.toString()}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
        })
        .then(response => response.json())
        .then(users => {
            let resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '';  // Clear any previous results
            users.forEach(user => {
                // Create a link element for each user
                let userLink = document.createElement('a');
                userLink.href = `/profile?email=${user.email}`;
                userLink.textContent = `${user.firstname} ${user.lastname}`;
                
                // Display average stars and a review
                let reviewText = user.reviews.length > 0 ? user.reviews[0] : 'No reviews yet';
                let stars = user.numOfStars / user.numOfReviews || 0;

                let userInfo = document.createElement('div');
                userInfo.innerHTML = `
                    <strong>${userLink.outerHTML}</strong> 
                    <p>Review: ${reviewText}</p>
                    <p>Average Stars: ${stars.toFixed(2)}</p>
                `;

                resultsDiv.appendChild(userInfo);
            });

            // If no users are found
            if (users.length === 0) {
                resultsDiv.innerHTML = '<p>No users found</p>';
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    } else {
        console.log('No match found');
    }
}


function register(form) {
    // Extract form data and perform simple validation
    const registrationType = form["registration-type"].value;
    const firstName = form["firstname"].value.trim();
    const lastName = form["lastname"].value.trim();
    const username = form["username"].value.trim();
    const email = form["email"].value.trim();
    const password = form["password"].value.trim();
    const contact = form["contact"].value.trim();
    const state = form["state"].value.trim();
    const areaOrCity = form["city"].value.trim();
    const lga = form["lga"].value.trim();
    const street = form["street"].value.trim();
    const service = form["service"].value.trim();

    // Simple validation
    if (registrationType === "professional" && (!service || !state || !lga || !street || !areaOrCity || !contact)) {
        alert("Please fill in all required fields.");
        return;
    }

    // Prepare the data object in dictionary form
    const formData = {
        "registration-type": registrationType,
        "firstname": firstName,
        "lastname": lastName,
        "username": username,
        "email": email,
        "password": password,
        "contact": contact,
        "state": state,
        "city": areaOrCity,
        "lga": lga,
        "street": street,
        "service": service
    };

    // Send the data using fetch API
    fetch('/register', {
        method: 'POST'
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error during registration: ' + error.message);
    });
    
}

async function getProfessionalProfile() {
    try {
      const response = await fetch('/profile', {
        method: 'GET'
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      const userProfile = await response.json();
  
      // Do nothing with the userProfile, per the instructions
      // console.log(userProfile);
  
    } catch (error) {
      console.error('Error fetching user profile:', error);
    }
  }
  
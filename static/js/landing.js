let availableServices = [
    'electrician', 'solar-installer', 'braider', 'bricklayer', 'nothing', 'plumber', 'carpenter', 'tailor', 'hair-stylist', 'mechanic',
    'chef', 'gardener', 'cleaner', 'painter', 'mason', 'welder', 'caterer', 'barber', 'make-up-artist', 'fashion-designer', 'interior-designer',
    'event-planner', 'photographer', 'videographer', 'musician', 'dj', 'mc', 'comedian', 'actor', 'actress', 'dancer', 'model', 'writer', 'poet',
    'artist', 'graphic-designer', 'web-designer', 'software-developer', 'app-developer', 'data-scientist', 'data-analyst', 'business-analyst',
    'project-manager', 'product-manager', 'accountant', 'auditor', 'financial-analyst', 'investment-analyst', 'investment-banker', 'stock-broker',
    'insurance-agent', 'insurance-broker', 'real-estate-agent', 'real-estate-broker', 'property-developer', 'civil-engineer', 'mechanical-engineer',
    'electrical-engineer', 'chemical-engineer', 'software-engineer', 'computer-engineer', 'network-engineer', 'security-engineer', 'systems-engineer',
    'biomedical-engineer', 'environmental-engineer', 'aerospace-engineer', 'marine-engineer', 'petroleum-engineer', 'geologist', 'geophysicist', 'geographer',
    'cartographer', 'surveyor', 'urban-planner', 'architect', 'landscape-architect', 'interior-architect', 'structural-engineer', 'quantity-surveyor', 'building-surveyor',
    'land-surveyor', 'town-planner', 'environmental-scientist', 'environmental-consultant', 'environmental-manager', 'environmental-officer', 'environmental-engineer',
    'environmental-technician', 'environmental-analyst', 'environmental-educator', 'environmental-advocate', 'environmental-lobbyist', 'environmental-activist',
    'environmental-entrepreneur', 'environmental-journalist', 'environmental-artist', 'environmental-photographer', 'environmental-filmmaker', 'environmental-consultant', 'environmental-consultant',
    'barber', 'nanny', 'maid', 'house-help', 'driver', 'security-guard', 'grass-cutter', 'painter', 'house-cleaner', 'house-keeper', 'house-maid', 'solar'
];

function search(service) {
    return availableServices.filter(s => s.toLowerCase().includes(service.toLowerCase()));
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
    let matchedService = availableServices.find(s => s.toLowerCase() === searchInput.toLowerCase());
    
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

    // Prepare the form data for URL-encoded format
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

    // Send the data using fetch API with 'application/x-www-form-urlencoded'
    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.text()) // Convert the response to text (HTML)
    .then(html => {
        // Do something with the HTML, like inserting it into the page
        document.body.innerHTML = html; // Example: Replace body content with the HTML
        })
    .catch((error) => {
        console.error('Error:', error); // Handle any errors
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
  };
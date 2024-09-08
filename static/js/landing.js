let availableServices = ['electrician', 'solar-installer', 'braider', 'bricklayer'];

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
        fetch('/action/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ service: matchedService })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data); // handle the search result
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
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.text())  // Get the HTML content as a text response
    .then(html => {
        // Create a new document from the received HTML
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
    
        // Replace the entire document with the new HTML
        document.replaceChild(
            document.adoptNode(doc.documentElement), 
            document.documentElement
        );
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error during registration: ' + error.message);
    });
    
}

function login(form) {
    
}
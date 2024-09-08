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

    form.reset
}

function login(form) {
    
}
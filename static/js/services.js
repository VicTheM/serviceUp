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

serivices = JSON.stringify(availableServices)
serviceArray = JSON.parse(serivices)

exports.availableServices = availableServices;
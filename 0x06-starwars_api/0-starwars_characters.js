const axios = require('axios');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: node 0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

axios.get(apiUrl)
  .then(response => {
    const charactersUrls = response.data.characters;
    const characterPromises = charactersUrls.map(url => axios.get(url));

    return Promise.all(characterPromises);
  })
  .then(characterResponses => {
    const characterNames = characterResponses.map(response => response.data.name);
    characterNames.forEach(name => console.log(name));
  })
  .catch(error => {
    console.error('Error:', error.message);
  });

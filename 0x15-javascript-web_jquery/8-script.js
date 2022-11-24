$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const movieList = data.results;
  for (let i = 0; i < movieList.length; i++) {
    $('UL#list_movies').append($('<li></li>').text(movieList[i].title));
  }
});

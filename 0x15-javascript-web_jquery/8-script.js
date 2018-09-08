url = "https://swapi.co/api/films/?format=json";
$.get(url, function(data){
	$("#list_movies").html(data.results)
	for (movie of data.results) {
	    $("#list_movies").append("<li>" + movie.title + "</li>");
    }
});

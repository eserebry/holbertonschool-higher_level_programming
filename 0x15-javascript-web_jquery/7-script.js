url = "https://swapi.co/api/people/5/?format=json";
$.get(url, function(data){
	$("#character").html(data.name)
});

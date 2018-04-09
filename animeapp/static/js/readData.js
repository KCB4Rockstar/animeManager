$(function (){
	    $.ajax({
        type: "GET",
        url: "/ajax/loadTable/",
        dataType: "json",
        success: function(data) {processData(data);}
    });
})


function processData(data) {
	arr = data.csvData.split("\n");
	var headers = document.getElementById("headers");
	headNames = arr[0].split(",");
	headerString = "<tr>";
	for(var i in headNames){
		headerString+="<td>"+headNames[i]+"</td>";
	}
	headerString+="</tr>";
	headers.innerHTML = headerString;

	arr = arr.slice(1, arr.length);
	var body = document.getElementById('body');


	arr.forEach(function(single_row) {
		var arr = single_row.split(",");
		if(arr.length>=7){
			var genre_arr = arr.slice(2, arr.length - (headNames.length-(2+1)));
			var row = document.createElement("tr");

			var len_genre = genre_arr.length;
			var last_element = genre_arr[len_genre - 1];
			genre_arr[0] = genre_arr[0].slice(1, genre_arr[0].length);
			last_element = last_element.slice(0, last_element.length - 1);
			genre_arr[len_genre - 1] = last_element;
			
			var new_arr = [];
			new_arr.push(arr[0]);
			new_arr.push(arr[1]);
			new_arr.push(genre_arr);
			for (var i = arr.length-(headNames.length-(2+1)); i < arr.length; i++ ) {
				new_arr.push(arr[i]);
			}

			new_arr.forEach(function (element) {
				var data = document.createElement("td");
				if (typeof element === "object") {
					element.forEach(function (sub_elem) {
						data.innerHTML += (sub_elem + "\n");
					})
				} else { data.innerHTML = element; }
				row.appendChild(data);
			})
			body.appendChild(row);
		}
	})
}
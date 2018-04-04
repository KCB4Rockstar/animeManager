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
	arr = arr.slice(1, arr.length);
	arr = arr.slice(0, arr.length - 1);
	var body = document.getElementById('body');


	arr.forEach(function(single_row) {
		var arr = single_row.split(",");
		var genre_arr = arr.slice(2, (arr.length - 4));
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
		for (var i =  arr.length - 4; i < arr.length; i++ ) {
			new_arr.push(arr[i]);
		}

		// console.log(new_arr);

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

	})
}



function next_pos (str, char) {
	pos = str.indexOf(char);
	console.log("First position of \" is " + pos);
	str = str.slice(pos + 1, str.length);

	pos2 = str.indexOf(char);
	console.log("First second of \" is " + pos2);

	console.log(str.slice(0, str.indexOf('"')));

	// console.log("String between character is....");
	// console.log(str.slice(pos, pos2));


	return str.indexOf(char);

}




/*

	information
	

*/
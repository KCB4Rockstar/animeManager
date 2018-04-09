$(function (){
	    $.ajax({
        type: "GET",
        url: "/ajax/loadTable/",
        dataType: "json",
        success: function(data) {processData(data);}
    });
})


function processData(data) {
	csv = data.csvData.split("\n");
	numCols = csv[0].replace(/"/g,"").split(",");

	var headers = document.getElementById("headers");
	headerString = "<tr>";
	for(var i in numCols){
		headerString+="<td>"+numCols[i]+"</td>";
	}
	headerString+="</tr>";
	headers.innerHTML = headerString;

	csv = csv.slice(1, csv.length);
	var body = document.getElementById('body');

	csv.forEach(function(single_row){
		a = [];

		var numFields = (single_row.match(/"/g) || []).length;
		for(var i in single_row){
			if(single_row[i].match(/"/g)){
				a.push(i);
			}
		}

		var new_arr = [];

		if(a[0]==0){
			var firstData = single_row.substring(a[0], a[3]).replace(/"/g,"");
			var genres = single_row.substring(a[3], a[6]).replace(/"/g, "");
			var afterGenre = single_row.substring(a[6], single_row.length).replace(/"/g, "");;

			firstData = firstData.split(",");
			new_arr.push(firstData[0]);
			new_arr.push(firstData[1]);

			genres = genres.substring(1, genres.length-1);
			new_arr.push(genres);

			afterGenre = afterGenre.split(",");
			if(afterGenre.length>6){
				var tempArr = [];
				tempArr.push(afterGenre[0]);
				tempArr.push(afterGenre[1]);
				tempArr.push(afterGenre[2]);
				tempArr.push(afterGenre[3]);

				var photoLink = "";
				for(var i=4;i<afterGenre.length-1;i++){
					photoLink+=afterGenre[i];
				}
				tempArr.push(photoLink);
				tempArr.push(afterGenre[afterGenre.length-1]);

				afterGenre = tempArr;
			}
			for(var i=0;i<afterGenre.length;i++){
				new_arr.push(afterGenre[i]);
			}
		}
		else{
			var arr1 = single_row.replace(/"/g, "").split(",");
			var genre_arr = arr1.slice(2, arr1.length - (numCols.length-(2+1)));
			new_arr.push(arr1[0]);
			new_arr.push(arr1[1]);
			new_arr.push(genre_arr);
			for (var i = arr1.length-(numCols.length-(2+1)); i < arr1.length; i++ ) {
				new_arr.push(arr1[i]);
			}
		}
		


		var rowElement = document.createElement("tr");
		new_arr.forEach(function (element) {
			var data = document.createElement("td");
			data.innerHTML = element;
			rowElement.appendChild(data);
		});
		body.appendChild(rowElement);
	});
}
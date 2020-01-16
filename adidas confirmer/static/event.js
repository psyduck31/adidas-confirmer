async function main() {
	$.get("../api/getEvent", async function (data) {
		data = JSON.parse(data);
		var images = [];
    	for (i = 0; i < data['images'].length; i++)
    	{
    		images.push(data['images'][i]);
    	}
    	await startEvent(images, data['start'])
})
}


async function startEvent(images, startTime) {
	var count = 0;
	for (i = 0; i < Math.floor(images.length/3); i++) {
		$(".event").prepend("<div class='imageBlock'>");
	}
	for (i = 0; i < Math.floor(images.length/3); i++) {
		$(".imageBlock").each(function() {
			$(this).eq(0).append("<img class='eventImage'>");
		})
	}
	/*
	for (i = 0; i < images.length; i++)
	{
		if (count == 0) {
			$(".event").prepend("<div class='imageBlock'>")
		}
		$(".imageBlock").eq(-1).append("<img class='eventImage'>");
		console.log($(".imageBlock").length);
		count += 1;
		if (count == 3) {
			count = 0;
		}
	}
	*/
	$.ajax({
		type: 'POST',
		contentType: 'application/json',
		url: "../api/getImage",
		dataType : 'json',
		data: JSON.stringify({"images": images, "hash": getHash(document.URL.slice(document.URL.indexOf("/event")))}),
		success: async function(data) {
			await sleep(Date.parse(startTime) - Number(Date.now()));
			$(".eventImage").each(function() {
				$( this ).attr({"height": 200, "width": 200, "src": "data:image/jpg;base64," + data['images'].pop()});
			})
		}
	})}


function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}


main();
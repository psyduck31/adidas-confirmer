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
	for (i = 0; i < images.length; i++)
	{
		$(".event").prepend("<img class='eventImage'>");
	}
	$.ajax({
		type: 'POST',
		contentType: 'application/json',
		url: "../api/getImage",
		dataType : 'json',
		data: JSON.stringify({"images": images}),
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
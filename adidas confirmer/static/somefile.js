function getHash(string) {
	string += " " + navigator.userAgent + " " + Date.now()
	var result = '';
		for (i = 0; i < string.length; i++) {
			if (string.charCodeAt(i) - 5 < 20 || string.charCodeAt(i) + 5 > 126) {
				var code = string.charCodeAt(i)
			}
			else { 
				var code = string.charCodeAt(i) - 5;
			}
			code = String.fromCharCode(code);
			result += code;
		}
	console.log(result);
	return result;
}
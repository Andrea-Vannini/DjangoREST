function setAttributes(e, attrs) {
	for(var key in attrs) {
		e.setAttribute(key, attrs[key]);
	}
}

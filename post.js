window.onload = function() {
    var anchors = document.getElementsByTagName("a");
    for (var i = 0; i < anchors.length; i++) {
        var anchor = anchors[i];
        if (anchor.hostname !== window.location.hostname
            || anchor.pathname !== window.location.pathname) {
            anchor.target = "_blank";
	}
    }
};

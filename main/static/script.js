$(document).ready(function(){
    // Function to set body height to window height or document height, whichever is greater
    function setBodyHeight() {
        var windowHeight = $(window).height();
        var documentHeight = $(document).height();
        var newHeight = Math.max(windowHeight, documentHeight);
        $('body').css('height', newHeight + 'px');
    }

    // Call setBodyHeight function on page load
    setBodyHeight();

    // Call setBodyHeight function whenever the window is resized
    $(window).resize(setBodyHeight);
});

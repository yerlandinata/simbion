const newPage = function(page) {
    switchPage(page);
    window.history.pushState(currentPage, page, page);
}

const switchPage = function(page) {
    Array.from($(".simbion-page")).forEach(e => {
        $(e).fadeOut(250);
    });
    console.log(page);
    setTimeout(() => $("#" + page).fadeIn(250), 250);
    currentPage = page;
    document.title = parseTitle(page);
};

const parseTitle = function(str) {
    return str.replace(/\b\w/g, (l) => { return l.toUpperCase() }).replace('-', ' ');
};

const initLinks = function() {
    Array.from(document.getElementsByTagName('a')).forEach(e => {
        console.log(e.getAttribute('href'));
        e.onclick = () => {
            newPage(e.getAttribute('href').substr(1));
            return false;
        };
    });
}

window.onpopstate = function(event) {
    console.log("location: " + document.location + ", state: " + JSON.stringify(event.state));
    switchPage(event.state);
    window.history.replaceState(event.state, event.page, event.state);
};

const showProperPage = function() {
    $("#default-body").addClass('d-none');
    Array.from($(".simbion-page")).forEach(e => {
        $(e).hide();
    });
    $("#great-body").removeClass('d-none');
    initLinks();
    newPage(currentPage);
};

// execute right after page loaded:
showProperPage();

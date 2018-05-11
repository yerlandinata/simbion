const initBody = function() {
    $('#simbion-body').hide();
    $('#simbion-body').removeClass('d-none');
    $('#simbion-body').fadeIn('250');
};

const initSmoothTransition = async function() {
    Array.from(document.getElementsByTagName('a')).forEach(e => {
        e.onclick = () => {
            $('#simbion-body').fadeOut('50');
            setTimeout(() => {
                $('#loading').hide();
                $('#loading').removeClass('d-none');
                $('#loading').fadeIn('50');
                setTimeout(() => window.location.replace(e.href), 500);
            }, 500);
            return false;
        };
    });
};

const sleep = function (ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
};

initBody();
initSmoothTransition();

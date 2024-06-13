console.log('start delete...');
document.addEventListener("DOMContentLoaded", function() {
    var esChrome = /Chrome/.test(navigator.userAgent) && /Google Inc/.test(navigator.vendor);
    var esFirefox = navigator.userAgent.toLowerCase().indexOf('firefox') > -1;
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }
    const csrftoken = getCookie('csrftoken')

    function getDeleteFile(tokenID){
        var data = {
        token: tokenID,
        };

        var xhr = new XMLHttpRequest();
        xhr.open("POST", routerDelete, true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
        xhr.onload = function () {
            if (xhr.status === 200) {
                console.log(xhr.responseText);
                console.log('ejecutado');
            }
        };
        xhr.send(JSON.stringify(data));
    }


    if (esChrome) {
        window.addEventListener('unload', function(event) {
            getDeleteFile(tokenDocument);
        });
    } else if (esFirefox) {
        window.addEventListener('beforeunload', function (event) {
            getDeleteFile(tokenDocument);
        });
    } else {
        window.addEventListener('unload', function(event) {
            getDeleteFile(tokenDocument);
        });
    }

})
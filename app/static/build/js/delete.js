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

    function getDeleteFile(tokenID, name_fileID, formatID){
        var data = {
            token: tokenID,
            name_file: name_fileID,
            format: formatID
        };

        var xhr = new XMLHttpRequest();
        xhr.open("POST", routerDelete, true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
        xhr.onload = function () {
            if (xhr.status === 200) {
                console.log('ejecutado');
            }
        };
        xhr.send(JSON.stringify(data));
    }


    if (esChrome) {
        window.addEventListener('unload', function(event) {
            getDeleteFile(tokenDocument, nameDocument, formatDocument);
        });
    } else if (esFirefox) {
        window.addEventListener('beforeunload', function (event) {
            getDeleteFile(tokenDocument, nameDocument, formatDocument);
        });
    } else {
        window.addEventListener('unload', function(event) {
            getDeleteFile(tokenDocument, nameDocument, formatDocument);
        });
    }

})
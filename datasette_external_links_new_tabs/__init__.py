from datasette import hookimpl

@hookimpl
def extra_body_script():
    return {
        "script": "window.onload = function(){ var a = document.getElementsByTagName('a'); for (var i=0; i<a.length; i++){ if(a[i].hostname != location.hostname) {a[i].setAttribute('target', '_blank'); } } }",
        }
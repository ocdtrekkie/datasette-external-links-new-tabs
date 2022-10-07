from datasette import hookimpl

@hookimpl
def extra_body_script():
    return {
        "script": "window.onload = function(){ var a = document.getElementsByTagName('a'); for (var i=0; i<a.length; i++){ a[i].setAttribute('target', '_blank'); } }",
        }
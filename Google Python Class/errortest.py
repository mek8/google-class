import urllib.request, subprocess

## Given a url, try to retrieve it. If it's text/html,
## print its base url and its text.
def wget(url, filename):
    ufile = urllib.request.urlopen(url)  ## get file-like object for url
    info = ufile.info()   ## meta-info about the url content
    if info.get_content_type() == 'text/html':
        print('base url:' + ufile.geturl())
        text = ufile.readlines()  ## read all its text

    subprocess.call(['touch', filename])
    file_w = open(filename, 'w')
    for t in text:
        file_w.write(str(t))
    file_w.close()

wget('https://developers.google.com/edu/python/', 'htmlfile.html')

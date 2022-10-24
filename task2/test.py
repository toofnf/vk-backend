def app(environ, start_response):
    """Simplest possible application object"""
    data = b'Alya is the best cat! \n She is just love of my life!\n You have seen her earlier in this screencast. \n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])
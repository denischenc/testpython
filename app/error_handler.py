from flask import render_template, jsonify, request

# def page_not_found(e):
#     return render_template('404.html'), 404


def page_not_found(e):
    """A dynamic error handler for 404
       Returns 404.html if the Content-type is not available else returns the json string and a status of 404
    """

    if 'Content-type' in request.headers:
        return jsonify(error=str(e)), 404
    else:
        return render_template('404.html'), 404

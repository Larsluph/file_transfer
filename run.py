"""run flask web server."""

from web_storage import app

if __name__ == '__main__':
    app.run(debug=False, host='larspi.local', port=49550)

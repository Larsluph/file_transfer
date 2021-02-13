"""run flask web server."""

from web_storage import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

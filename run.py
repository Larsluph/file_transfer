"""run flask web server."""

import colorama

from web_storage import app

colorama.init()

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=49550)

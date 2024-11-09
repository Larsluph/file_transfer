"""run flask web server"""

import colorama

from web_storage import app

colorama.init()

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=49550)

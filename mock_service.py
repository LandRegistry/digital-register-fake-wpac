import logging
from flask import Flask
#from flask.ext.api import status

HTTP_200_OK = 200       # Should be status.HTTP_200_OK


app = Flask(__name__)


LOGGER = logging.getLogger(__name__)


@app.route('/wp', methods=['GET', 'POST'])
def fake_wpac():
    """
    Pretend to be WPAC.
    """

    return "", HTTP_200_OK



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)


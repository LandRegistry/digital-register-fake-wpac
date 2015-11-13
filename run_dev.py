from flask.ext.script import Manager
from mock_service import app

port = int(app.config.get('PORT', 8009))
app.run(host='0.0.0.0', port=port, debug=True)

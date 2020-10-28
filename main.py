# Imports
import os
from api import app_3D

# Create the port
port = int(os.environ.get("PORT", 5000))


# Run the app
if __name__ == '__main__':
    app_3D.run('127.0.0.1', port=port, debug=False, threaded=False)


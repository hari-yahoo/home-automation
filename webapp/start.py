import os
from app import create_app

#############################################################
## This one is for testing the app. For deployment use run.py
#############################################################

app = create_app('development')

if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    # This block will only execute in the main process
    print("Starting the application")
else:
    print("Application is running in a worker process")

app.run(debug=True, use_reloader=False )


# entrypoint for Gunicorn on Azure
from app import app           
application = app              

if __name__ == "__main__":
    app.run()

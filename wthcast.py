import os
import app   
from app import create_app 
 
app = create_app(os.getenv('heroku') or "default")
app.config['SECRET_KEY'] = 'qualquercoisa'

if __name__ == "__main__":
    app.run(debug=True)
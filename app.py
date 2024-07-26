from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    from main.routes import main
    from blog.routes import blog
    from media.routes import media
    
    app.register_blueprint(main)
    app.register_blueprint(blog, url_prefix="/blog")
    app.register_blueprint(media, url_prefix="/media")

    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///personal_website.db"
    # db = SQLAlchemy(app)
    # db.init_app(app)

    # from models import ImageCategory, Image
    # db.create_all()

    return app

app = create_app()

db = SQLAlchemy(app)

if __name__ == "__main__":
    from models import ImageTag, Image
    with app.app_context():
        db.create_all()

    app.run(debug=True)
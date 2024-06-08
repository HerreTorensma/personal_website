from flask import Flask

def create_app():
    app = Flask(__name__)

    from main.routes import main
    from blog.routes import blog
    
    app.register_blueprint(main)
    app.register_blueprint(blog, url_prefix="/blog")

    return app

if __name__ == "__main__":
    create_app().run(debug=True)
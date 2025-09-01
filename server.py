from flask import Flask
# from flask_login import LoginManager

def create_app():
    app = Flask(__name__)

    from main.routes import main
    from blog.routes import blog
    from zinc95.routes import zinc95
    
    app.register_blueprint(main)
    app.register_blueprint(blog, url_prefix="/blog")
    app.register_blueprint(zinc95, url_prefix="/zinc95")

    # login_manager = LoginManager()
    # login_manager.init_app(app)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
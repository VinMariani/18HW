# основной файл приложения. здесь конфигурируется фласк,
# сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.movie import movie_ns
from views.director import director_ns
from views.genre import genre_ns


# функция создания основного объекта app
def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def configure_app(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(movie_ns)
    #load_data(application, db)


'''def load_data(application, db):
    with application.app_context():
        pass
        db.create_all()
         создать         несколько        сущностей        чтобы        добавить        их        в        БД
        with db.session.begin():
     db.session.add_all(здесь            список            созданных            объектов)'''


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(debug=True)

from flask_script import Manager
from apps import api_create_app

app = api_create_app()
manager = Manager(app)

if __name__ == '__main__':
    print(app.url_map)
    manager.run()

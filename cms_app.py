from apps import create_app

cms_app = create_app()

if __name__ == '__main__':
    cms_app.run(host='0.0.0.0')

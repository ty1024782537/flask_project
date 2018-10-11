from apps import api_create_app


api_app = api_create_app()


if __name__ == '__main__':

    api_app.run(debug=True, port=8080)

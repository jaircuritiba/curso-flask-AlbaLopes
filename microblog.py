from app import app
import os


if __name__ == '__main__':
    port = int(os.getenv('PORT'), '5000')
    app.run(host='127.0.0.1', port = port)
from app import app, socketio
import nextq_api


if __name__ == '__main__':
    socketio.run(app)
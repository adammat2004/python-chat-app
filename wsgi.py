from app import app, socketio

if __name__ == "__main__":
    socketio.run(app)

#gunicorn and wsgi (web server gateway interface) are both 
# components used in deploying and serving Python web applications, 
# particularly those buily with web frameworks like flask and django
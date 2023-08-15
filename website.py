from flask import Flask, render_template, send_from_directory, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os


app = Flask(__name__, static_folder='static')
app.config['APPLICATION_ROOT'] = "/volume1/Web/website/"
folder_path = "/volume1/Web/website/templates"
# Get the list of files in the folder
files = os.listdir(folder_path)
limiter = Limiter(app=app, key_func=get_remote_address)


def log_requests_to_file():
    log_data = f"{request.remote_addr} - {request.method} {request.url}"
    with open('/volume1/Web/website/requests.log', 'rb') as f:
        try:  # catch OSError in case of a one line file 
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b'\n':
                f.seek(-2, os.SEEK_CUR)
        except OSError:
            f.seek(0)
        last_line = f.readline().decode()
        last_logged_ip = last_line.split(" - ")[0]
    with open('/volume1/Web/website/requests.log', 'a') as f:
        if last_logged_ip != request.remote_addr:
            f.write("\n--------------------------\n")
        f.write(log_data + "\n")

@app.before_request
def log_request():
    try:
        log_requests_to_file()
    except Exception:
        print("Exception writing to file")


# Generate routes based on files
for filename in files:
    # Generate route path from the filename
    route_path = '/' + os.path.splitext(filename)[0]

    # Define a route handler function dynamically
    def route_handler_generator(file_path):
        @limiter.limit("10/minute")
        def route_handler():
            with open(file_path, 'r') as file:
                return file.read()
        return route_handler

    # Create a unique function name for the route handler
    route_handler_name = f'route_handler_{filename}'
    route_handler_function = route_handler_generator(os.path.join(folder_path, filename))
    route_handler_function.__name__ = route_handler_name

    # Register the route with the unique route handler function
    app.route(route_path)(route_handler_function)

@app.route("/")
def hello():
    return render_template('/volume1/Web/website/notice.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

    
if __name__ == "__main__":
    while True:
        try:
            app.run(debug=True,host='0.0.0.0')
        except Exception:
            pass
    
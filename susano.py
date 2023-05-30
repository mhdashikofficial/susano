import os
import subprocess
from flask import Flask
from flask import send_from_directory
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Flask web server
app = Flask(__name__)

# Note
note = "This script is created by Mhd Ashik. Please copy with credits."

# HTML, CSS, JS directory path
dir_path = os.path.dirname(os.path.realpath(__file__))
static_path = os.path.join(dir_path, 'static')

# Serve static files (HTML, CSS, JS)
@app.route('/')
def serve_static():
    return send_from_directory(static_path, 'index.html')

# Ngrok tunnel setup
def setup_ngrok():
    ngrok_path = "/path/to/ngrok"  # Replace with the actual path to your Ngrok binary
    ngrok_command = [ngrok_path, 'http', '8080']
    ngrok_process = subprocess.Popen(ngrok_command, stdout=subprocess.PIPE)
    print("Ngrok URL: ", ngrok_process.stdout.readline().decode().strip())

# Watch for changes in location.txt
class LocationFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == os.path.join(dir_path, 'location.txt'):
            print("Changes detected in location.txt!")
            with open(event.src_path) as file:
                location_data = file.read()
                print(location_data)

# Monitor location.txt changes
def monitor_location_file():
    event_handler = LocationFileHandler()
    observer = Observer()
    observer.schedule(event_handler, dir_path, recursive=False)
    observer.start()
    print("Monitoring location.txt for changes...")

try:
    # Start Flask server
    if __name__ == '__main__':
        setup_ngrok()
        monitor_location_file()
        app.run(host='localhost', port=8080)
except KeyboardInterrupt:
    print("Stopping the script...")

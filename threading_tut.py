import tkinter as tk
import requests
import time
import threading

def send_request():
    time.sleep(10)
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        if response.status_code == 200:
            print(response.json())
        else:
            print(response.status_code)
    except Exception as e:
        print(e)

def start_thread():
    thread = threading.Thread(target=send_request)
    thread.start()

# Create the main window
root = tk.Tk()
root.title("HTTP Request Sender")

# Create a button to send the HTTP request
send_button = tk.Button(root, text="Send HTTP Request", command=start_thread)
send_button.pack(pady=20)
send_button = tk.Button(root, text="Test Button")
send_button.pack(pady=30)

# Start the Tkinter event loop
root.mainloop()

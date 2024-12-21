import threading # For creating multiple threads
import requests # For sending HTTP requests

target_url = "http://127.0.0.1:5000"

def send_requests():
    while True: # Keep sending requests indefinitely
        try:
            response = requests.get(target_url) # Send GET request
            print(f"Request sent: {response.status_code}") # Print
        except Exception as e:
            pass
        
num_threads = 100 # Number of threads to simulate
threads = []
for i in range(num_threads): # Create threads
    thread = threading.Thread(target=send_requests)
    thread.start() # Start each thread
    threads.append(thread)
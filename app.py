# app.py
import requests

def fetch_data():
    response = requests.get('https://api.github.com')
    if response.status_code == 200:
        print("Connected to GitHub API!")
    else:
        print("Failed to connect")

if __name__ == "__main__":
    fetch_data()

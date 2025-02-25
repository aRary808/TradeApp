import webview
import pandas as pd

# Define a simple API to communicate with the frontend
class API:
    def print_csv(self, name):
        return f"Aloha, {name}!"

api = API()

# Open Nuxt.js app in Pywebview
webview.create_window("Nuxt + Pywebview", "http://localhost:3000", js_api=api)
webview.start()
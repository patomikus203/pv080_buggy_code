import sys
import os
import yaml
from flask import request, Response
import logging
import urllib3
import urllib2

app = flask.Flask(__name__)


@app.route("/")
def index():
    version = request.args.get("urllib_version")
    url = request.args.get("url")

    if not url or not version:
        return Response("Missing urllib_version or url parameter", mimetype='text/plain')

    # Sanitize the url input to avoid XSS
    url = sanitize_url(url)
    
    # Fetch the website content
    content = fetch_website(version, url)
    
    if not content:
        return Response("Invalid urllib version specified.", mimetype='text/plain')
    
    return Response(content, mimetype='text/plain')

def sanitize_url(url):
    # Simple sanitization example
    # Ensure the URL is well-formed and only allows specific schemes like http/https
    if not (url.startswith("http://") or url.startswith("https://")):
        raise ValueError("Invalid URL scheme. Only 'http' and 'https' are allowed.")
    return url
        
CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}
class Person(object):
    def __init__(self, name):
        self.name = name


def print_nametag(format_string, person):
    print(format_string.format(person=person))


def fetch_website(urllib_version, url):
    if urllib_version == "2":
        http = urllib2.urlopen(url)
        content = http.read()
        http.close()
    elif urllib_version == "3":
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        content = r.data
    else:
        return "Invalid urllib version specified."
    
    return content


def load_yaml(filename):
    with open(filename, 'r') as stream:
        deserialized_data = yaml.safe_load(stream)  # Use safe_load instead of load
    return deserialized_data
    
def authenticate(password):
    # Avoid using assert statements for production code
    if password == "Iloveyou":
        print("Successfully authenticated!")
    else:
        raise ValueError("Invalid password!")

if __name__ == '__main__':
    print("Vulnerabilities:")
    print("1. Format string vulnerability:")
    print("2. Code injection vulnerability:")
    print("3. Yaml deserialization vulnerability:")
    print("4. Use of assert statements vulnerability:")
    choice  = input("Select vulnerability: ")
    if choice == "1":
        new_person = Person("Vickie")
        print_nametag(input("Please format your nametag: "), new_person)
    elif choice == "2":
        urlib_version = input("Choose version of urllib: ")
        fetch_website(urlib_version, url="https://www.google.com")
    elif choice == "3":
        load_yaml(input("File name: "))
        print("Executed -ls on current folder")
    elif choice == "4":
        password = input("Enter master password: ")
        authenticate(password)


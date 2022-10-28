import requests

class Post:
  URL = 'https://jsonplaceholder.typicode.com/posts'

  def __init__(self):
    result = requests.get(url=self.URL)
    self.posts = result.json()

  def log_posts(self):
    print(self.posts[0]['userId'])
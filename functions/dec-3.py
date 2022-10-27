def my_decorator(fn):
  def wrapper(*args, **kwargs):
    print('start decorator wrapper')
    fn(*args, **kwargs)
    print('stop decorator wrapper')
  return wrapper

@my_decorator
def log(message):
  print(message)

log('message')
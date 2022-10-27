def my_decorator(fn):
  def wrapper():
    print('start decorator wrapper')
    fn()
    print('stop decorator wrapper')
  return wrapper

@my_decorator
def log():
  print('message')

log()

# result = my_decorator(log)
# result()
# my_decorator(log)()
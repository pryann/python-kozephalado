def my_decorator(fn):
  def wrapper():
    print('start decorator wrapper')
    fn()
    print('stop decorator wrapper')
  return wrapper

def log():
  print('message')

# result = my_decorator(log)
# result()

my_decorator(log)()
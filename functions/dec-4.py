def my_decorator(fn):
  def wrapper(*args, **kwargs):
    print('start decorator wrapper')
    print('stop decorator wrapper')
    return fn(*args, **kwargs) * 100
  return wrapper

@my_decorator
def log(a,b):
  return a + b

print(log(10,20))
def my_decorator(*dec_args, **dec_kwargs):
  print(dec_kwargs['inc_value'])
  def inner(fn):
    def wrapper(*args, **kwargs):
      print('start decorator wrapper')
      print('stop decorator wrapper')
      return fn(*args, **kwargs) * dec_kwargs['inc_value']
    return wrapper
  return inner

@my_decorator(inc_value=10)
def log(a,b):
  return a + b

print(log(10,20))
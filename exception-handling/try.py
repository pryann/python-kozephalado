import errno
import sys

# try:
#     name = 'Bob'
#     name += 5
# except:
#     print(sys.exc_info())

# print('end')

# try:
#     name = 'Bob'
#     name += 5
#     # namea += 5
# except (NameError, TypeError) as error:
#     print(error)

# try:
#     name = 'Bob'
#     name += 5
# except NameError as ne:
#     # Code to handle NameError
#     print(ne)
# except TypeError as te:
#     # Code to handle TypeError
#     print(te)

# try:
#     f = open('file.txt')
# except IOError as error:
#     if error.errno == errno.ENOENT:
#         print('File not found')
#     elif error.errno == errno.EACCES:
#         print('Permission denied')
#     else:
#         print(error)


try:
    f = open('demofile.txt', 'r+', encoding='utf-8')
    try:
        f.write(f.read())
    except IOError:
        print(sys.exc_info())
    finally:
        f.close()
except FileNotFoundError:
    print(sys.exc_info())

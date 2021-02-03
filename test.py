import os

webcam_id = [0, 2, 4]
paths = [None] * len(webcam_id)
for i in range(len(webcam_id)):
    paths[i] = os.path.join('/home/wc/Desktop', 'webcam' + str(webcam_id[i]))


print(paths)

# if not os.path.exists(path):    # '/usr/aaa'
try:
    for i in range(len(paths)):
        os.makedirs(paths[i], exist_ok=True)
except OSError:
    print("Can't create destination directory (%s)!" % paths[i])
    home = os.path.expanduser("~")
    path = os.path.join(home, 'unkwon webcam')
    os.makedirs(path, exist_ok=True)
    print(f"Default path will be used: {path}")

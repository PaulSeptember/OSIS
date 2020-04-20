import os

path = "/homse/user/sublime_text_3" 
fSTuple = []
lS = 0
p = path.split("//")
if (os.path.isdir("/" + p[0])== False):
       print("Disk does not exists")
for root, dirs, files in os.walk(path):
    for file in files:
        fSTuple.append((file, os.path.getsize(os.path.join(root, file))))
try: 
    for fileName, fS in fSTuple:
        if fS > lS:
            lS = fS
            ans = fileName
    print("Result:   ",ans, lS, "b")
except:
	print("Path does not exist.")
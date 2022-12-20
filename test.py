import os 

def main(length= 10, name="blaize"):
    if os.path.exists(name):
        os.remove(name)
    os.mkdir(name)
    for i in range(0, length):
        with open(name + "/%d.txt" % i, "w") as f:
            f.write("hello")
            f.write("\n")
            f.write("world")
            f.write("\n")
            f.write("hello")
            f.write("\n")
            f.write("world")
            f.write("\n")
            f.write("hello")
            f.write("\n")
        with open(name + "/%d.txt" % i, "r") as f:
            f.seek(0)
        f.truncate()
        f.close()
    os.rmdir(name)
    os.mkdir(name)
    for i in range(0, length):
        with open(name + "/%d.txt" % i, "w") as f:
            f.write("hello")
            f.write("\n")
            f.write("world")
            f.write("\n")
            f.write("hello")
            f.write("\n")
    main(length,name)
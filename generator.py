import os

rootdir = "."
header = []
footer = []

with open("header", "r") as f:
    header = f.readlines()
    
with open("footer", "r") as f:
    footer = f.readlines()

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".htm"):
            base = os.path.basename(filepath)
            print(os.path.splitext(base)[0] + ".html")

            with open(filepath, "r") as f:
                print("".join(header + f.readlines() + footer))
                # tf = open(os.path.splitext(base)[0] + ".html", "w+")
                # tf.write("".join(header + f.readlines() + footer))
                # tf.close()
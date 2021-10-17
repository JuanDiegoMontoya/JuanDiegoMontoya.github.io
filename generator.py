# This script generates html files.
# It first reads the files "header" and "footer" in its current directory.
# Next, it recursively traverses the current tree for any file
# with the extension '.htm' (which indicates an "unfinished" html file
# for the purposes of this script). Then, the header and footer are
# pre- and post-pended to the current file's contents. The result
# is written to a new file in the current directory with the extension '.html'.

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
                #print("".join(header + f.readlines() + footer))
                tf = open(os.path.splitext(base)[0] + ".html", "w+")
                tf.write("".join(header + f.readlines() + footer))
                tf.close()
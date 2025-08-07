import os,shutil
for f in os.listdir("."):
    if f.startswith("äus1_"):
        shutil.copy2(f, "aeusgasthaus1.jpeg")
        print("Copied", f, "to aeusgasthaus1.jpeg")
    elif f.startswith("äus4_"):
        shutil.copy2(f, "aeusgasthaus4.jpeg")
        print("Copied", f, "to aeusgasthaus4.jpeg")

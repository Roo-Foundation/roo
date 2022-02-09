import os

t = """
# roo
Images of roo
"""
for roo in os.listdir("./roos"):
    roo = roo.split(".")[0]
    t += f'\n\n\n### {roo}\n<img src="https://raw.githubusercontent.com/Roo-Foundation/roo/main/roos/{roo}.png" width="130" height="130">'


with open("README.md", "w") as f:
    f.write(t)

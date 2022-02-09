import os

t = """
# roo
Images of roo
"""

for roo in os.listdir("./roos"):
    roo_name = roo.split(".")[0]
    t += f'\n\n\n### {roo_name}\n<img src="https://raw.githubusercontent.com/Roo-Foundation/roo/main/roos/{roo}" width="130" height="130">'
    print(f"Updated {roo}")

with open("README.md", "w") as f:
    f.write(t)

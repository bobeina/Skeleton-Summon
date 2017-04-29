# coding=utf8

u"""
Summon a skeleton (project) in book 'learn python hard way' automatically by asking you a few questions. It's too boring to create it manually.

The new skeleton you summon will appear in the same directory with this scroll.

ver 0.1 by a crazy necromancer (minvacai@sina.com)
2017/4/29
"""

import os
import sys

version = sys.version_info

info = {
    'description': 'MyProject',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': 'NAME',
    'scripts': [],
    'name': 'projectname'
}

if version.major ==2:
    lst = info.keys()
else:
    lst = list(info)

ignore_list = [
    "scripts",
    "install_requires",
    "version"
]
elelst = []
for ele in lst:
    if ele not in ignore_list:
        elelst.append(ele)

print("Python %d.%d.%d detected. \nPress Ctrl+Z to quit.\n" % (version.major, version.minor, version.micro))

for w in elelst:
    raw = ""
    while(raw.strip() == ""):
        text = u"Project {0}(default: '{1}'): ".format(w, info[w])
        raw = raw_input(text)
        if raw.strip() == "":
            break
        else:
            info[w] = raw

# mkdir project_name
path = info['name']
if os.path.exists(path) == False:
    os.mkdir(path)
else:
    print("Directory %s exists. Quit." % info['name'])
    sys.exit(2)

# mkdir bin source_dir tests docs
os.mkdir(path + '/bin')
os.mkdir(path + '/tests')
os.mkdir(path + '/docs')
source_dir = path + '/' + info['packages']
os.mkdir(source_dir)

# touch source_dir/__init__.py
f = file(source_dir + '/__init__.py', 'w')
f.write('\n')
f.close()

# touch tests/__init__.py
tests_dir = path + '/tests'
f = file(tests_dir + '/__init__.py', 'w')
f.write('\n')
f.close()

# create setup.py:
setup_str = """
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {{
    'description': '{0}',
    'author': '{1}',
    'url':  '{2}',
    'download_url': '{3}',
    'author_email': '{4}',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['{5}'],
    'scripts': [],
    'name': '{6}'
}}

setup(**config)
""".format(
    info['description'],
    info['author'],
    info['url'],
    info['download_url'],
    info['author_email'],
    info['packages'],
    info['name']
)

lines = setup_str.split('\n')
f = file(path + '/setup.py', 'w')
#f.writelines(lines)
f.write(setup_str)
f.close()

print("done.")

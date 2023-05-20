import os
import sys
import shutil
import json

tl_output = 'output'
web_output = 'dist'
if len(sys.argv) > 1:
  tl_output = sys.argv[1]
if len(sys.argv) > 2:
  web_output = sys.argv[2]
  
tl_path = os.path.join(os.getcwd(), tl_output)
web_path = os.path.join(os.getcwd(), web_output)
  
if not os.path.exists(tl_path):
  print(f'{tl_path} does not exist')
  exit()

shutil.copytree(tl_path, web_path, dirs_exist_ok=True)
shutil.copyfile('novels.html', os.path.join(web_path, 'index.html'))

sitemap = {}
for file in os.listdir(web_path):
  f = os.path.join(web_path, file)
  if os.path.isdir(f):
    sitemap[file] = '' # metadata can be added here(like chapter #)
    shutil.copyfile('chapters.html', os.path.join(f, 'index.html'))

sitemap_json = json.dumps(sitemap, indent=4)
with open(os.path.join(web_path, 'sitemap.json'), 'w') as outfile:
  outfile.write(sitemap_json)
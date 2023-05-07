import configparser
import os

from translate import Translator
from novel import Novel
import novels.example

def main():
  parser = configparser.ConfigParser()
  parser.read('config.ini')
  print(parser.sections())
  openai = dict(parser.items('openai'))
  print(openai)

  translator = Translator(openai)
  name='Test Novel'
  test_novel = Novel(name, 2, novels.example.get_next, translator, True)
  chapters=[]
  path = os.path.join(os.getcwd(), 'output', name)
  if not os.path.exists(path):
    os.makedirs(path)
  chap = test_novel.next_chapter()
  while chap is not None:
    chapters.append(chap)
    chap = test_novel.next_chapter()
  for i,chapter in enumerate(chapters):
    file = open(f'output/{name}/{i+1}.txt', 'w')
    file.write(chapter)
    file.close()
  
if __name__ == "__main__":
    main()
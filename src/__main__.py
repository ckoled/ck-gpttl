import os

from config import config
from novel import Novel
from translate import Translator
import novels.example

def main():
  print(config.openai)

  name = novels.example.name
  translator = Translator(config.openai)
  test_novel = Novel(novels.example, translator, split_chapter=True)
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
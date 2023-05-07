import configparser

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
  test_novel = Novel('Test Novel', 2, novels.example.get_next, translator, True)
  chapters=[]
  chap = test_novel.next_chapter()
  while chap is not None:
    chapters.append(chap)
    chap = test_novel.next_chapter()
  for i,chapter in enumerate(chapters):
    print(f'Chapter {i}')
    print(chapter)
  
if __name__ == "__main__":
    main()
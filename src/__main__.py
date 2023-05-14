from config import config
from novel import Novel
from translate import Translator
import novels.example

def main():
  print(config.openai)
  
  translator = Translator(config.openai)
  
  test_novel = Novel(novels.example, translator, split_chapter=True)
  test_novel.tl_novel(num=1)
  
if __name__ == "__main__":
    main()
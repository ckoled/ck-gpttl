import time

from config import config
from novel import Novel
from translate import Translator
import novels.example

def main():
  print(config.openai)
  t_start = time.perf_counter()
  
  translator = Translator(config.openai)
  
  test_novel = Novel(novels.example, translator, split_chapter=True)
  test_novel.tl_novel(num=1)

  print(f'Total Tokens: {translator.api.total_tokens}')
  print(f'Completed in {time.perf_counter()-t_start:0.4f}')
  
if __name__ == "__main__":
    main()
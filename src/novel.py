from helpers import split

class Novel:
  summary=''
  
  def __init__(self, novel_info, translator, current=1, split_chapter=False, split_length=1500) -> None:
    self.novel_info = novel_info
    self.translator = translator
    self.current = current
    self.split_chapter = split_chapter
    self.split_length = split_length
    
  def tl_chapter(self, chapter):
    raw = self.novel_info.get_chap(chapter)
    text = ''
    if self.split_chapter:
      sections = split(raw, self.split_length)
      section_summary = ''
      for section in sections:
        section_text = self.translator.translate(section, f'{self.summary} {section_summary}')
        section_summary = self.translator.summarize(section_text)
        text = f'{text}\n{section_text}'
    else:
      text = self.translator.translate(raw, self.summary)
    self.summary = self.translator.summarize(text)
    return text
  
  def next_chapter(self):
    if self.current > self.novel_info.total_chapters:
      return None
    text = self.tl_chapter(self.current)
    self.current += 1
    return text
  
  
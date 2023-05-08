from translate import translator

class Novel:
  summary=''
  current=1
  
  def __init__(self, name, chapters, get_next, split_chapter=False) -> None:
    self.name = name
    self.chapters = chapters
    self.get_next = get_next
    self.split_chapter = split_chapter
    
  def split(self, raw, length):
    sections = []
    lines = raw.split('\n')
    section = ''
    for line in lines:
      section = section + line
      if len(section) > length:
        sections.append(section)
        section = ''
    return sections
    
  def next_chapter(self):
    if (self.current > self.chapters):
      print('No more chapters')
      return None
    raw = self.get_next(self.current)
    text = ''
    if self.split_chapter:
      sections = self.split(raw, 1500)
      section_summary = ''
      for section in sections:
        section_text = translator.translate(section, f'{self.summary} {section_summary}')
        section_summary = translator.summarize(section_text)
        text = f'{text}\n{section_text}'
    else:
      text = translator.translate(raw, self.summary)
    self.summary = translator.summarize(text)
    self.current = self.current+1
    return text
  
  
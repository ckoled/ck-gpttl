def clean(raw):
  raw = raw.replace('\u3000', '\n')
  return raw

def recode(text):
  return text.encode('ascii', 'ignore').decode()

def split(raw, length):
    sections = []
    lines = raw.split('\n')
    section = ''
    for line in lines:
      if not line:
        continue
      section = section + line + '\n'
      if len(section) > length:
        sections.append(section)
        section = ''
    sections.append(section)
    return sections
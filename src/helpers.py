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
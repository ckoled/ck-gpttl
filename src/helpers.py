def split(raw, length):
    sections = []
    raw = raw.replace('\u3000', '\n')
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
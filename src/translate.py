from api import Api

class Translator:
  def __init__(self, config) -> None:
    self.api = Api(config)

  def translate(self, raw, summary, prompt='Any text before this is a summary of the previous chapters. Translate the following into english. Do not uneccesarily remove sentences. Your response should only contain the translated text.'):
    message = f'''{summary}
    {prompt}
    {raw}'''
    
    return self.api.call(message)
    
  def summarize(self, text):
    message = f'''Summarize the following. Make sure to include names of places, people, things. Your response should only contain the summary and not be over 5 sentences.
    {text}'''
    
    return self.api.call(message)
  
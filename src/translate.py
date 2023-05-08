from api import api

class _Translator:
  def translate(self, raw, summary, prompt='Any text before this is a summary of the previous chapters. Translate the following into english. Do not uneccesarily remove sentences. Your response should only contain the translated text.'):
    message = f'''{summary}
    {prompt}
    {raw}'''
    
    return api.call(message)
    
  def summarize(self, text):
    message = f'''Summarize the following. Make sure to include names of places, people, things. Your response should only contain the summary and not be over 5 sentences.
    {text}'''
    
    return api.call(message)
  
translator = _Translator()
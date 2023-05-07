import openai

class Translator:
  model=''
  calls=0
  
  def __init__(self, config):
    openai.organization = config['org']
    openai.api_key = config['key']
    self.model = config['model']
    
  def call(self, message):
    try:
      self.calls = self.calls+1
      print(f'Call: {self.calls}')
      print(f'Prompt: {message}')
      response = openai.ChatCompletion.create(
        model=self.model,
        messages=[{
          'role': 'user',
          'content': message,
        }]
      )
      print(f'Response: {response}')
      return response.choices[0].message.content
    except Exception as e:
      print(f'OpenAI call failed: {e}')
      raise e
    
  def translate(self, raw, summary, prompt='Any text before this is a summary of the previous chapters. Translate the following into english. Do not uneccesarily remove sentences. Your response should only contain the translated text.'):
    message = f'''{summary}
    {prompt}
    {raw}'''
    
    return self.call(message)
    
  def summarize(self, text):
    message = f'''Summarize the following. Make sure to include names of places, people, things. Your response should only contain the summary and not be over 5 sentences.
    {text}'''
    
    return self.call(message)
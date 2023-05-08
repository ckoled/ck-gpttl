import openai

from config import config

class _Api:
  model=''
  calls=0
  retries=3
  
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
      if self.retries > 0:
        self.retries = self.retries-1
        return self.call(message)
      raise e

api = _Api(config.openai)
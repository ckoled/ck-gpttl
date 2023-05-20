import openai

class Api:
  model=''
  calls=0
  total_tokens=0
  
  def __init__(self, config, retries=1):
    openai.organization = config['org']
    openai.api_key = config['key']
    self.model = config['model']
    self.retries = retries
    
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
      self.total_tokens += response.usage.total_tokens
      print(f'Accumulated Tokens: {self.total_tokens}')
      return response.choices[0].message.content
    except Exception as e:
      print(f'OpenAI call failed: {e}')
      if self.retries > 0:
        self.retries -= 1
        return self.call(message)
      raise e

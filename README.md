# ck-gpttl

This is a tool designed to translate novels to english. It uses openai's gpt models to achieve passable chinese, korean, or japanese translation.

Check out [gptwntranslator](https://github.com/combobulativedesigns/gptwntranslator) for the idea of using summaries for memory (and its just better than mine).

## Usage

1. create python file for each novel under src/novels
2. add to src/main
3. run `python src/__main__.py`
4. run `python -m http.serve` from output directory to see web version

## TODO

- gpt4
- add split/token logic
- better memory
- easy to launch web server/cloud upload(s3)
- improved memory with some database*
- auto publish/public site*
- scraping builder/user submitted novels*

*if I go crazy

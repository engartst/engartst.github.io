from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from json import load
import fnmatch, glob, os, os.path

file_list = []
dir_list = []

template_env = Environment(loader=FileSystemLoader(searchpath='.'))
template = template_env.get_template('piece_template.html')

for root, dirs, files in os.walk('./works/'):
    for di in dirs:
        dir_list.append(os.path.join(root,di))
    for file in files:
        file_list.append(os.path.join(root,file))



for file in file_list:
    if file.endswith(".md"):
        with open(f'{file}', 'r') as markdown_file:
            article = markdown(markdown_file.read(),
            extras=['fenced=code=blocks', 'code-friendly'])

            _folder = file.rpartition("/")

            # check for pdf
            pdf=_folder[2][:-3]+"ENGART.pdf"
            score = file[:-3]+"ENGART.pdf"
            score_exists = os.path.exists(score)

            # check for mp3
            mp3=_folder[2][:-3]+"ENGART.mp3"
            audio = file[:-3]+"ENGART.mp3"
            audio_exists = os.path.exists(audio)

            with open(f'{_folder[0]}/config.json', 'r') as config_file:
                config = load(config_file)

            with open(f'{_folder[0]}/index.html', 'w') as output_file:
                output_file.write(
                    template.render(
                        article=article,
                        instrumentation=config['instrumentation'],
                        year=config['year'],
                        duration=config['duration'],
                        title=config['title'],
                        score_exists=score_exists,
                        score=pdf,
                        audio_exists=audio_exists,
                        audio=mp3
                    )
                )

from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from json import load
import fnmatch, glob, os, os.path, re

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

            # check for png
            png =_folder[2][:-3]+"ENGART.png"
            pic = file[:-3]+"ENGART.png"
            pic_exists = os.path.exists(pic)

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
                        audio=mp3,
                        pic_exists=pic_exists,
                        pic=png
                    )
                )

recipe_dir_list = []
recipe_file_list = []
recipe_list = []

#template_env = Environment(loader=FileSystemLoader(searchpath='.'))
recipe_template = template_env.get_template('recipe_template.html')

for root, dirs, files in os.walk('./recipes/'):
    for di in dirs:
        recipe_dir_list.append(os.path.join(root,di))
    for file in files:
        recipe_file_list.append(os.path.join(root,file))


for file in recipe_file_list:
    if file.endswith(".md"):
        with open(f'{file}', 'r') as markdown_file:
            article = markdown(markdown_file.read())
            title = file.split('/')
            title = title[-1]
            title = title.split('.')[0]
            recipe_list.append(title)
            with open(f'{file[:-3]}.html', 'w') as output_file:
                output_file.write(
                    recipe_template.render(
                        article=article,
                        title=title
                    )
                )


recipe_list_template = template_env.get_template('recipe_list_template.html')

recipe_len = len(recipe_list)
recipe_list.sort()
list_list = []

for i in recipe_list:
    i = re.sub('([A-Z])', r' \1', i)
    list_list.append(i.title())

zip_list = zip(list_list, recipe_list)

with open('recipes.html', 'w') as output_file:
    output_file.write(
        recipe_list_template.render(
            recipe_list = recipe_list,
            recipe_len = recipe_len,
            list_list = zip_list
        )
    )

# MEDIA PLAY
mp_dir_list = []
mp_file_list = []
mp_list = []
mpl = []

mp_note_template = template_env.get_template('mp_note_temp.html')

for root, dirs, files in os.walk('./mediaPlay/notes/'):
    for di in dirs:
        mp_dir_list.append(os.path.join(root,di))
    for file in files:
        mp_file_list.append(os.path.join(root,file))


for file in mp_file_list:
    if file.endswith(".md"):
        with open(f'{file}', 'r') as markdown_file:
            article = markdown(markdown_file.read())
            title = file.split('/')
            title = title[-1]
            title = title.split('.')[0]
            mpl.append(title)
            with open(f'{file[:-3]}.html', 'w') as output_file:
                output_file.write(
                    mp_note_template.render(
                        article=article,
                        title=title
                    )
                )


mp_piece_dir_list = []
mp_piece_file_list = []
mppl = []

for root, dirs, files in os.walk('./mediaPlay/pieces/'):
    for di in dirs:
        mp_piece_dir_list.append(os.path.join(root,di))
    for file in files:
        mp_piece_file_list.append(os.path.join(root,file))
        mppl.append(file.rsplit('.', 1)[0])

mp_piece_list = mp_piece_file_list
mp_list_template = template_env.get_template('mp_note_list_temp.html')

mp_len = len(mp_list)
mp_list.sort()
mp_piece_len = len(mp_piece_list)
mp_piece_list.sort()
list_list = []
piece_list_list = []
x = []
y = []

for i in mp_list:
    mpl.append(i.rsplit('/', 1)[-1])

for i in mp_file_list:
    x.append(i.rsplit('Play/', 1)[1])

for i in mp_piece_file_list:
    y.append(i.rsplit('Play/',1)[1])

x.sort()
y.sort()
zip_list = zip(mpl, x)
piece_list = zip(mppl, y)

with open('./mediaPlay/index.html', 'w') as output_file:
    output_file.write(
        mp_list_template.render(
            mp_list = mp_list,
            mp_len = mp_len,
            list_list = zip_list,
            piece_list = piece_list
        )
    )


import os
import re
import json
from pathlib import Path
from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Security: Define allowed file extensions
ALLOWED_EXTENSIONS = {'.md', '.json', '.html'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB limit

# Constants
MEDIA_SUFFIXES = ["ENGART.pdf", "ENGART.mp3", "ENGART.png"]
TEMPLATE_PATH = "."
WORKS_DIR = "./works/"
RECIPES_DIR = "./recipes/"
MEDIA_NOTES_DIR = "./mediaPlay/notes/"
MEDIA_PIECES_DIR = "./mediaPlay/pieces/"

# Setup Jinja2
template_env = Environment(loader=FileSystemLoader(searchpath=TEMPLATE_PATH))


def collect_files_and_dirs(path):
    dir_list, file_list = [], []
    for root, dirs, files in os.walk(path):
        for d in dirs:
            dir_list.append(os.path.join(root, d))
        for f in files:
            file_list.append(os.path.join(root, f))
    return dir_list, file_list


def check_media_assets(base_path):
    assets = {}
    for suffix in MEDIA_SUFFIXES:
        filename = base_path + suffix
        assets[suffix] = os.path.exists(filename)
    return assets


def validate_file_path(file_path):
    """Validate file path for security"""
    path = Path(file_path)
    
    # Check if file exists and is within allowed directories
    if not path.exists():
        raise ValueError(f"File does not exist: {file_path}")
    
    # Check file extension
    if path.suffix not in ALLOWED_EXTENSIONS:
        raise ValueError(f"File extension not allowed: {path.suffix}")
    
    # Check file size
    if path.stat().st_size > MAX_FILE_SIZE:
        raise ValueError(f"File too large: {file_path}")
    
    # Prevent directory traversal
    if '..' in str(path) or str(path).startswith('/'):
        raise ValueError(f"Invalid file path: {file_path}")
    
    return path

def render_markdown_to_html(md_file_path, output_path, template, **kwargs):
    try:
        # Validate input paths
        md_path = validate_file_path(md_file_path)
        
        with open(md_path, "r", encoding='utf-8') as f:
            content = f.read()
            # Security: Limit content size
            if len(content) > MAX_FILE_SIZE:
                raise ValueError("Content too large")
            article = markdown(content, extras=["fenced-code-blocks", "code-friendly"])
        
        # Validate output path
        output_dir = Path(output_path).parent
        output_dir.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, "w", encoding='utf-8') as f:
            f.write(template.render(article=article, **kwargs))
        
        logger.info(f"Successfully processed: {md_file_path} -> {output_path}")
        
    except Exception as e:
        logger.error(f"Error processing {md_file_path}: {e}")
        raise


# === Works Section ===
_, file_list = collect_files_and_dirs(WORKS_DIR)
piece_template = template_env.get_template("piece_template.html")

for file in file_list:
    if file.endswith(".md"):
        folder = os.path.dirname(file)
        base_name = os.path.splitext(os.path.basename(file))[0]

        media_assets = check_media_assets(file[:-3])

        config_path = os.path.join(folder, "config.json")
        try:
            validate_file_path(config_path)
            with open(config_path, "r", encoding='utf-8') as config_file:
                config = json.load(config_file)
            
            # Validate config structure
            required_keys = ['title', 'instrumentation', 'year', 'duration']
            for key in required_keys:
                if key not in config:
                    logger.warning(f"Missing required key '{key}' in {config_path}")
                    config[key] = ''
                    
        except (FileNotFoundError, ValueError) as e:
            logger.error(f"Config file error {config_path}: {e}")
            continue

        output_path = os.path.join(folder, "index.html")
        try:
            with open(file, "r") as markdown_file:
                article = markdown(
                    markdown_file.read(), extras=["fenced-code-blocks", "code-friendly"]
                )
            with open(output_path, "w") as output_file:
                output_file.write(
                    piece_template.render(
                        article=article,
                        instrumentation=config.get("instrumentation", ""),
                        year=config.get("year", ""),
                        duration=config.get("duration", ""),
                        title=config.get("title", ""),
                        score_exists=media_assets["ENGART.pdf"],
                        score=base_name + "ENGART.pdf",
                        audio_exists=media_assets["ENGART.mp3"],
                        audio=base_name + "ENGART.mp3",
                        pic_exists=media_assets["ENGART.png"],
                        pic=base_name + "ENGART.png",
                    )
                )
        except Exception as e:
            print(f"Failed to render article: {file} due to {e}")

# === Recipes Section ===
_, recipe_files = collect_files_and_dirs(RECIPES_DIR)
recipe_template = template_env.get_template("recipe_template.html")
recipe_list = []

for file in recipe_files:
    if file.endswith(".md"):
        title = os.path.splitext(os.path.basename(file))[0]
        recipe_list.append(title)
        render_markdown_to_html(file, f"{file[:-3]}.html", recipe_template, title=title)

recipe_list_template = template_env.get_template("recipe_list_template.html")
list_list = [re.sub(r"(?<!^)([A-Z])", r" \1", name).title() for name in recipe_list]
zip_list = zip(sorted(list_list), sorted(recipe_list))

with open("recipes.html", "w") as output_file:
    output_file.write(
        recipe_list_template.render(
            recipe_list=sorted(recipe_list),
            recipe_len=len(recipe_list),
            list_list=zip_list,
        )
    )

# === MediaPlay Notes Section ===
_, mp_note_files = collect_files_and_dirs(MEDIA_NOTES_DIR)
mp_note_template = template_env.get_template("mp_note_temp.html")
media_note_titles = []

for file in mp_note_files:
    if file.endswith(".md"):
        title = os.path.splitext(os.path.basename(file))[0]
        media_note_titles.append(title)
        render_markdown_to_html(
            file, f"{file[:-3]}.html", mp_note_template, title=title
        )

# === MediaPlay Pieces Section ===
_, mp_piece_files = collect_files_and_dirs(MEDIA_PIECES_DIR)
mp_piece_titles = [os.path.splitext(os.path.basename(f))[0] for f in mp_piece_files]

x = [f.split("Play/", 1)[-1] for f in mp_note_files]
y = [f.split("Play/", 1)[-1] for f in mp_piece_files]

media_note_titles.sort()
mp_piece_titles.sort()
zip_notes = zip(media_note_titles, x)
zip_pieces = zip(mp_piece_titles, y)

mp_list_template = template_env.get_template("mp_note_list_temp.html")
with open("./mediaPlay/index.html", "w") as output_file:
    output_file.write(
        mp_list_template.render(
            mp_list=media_note_titles,
            mp_len=len(media_note_titles),
            list_list=zip_notes,
            piece_list=zip_pieces,
        )
    )

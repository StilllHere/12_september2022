from flask import Blueprint, render_template, request
import logging
from functions import post_text_add, safe_pic
from json import JSONDecodeError

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

@loader_blueprint.route("/post")
def page_post_form():
    return render_template('post_form.html')

@loader_blueprint.route("/post", methods = ["POST"])
def page_post_uploaded():
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    picture = request.files.get('picture')
    content = request.form.get('content')
    if not picture or not content:
        return'ошибка загрузки'
    extension = picture.filename.split('.')[-1]
    if extension not in ALLOWED_EXTENSIONS:
        logging.info('Файл не картинка')
        return 'Расширение не то'
    try:
        path_pic: str = safe_pic(picture)
        new_post= post_text_add({'pic': path_pic,'content': content})
        return render_template('post_uploaded.html', post=new_post)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return "Файл не найден"
    except JSONDecodeError:
        return "Не превращается в список"





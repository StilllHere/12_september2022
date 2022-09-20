import json
from flask import request

def read_file():
    """
    Чтение из файла
    """
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_word(word):
    """
    Поиск постов
    """
    result =[]
    for post in read_file():
        if word.lower() in post['content'].lower():
           result.append(post)
    return result

def safe_pic(picture):
    """
    Сохранение картинок
    """
    picture = request.files.get("picture")
    filename = picture.filename
    picture.save(f"./uploads/images/{filename}")
    return f"./uploads/images/{filename}"

def post_text_add(post):
    """
    Сохранение постов
    """
    posts = read_file()
    posts.append(post)
    with open('posts.json','w', encoding='utf-8') as f:
        json.dump(posts, f)
    return posts
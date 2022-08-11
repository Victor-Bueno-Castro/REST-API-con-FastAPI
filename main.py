from fastapi import FastAPI #   Importación de FastAPI
from pydantic import BaseModel  #   Librería para creación de modelos
from typing import Text, Optional #   Para creación de textos largos y campos opcionales
from datetime import datetime   #   Generación de las fechas
from uuid import uuid4 as uuid  #   Genera el id por default
from fastapi import HTTPException   #   Para validar errores por HTTP

app = FastAPI(title='Rest-API', 
              description='API - Test', 
              version = '1.0.1') #   Instancia de FastAPI

posts = []  #   Lista vacía para guardar datos

#   Para modelos   
class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False

#   Decorador o método GET
@app.get('/')   #   Raíz principal
def read_root():
    return {'Welcome: Welcome to my REST-API'}

@app.get('/posts')
def get_posts():
    return posts    #   Retorna la lista

#   Decorador o método POST
@app.post('/posts')
def save_posts(post: Post):
    post.id = str(uuid())
    posts.append(post.dict())  #    Agrega los datos a la lista vacía
    return posts[-1]    #   Retorna el ultimo dato

#   Obtener un dato mediante su id
@app.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail='Post Not Found')
    
#   Eliminar un elemento
@app.delete('/posts/{post_id}')
def delete_post(post_id: str):
    for index, post in enumerate(posts):    #   Recorre el índice y la publicación para ser eliminadas
        if post['id'] == post_id:
            posts.pop(index) #   elimina
            return {'message': 'Post has been deleted successfully'}
    raise HTTPException(status_code=404, detail='Post Not Found')

#   Actualizar un elemento
@app.put('/posts/{post_id}')
def update_post(post_id: str, updatedPost: Post):
    for index, post in enumerate(posts):
        if post['id'] == post_id:
            posts[index]['title'] = updatedPost.title
            posts[index]['content'] = updatedPost.content
            posts[index]['author'] = updatedPost.author
            return {'message': 'Post has been updated successfully'}
    raise HTTPException(status_code=404, detail='Post Not Found')
             

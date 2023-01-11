# from comunidadeimpressionadora import app, database
# from comunidadeimpressionadora.models import Usuario
#
# with app.app_context():
#     database.create_all()
# # Todos comandos que você executar em banco de dados deve estar dentro de um with app.app_context():
# print()
# with app.app_context():
#     usuario = Usuario(username="Renato", email="renato@gmail.com", senha="123456")
#     usuario_2 = Usuario(username="Rocha", email="rocha@gmail.com", senha="123456")
#
#     database.session.add(usuario)
#     database.session.add(usuario_2)
#
#     database.session.commit()


# with app.app_context():
#     usuario_teste = Usuario.query.filter_by(id=1).first()
#     usuario_teste_1 = Usuario.query.filter_by(email='renato@gmail.com').first()
#     # usuario_teste = Usuario.query.filter_by(id=1).all() -> Ia ser uma lista de todos usuarios que possuem esse critério
#     print(usuario_teste)
#     print(usuario_teste.email)
#     print(usuario_teste_1)
#     print(usuario_teste_1.username)

# with app.app_context():
#     my_post = Post(id_usuario=1, titulo="Primeiro post renato", corpo="Voador")
#     database.session.add(my_post)
#     database.session.commit()

print()
#
# with app.app_context():
#     post_test = Post.query.all()
#     post_test_1 = Post.query.first()
#     print(post_test_1)
#     print(post_test_1.titulo)
#     print(post_test_1.autor)
#     print(post_test_1.autor.username)
#     print(post_test_1.autor.email)
#     print(post_test_1.autor.id)


# with app.app_context():
#     database.drop_all()
#     database.create_all()
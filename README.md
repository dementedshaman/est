est
====

### Instalação

Após clonar o projeto, entre na pasta criada e execute os seguintes comandos:

* Crie uma virtualenv para facilidade na instalação de versões e para não conflitar com suas versões atuais.

```
virtualenv -p python3 venv
source venv/bin/activate
```

* Instale os pacotes requeridos.

```
pip install -r requirements.txt
```

* Criar Banco de dados est

```
psql -U username -d mydatabase -c 'CREATE DATABASE est'
```

* Faça o setup da aplicação, copiando o arquivo de settings local.

```
cp expotec/local_settings.py.example expotec/local_settings.py
```

* Edite o arquivo `expotec/local_settings.py` com as suas configurações.

* Inicie o projeto.

```
python manage.py runserver

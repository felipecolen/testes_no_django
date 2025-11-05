# Django Backend
Projeto desenvolvido para uma aula prática sobre Testes em Software.

Navegue pelas branchs para acompanhar a evolução do código, nesta sequência:

1. feature/estrutura-base
2. feature/consumir-api-camara
3. tests/adicionar-testes
4. tests/refatorando-para-adicionar-testes


### Subir o projeto

Instale as dependências e suba o projeto.
OBS: No Windows é necessário também instalar as dependências do requiriments-dev.txt
(devido a problemas para servir arquivos estáticos a partir do Windows, foi adicionado a dependência do Whitenoise)

Recomenda-se utilizar o [Python](https://www.python.org/downloads/) com
[Anaconda](https://www.anaconda.com/products/individual#Downloads) (já facilita a vida).


Execute os comandos abaixo em um terminal (bash/prompt) *dentro da pasta raiz deste projeto*.

    # criar um ambiente virtual do Python com Anaconda
    conda create --name tests_no_django python=3.10

    # ativar o ambiente virtual
    conda activate tests_no_django

    # instalar Django djangorestframework etc...
    python -m pip install -r requirements-dev.txt
    python manage.py runserver  # roda o projeto na porta 8000
    python manage.py runserver 8001 # roda o projeto na porta 8001


Acesse: `http://localhost:8000/`

Posteriormente, pela linha de comando será necessário apenas

    # caso precise, ativar o ambiente
    conda activate tests_no_django

    #subir a app
    python manage.py runserver


## Rodar os testes
    python manage.py test


## Docker
    docker-compose up -d

Acesse: `http://localhost:8080/`

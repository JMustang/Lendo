# Lendo

- Interpretador de texto, feito com **Django**.

## Passo a passo

- Criando o diretório:

```bash
mkdir Lendo && cd Lendo
```

- Iniciando o ambiente de desenvolvimento com **venv**:

```bash
python3 -m venv env
```

- Iniciando o ambiente virtual:

```bash
source env/bin/activate
```

- Instalando o **Django** no ambiente virtual:

```bash
pip install django
```

- Iniciando o projeto com o **django-admin**:

```bash
django-admin startproject app
```

- Rodando a primeira migration:

```bash
python manage.py migrate
```

- Iniciando o templete basico do **Django**:

```bash
python manage.py startapp core
```
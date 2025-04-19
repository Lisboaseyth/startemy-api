# 🎓 Startemy API

Bem-vindo à **Startemy API** – uma plataforma educacional desenvolvida com Django Rest Framework, com autenticação via JWT e suporte a cursos, módulos e etapas (steps).  

---

## 🛠️ Tecnologias

- Python 3.11+
- Django 4+
- Django REST Framework
- JWT com SimpleJWT
- SQLite
- Virtualenv

---

## 📦 Setup do Projeto

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/startemy-api.git

cd startemy-api

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Migrações
python manage.py migrate

# Crie um superusuário (opcional)
python manage.py createsuperuser

# Rode o servidor
python manage.py runserver
```

## 📚 Endpoints de Cursos
- GET
  ```bash
  GET /api/courses/ # Listar todos os Cursos
  GET /api/courses/<course_id>/ # Detalha um curso específico
  GET /api/courses/<course_id>/modules/ # Lista os módulos de um curso
  GET /api/courses/<course_id>/modules/<module_id>/ # Detalha um módulo específico
  GET /api/courses/<course_id>/modules/<module_id>/steps/ # Lista os passos (steps) de um módulo
  GET /api/courses/<course_id>/modules/<module_id>/steps/<step_id>/ # Detalha um passo (step) específico
  ```

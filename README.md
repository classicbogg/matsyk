# matsyk

## На паре развернуть

```bash
git clone https://github.com/classicbogg/matsyk.git
cd matsyk
python -m venv venv
```

Активация venv:

- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

Дальше:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Админка: http://127.0.0.1:8000/admin/  
Пример: http://127.0.0.1:8000/quotes/

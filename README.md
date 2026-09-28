# matsyk

## На паре развернуть

```bash
git clone https://github.com/classicbogg/matsyk.git
cd matsyk
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Вот примеры с полным URL

---

### Цитаты (`quotes`)

- `GET http://127.0.0.1:8000/quotes/` — получить список всех цитат.  
- `POST http://127.0.0.1:8000/quotes/` — создать новую цитату.  
- `GET http://127.0.0.1:8000/quotes/5/` — получить цитату с ID 5.  
- `PUT http://127.0.0.1:8000/quotes/5/` — обновить цитату с ID 5 (все переданные поля перезапишутся, остальные останутся).  
- `PATCH http://127.0.0.1:8000/quotes/5/` — частично обновить цитату с ID 5 (только те поля, что прислали в запросе).

---

### Категории (`categories`)

- `GET http://127.0.0.1:8000/categories/` — получить список категорий.  
- `POST http://127.0.0.1:8000/categories/` — создать категорию.  
- `GET http://127.0.0.1:8000/categories/3/` — получить категорию с ID 3.  
- `PUT http://127.0.0.1:8000/categories/3/` — обновить категорию с ID 3.  
- `PATCH http://127.0.0.1:8000/categories/3/` — частично обновить категорию с ID 3.

---

### Теги (`tags`)

- `GET http://127.0.0.1:8000/tags/` — получить список тегов.  
- `POST http://127.0.0.1:8000/tags/` — создать тег.  
- `GET http://127.0.0.1:8000/tags/7/` — получить тег с ID 7.  
- `PUT http://127.0.0.1:8000/tags/7/` — обновить тег с ID 7.  
- `PATCH http://127.0.0.1:8000/tags/7/` — частично обновить тег с ID 7.

---

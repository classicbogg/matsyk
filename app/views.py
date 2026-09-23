# json - стандартная библиотека Python, чтобы читать JSON из тела запроса
import json

# JsonResponse - ответ клиенту в формате JSON
from django.http import JsonResponse
# csrf_exempt - отключает проверку CSRF-токена для POST с JSON
from django.views.decorators.csrf import csrf_exempt

from .models import Category, Quote, Tag


def get_quotes(request):
    # Берём все цитаты из базы
    quotes = []
    for quote in Quote.objects.all():
        # В список кладём обычные словари Python
        quotes.append({
            "id": quote.id,
            "text": quote.text,
            # category.name - имя категории через связь ForeignKey
            "category": quote.category.name,
        })
    # Отдаём словарь {"quotes": [...]}, а не голый список
    return JsonResponse({"quotes": quotes})


def get_quote(request, pk):
    # pk - номер цитаты из адреса, например /quote/1/
    try:
        quote = Quote.objects.get(pk=pk)
    except Quote.DoesNotExist:
        # Если такой цитаты нет - отвечаем ошибкой 404
        return JsonResponse({"error": "Цитата не найдена"}, status=404)

    return JsonResponse({
        "id": quote.id,
        "text": quote.text,
        "category": quote.category.name,
    })


def get_categories(request):
    categories = []
    for category in Category.objects.all():
        categories.append({
            "id": category.id,
            "name": category.name,
        })
    return JsonResponse({"categories": categories})


def get_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return JsonResponse({"error": "Категория не найдена"}, status=404)

    return JsonResponse({
        "id": category.id,
        "name": category.name,
    })


def get_tags(request):
    tags = []
    for tag in Tag.objects.all():
        tags.append({
            "id": tag.id,
            "name": tag.name,
        })
    return JsonResponse({"tags": tags})


def get_tag(request, pk):
    try:
        tag = Tag.objects.get(pk=pk)
    except Tag.DoesNotExist:
        return JsonResponse({"error": "Тег не найден"}, status=404)

    return JsonResponse({
        "id": tag.id,
        "name": tag.name,
    })


# Без @csrf_exempt Django отклонит POST с JSON (ошибка 403)

@csrf_exempt
def create_category(request):
    # request.body - сырой текст запроса, json.loads делает из него словарь
    data = json.loads(request.body)
    # Создаём категорию в базе
    category = Category.objects.create(name=data["name"])
    return JsonResponse({"id": category.id, "name": category.name})


@csrf_exempt
def create_tag(request):
    data = json.loads(request.body)
    tag = Tag.objects.create(name=data["name"])
    return JsonResponse({"id": tag.id, "name": tag.name})


@csrf_exempt
def create_quote(request):
    # Ожидаем JSON вида:
    # {"text": "текст", "category_id": 1, "tag_ids": [1, 2]}
    data = json.loads(request.body)
    # category_id - номер категории, Django сам найдёт связь
    quote = Quote.objects.create(
        text=data["text"],
        category_id=data["category_id"],
    )
    # tags.set вешает теги по списку номеров (ManyToMany)
    # если тегов нет - присылай "tag_ids": []
    quote.tags.set(data["tag_ids"])
    return JsonResponse({"id": quote.id, "text": quote.text})

import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Category, Quote, Tag

# цитаты

@method_decorator(csrf_exempt, name='dispatch')
class QuoteList(View):
    def get(self, request):
        quotes = []
        for quote in Quote.objects.all():
            quotes.append({
                "id": quote.id,
                "text": quote.text,
                "category": quote.category.name,
            })
        return JsonResponse({"quotes": quotes})

    def post(self, request):
        data = json.loads(request.body)
        quote = Quote.objects.create(
            text=data["text"],
            category_id=data["category_id"],
        )
        quote.tags.set(data["tag_ids"])
        return JsonResponse({
            "id": quote.id,
            "text": quote.text,
        }, status=201)


class QuoteDetail(View):
    def get(self, request, pk):
        try:
            quote = Quote.objects.get(pk=pk)
        except Quote.DoesNotExist:
            return JsonResponse({"error": "Цитата не найдена"}, status=404)

        return JsonResponse({
            "id": quote.id,
            "text": quote.text,
            "category": quote.category.name,
        })


# категории

@method_decorator(csrf_exempt, name='dispatch')
class CategoryList(View):
    def get(self, request):
        categories = []
        for category in Category.objects.all():
            categories.append({
                "id": category.id,
                "name": category.name,
            })
        return JsonResponse({"categories": categories})

    def post(self, request):
        data = json.loads(request.body)
        category = Category.objects.create(name=data["name"])
        return JsonResponse({
            "id": category.id,
            "name": category.name,
        }, status=201)


class CategoryDetail(View):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return JsonResponse({"error": "Категория не найдена"}, status=404)

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })
    
# Тэги

@method_decorator(csrf_exempt, name='dispatch')
class TagList(View):
    def get(self, request):
        tags = []
        for tag in Tag.objects.all():
            tags.append({
                "id": tag.id,
                "name": tag.name,
            })
        return JsonResponse({"tags": tags})

    def post(self, request):
        data = json.loads(request.body)
        tag = Tag.objects.create(name=data["name"])
        return JsonResponse({
            "id": tag.id,
            "name": tag.name,
        }, status=201)


class TagDetail(View):
    def get(self, request, pk):
        try:
            tag = Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            return JsonResponse({"error": " Тег не найден"}, status=404)

        return JsonResponse({
            "id": tag.id,
            "name": tag.name,
        })

from django.views import View
from django.http import HttpResponse

class ItemUpdateView(View):
    def put(self, request, pk):
        # Получаем объект из базы данных по первичному ключу
        item = get_object_or_404(Item, pk=pk)

        # Обновляем поля из данных запроса
        item.name = request.data.get('name', item.name)
        item.done = request.data.get('done', item.done)
        item.save()

        # Возвращаем обновлённые данные
        return HttpResponse(f"Item {pk} updated successfully")

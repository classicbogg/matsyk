import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from .models import Category, Quote, Tag


# Цитаты

@method_decorator(csrf_exempt, name='dispatch')
class QuoteList(View):
    # GET  список всех цитат
    def get(self, request):
        quotes = []
        for quote in Quote.objects.all():
            quotes.append({
                "id": quote.id,
                "text": quote.text,
                "category": quote.category.name,
            })
        return JsonResponse({"quotes": quotes})

    # POST  создать цитату
    def post(self, request):
        data = json.loads(request.body)
        quote = Quote.objects.create(
            text=data["text"],
            category_id=data["category_id"],
        )
        if "tag_ids" in data:
            quote.tags.set(data["tag_ids"])
        return JsonResponse({
            "id": quote.id,
            "text": quote.text,
        }, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class QuoteDetail(View):
    # GET  получить одну цитату
    def get(self, request, pk):
        quote = get_object_or_404(Quote, pk=pk)
        return JsonResponse({
            "id": quote.id,
            "text": quote.text,
            "category": quote.category.name,
        })

    # PUT  обновление
    def put(self, request, pk):
        quote = get_object_or_404(Quote, pk=pk)
        data = json.loads(request.body)

        quote.text = data.get("text", quote.text)
        if "category_id" in data:
            quote.category_id = data["category_id"]
        if "tag_ids" in data:
            quote.tags.set(data["tag_ids"])
        quote.save()

        return JsonResponse({
            "id": quote.id,
            "text": quote.text,
            "category": quote.category.name,
        })

    # PATCH
    def patch(self, request, pk):
        quote = get_object_or_404(Quote, pk=pk)
        data = json.loads(request.body)

        if "text" in data:
            quote.text = data["text"]
        if "category_id" in data:
            quote.category_id = data["category_id"]
        if "tag_ids" in data:
            quote.tags.set(data["tag_ids"])

        quote.save()
        return JsonResponse({
            "id": quote.id,
            "text": quote.text,
            "category": quote.category.name,
        })


# Категории

@method_decorator(csrf_exempt, name='dispatch')
class CategoryList(View):
    # GET
    def get(self, request):
        categories = []
        for category in Category.objects.all():
            categories.append({
                "id": category.id,
                "name": category.name,
            })
        return JsonResponse({"categories": categories})

    # POST
    def post(self, request):
        data = json.loads(request.body)
        category = Category.objects.create(name=data["name"])
        return JsonResponse({
            "id": category.id,
            "name": category.name,
        }, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDetail(View):
    # GET одна категория
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })

    # PUT  обновить категорию
    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        data = json.loads(request.body)
        category.name = data.get("name", category.name)
        category.save()
        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })

    # PATCH  частично обновить категорию
    def patch(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        data = json.loads(request.body)
        if "name" in data:
            category.name = data["name"]
        category.save()
        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


# Теги

@method_decorator(csrf_exempt, name='dispatch')
class TagList(View):
    # GET список тегов
    def get(self, request):
        tags = []
        for tag in Tag.objects.all():
            tags.append({
                "id": tag.id,
                "name": tag.name,
            })
        return JsonResponse({"tags": tags})

    # POST создать тег
    def post(self, request):
        data = json.loads(request.body)
        tag = Tag.objects.create(name=data["name"])
        return JsonResponse({
            "id": tag.id,
            "name": tag.name,
        }, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class TagDetail(View):
    # GET один тег
    def get(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        return JsonResponse({
            "id": tag.id,
            "name": tag.name,
        })

    # PUT  обновить тег
    def put(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        data = json.loads(request.body)
        tag.name = data.get("name", tag.name)
        tag.save()
        return JsonResponse({
            "id": tag.id,
            "name": tag.name,
        })

    # PATCH  частично обновить тег
    def patch(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        data = json.loads(request.body)
        if "name" in data:
            tag.name = data["name"]
        tag.save()
        return JsonResponse({
            "id": tag.id,
            "name": tag.name,
        })

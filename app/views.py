from django.http import JsonResponse
from .models import Quote

def get_quote(request, pk):
    try:
        quote = Quote.objects.get(pk=pk)
    
        response_data = {
            "id": quote.id,
            "text": quote.text,
            "category": quote.category.name,       #  имя категории через связь
            "tags": [t.name for t in quote.tags.all()], #  список имен тегов
            "created_at": quote.created_at.isoformat()
        }
        return JsonResponse(response_data)
    except Quote.DoesNotExist:
        return JsonResponse({"error": "Цитата не найдена"}, status=404)

from store.models import Category, SubCategory


def categories(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    
    return {
        "categories": categories,
        "subcategories": subcategories
    }
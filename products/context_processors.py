from products.models import Category


def navbar_data(request):
    categories = Category.objects.filter(parent_category=None)
    return {'categories': categories}
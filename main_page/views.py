from django.shortcuts import render
from .models import WorkPost

def index(request):
    posts = WorkPost.objects.all().order_by('-pk')

    return render(
        request,
        'main_page/index.html',
        {
            'posts' : posts,
        }
    )

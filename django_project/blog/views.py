from django.shortcuts import render

# Create your views here.


posts = [
    {
        'author' : 'CoreyMS',
        'title' : 'blog post 1',
        'content' : 'first post content',
        'date_posted' : 'August 27, 2018'
    },
    {
        'author' : 'sebastian',
        'title' : 'blog post 2',
        'content' : 'second post content',
        'date_posted' : 'sep 7, 20202'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html' , { 'title' : 'About' })
from django.shortcuts import render
from django.core.paginator import Paginator

def index(request):
    all_posts = [
        {"title" : "Post 1", "content" : "Content 1", "author": "Author 1"},
        {"title" : "Post 2", "content" : "Content 2", "author": "Author 2"},
        {"title" : "Post 3", "content" : "Content 3", "author": "Author 3"},
        {"title" : "Post 4", "content" : "Content 4", "author": "Author 4"},
        {"title" : "Post 5", "content" : "Content 5", "author": "Author 5"},
        {"title" : "Post 6", "content" : "Content 6", "author": "Author 6"},
        {"title" : "Post 7", "content" : "Content 7", "author": "Author 7"},
        {"title" : "Post 8", "content" : "Content 8", "author": "Author 8"},
        {"title" : "Post 9", "content" : "Content 9", "author": "Author 9"},
        {"title" : "Post 10", "content" : "Content 10", "author": "Author 10"},
        {"title" : "Post 1", "content" : "Content 1", "author": "Author 1"},
        {"title" : "Post 2", "content" : "Content 2", "author": "Author 2"},
        {"title" : "Post 3", "content" : "Content 3", "author": "Author 3"},
        {"title" : "Post 4", "content" : "Content 4", "author": "Author 4"},
        {"title" : "Post 5", "content" : "Content 5", "author": "Author 5"},
        {"title" : "Post 6", "content" : "Content 6", "author": "Author 6"},
        {"title" : "Post 7", "content" : "Content 7", "author": "Author 7"},
        {"title" : "Post 8", "content" : "Content 8", "author": "Author 8"},
        {"title" : "Post 9", "content" : "Content 9", "author": "Author 9"},
        {"title" : "Post 10", "content" : "Content 10", "author": "Author 10"},
        {"title" : "Post 1", "content" : "Content 1", "author": "Author 1"},
        {"title" : "Post 2", "content" : "Content 2", "author": "Author 2"},
        {"title" : "Post 3", "content" : "Content 3", "author": "Author 3"},
        {"title" : "Post 4", "content" : "Content 4", "author": "Author 4"},
        {"title" : "Post 5", "content" : "Content 5", "author": "Author 5"},
        {"title" : "Post 6", "content" : "Content 6", "author": "Author 6"},
        {"title" : "Post 7", "content" : "Content 7", "author": "Author 7"},
        {"title" : "Post 8", "content" : "Content 8", "author": "Author 8"},
        {"title" : "Post 9", "content" : "Content 9", "author": "Author 9"},
        {"title" : "Post 10", "content" : "Content 10", "author": "Author 10"},
        {"title" : "Post 1", "content" : "Content 1", "author": "Author 1"},
        {"title" : "Post 2", "content" : "Content 2", "author": "Author 2"},
        {"title" : "Post 3", "content" : "Content 3", "author": "Author 3"},
        {"title" : "Post 4", "content" : "Content 4", "author": "Author 4"},
        {"title" : "Post 5", "content" : "Content 5", "author": "Author 5"},
        {"title" : "Post 6", "content" : "Content 6", "author": "Author 6"},
        {"title" : "Post 7", "content" : "Content 7", "author": "Author 7"},
        {"title" : "Post 8", "content" : "Content 8", "author": "Author 8"},
        {"title" : "Post 9", "content" : "Content 9", "author": "Author 9"},
        {"title" : "Post 10", "content" : "Content 10", "author": "Author 10"},
        {"title" : "Post 1", "content" : "Content 1", "author": "Author 1"},
        {"title" : "Post 2", "content" : "Content 2", "author": "Author 2"},
        {"title" : "Post 3", "content" : "Content 3", "author": "Author 3"},
        {"title" : "Post 4", "content" : "Content 4", "author": "Author 4"},
        {"title" : "Post 5", "content" : "Content 5", "author": "Author 5"},
        {"title" : "Post 6", "content" : "Content 6", "author": "Author 6"},
        {"title" : "Post 7", "content" : "Content 7", "author": "Author 7"},
        {"title" : "Post 8", "content" : "Content 8", "author": "Author 8"},
        {"title" : "Post 9", "content" : "Content 9", "author": "Author 9"},
        {"title" : "Post 10", "content" : "Content 10", "author": "Author 10"},
    ]

    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    featured_posts = all_posts[:3]
    recent_posts = all_posts[3:7]
    popular_posts = all_posts[7:]
     
    context = {'featured_posts': featured_posts, 'recent_posts' : recent_posts, 'popular_posts' : popular_posts, 'all_posts' : all_posts, 'total_posts' : len(all_posts) }
    
    
    return render(request, 'MyApp/index.html', {'posts': context})

from tkinter.tix import Tree
from turtle import distance, title
from django.shortcuts import render
from .forms import PostSearchForm
from .models import Book
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity, TrigramDistance


# Create your views here.

def search(request):
    form = PostSearchForm()
    results = []
    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            # results = Book.objects.filter(title__icontains=q)
            # print(Book.objects.filter(title__icontains=q).query) # returns the raw sql statement 
            # print(Book.objects.filter(title__icontains=q).explain(analyze=True)) # returns an anlysis of how long the execution took
            # Full text search
            results = Book.objects.filter(title__search=q)

            # using search Vector
            # results = Book.objects.annotate(search=SearchVector('title', 'authors'),).filter(search=q)

            # search rank
            #     vector = SearchVector('title')
            #     query = SearchQuery(q)
            #     results = Book.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')
            # # weighted rank
            # vector = SearchVector('title', weight='B') + SearchVector('authors', weight='A')
            # query = SearchQuery(q)
            # results = Book.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')
            # #  using trigram similarity
            # results = Book.objects.annotate(similarity=TrigramSimilarity('title', q),).filter(similarity__gte=0.4).order_by('-similarity')

            # using trigram distance
            # results = Book.objects.annotate(distance=TrigramDistance('title', q), ).filter(distance__lte=0.8).order_by(
        # 'distance')

        # using gin index
        # print('#1: ')
        # print(Book.objects.filter(title__trigram_similar=q).explain(analyze=True))

        # print('#2: ')
        # print(Book.objects.filter(title__trigram_similar=q).annotate(similar=TrigramSimilarity('title', q)).order_by('-similar').explain(analyze=True)
        # )

    return render(request, 'book/index.html', {'form': form, 'results': results})

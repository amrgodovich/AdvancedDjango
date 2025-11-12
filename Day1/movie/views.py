from django.shortcuts import render,HttpResponse
from .models import *
from django.db import connection
from django.db.models import Q, F
import time
import cProfile, pstats, io

# Create your views here.
def listing(request):
    # This is N+1 because of Foreign Key
    # ratings = Rating.objects.all()
    # html = "<ul>"
    # limit=500
    # for r in ratings:
    #     limit-=1
    #     if limit==0:
    #         break
    #     print(r)
    #     html += f"<li>User: {r.userId} | Movie: {r.movieId} | Rating: {r.rating}</li>"
    # html += "</ul>"
    # num_queries = len(connection.queries)
    # html = f"<p>Number of queries: {num_queries}</p>" + html
    # return HttpResponse(html)


# ENHACEDDDDDDD
    # Enhance above query using ‘select_related’ and analyze difference.
    # ratings = Rating.objects.select_related('userId', 'movieId').all()
    # html = "<ul>"
    # limit=500
    # for r in ratings:
    #     limit-=1
    #     if limit==0:
    #         break
    #     print(r)
    #     html += f"<li>User: {r.userId} | Movie: {r.movieId.title} | Rating: {r.rating}</li>"
    # html += "</ul>"
    # num_queries = len(connection.queries)
    # html = f"<p>Number of queries: {num_queries}</p>" + html
    # return HttpResponse(html)


##PREFETCH
    # movies = Movie.objects.prefetch_related('tag_set').all()
    # html = "<ul>"
    # for m in movies:
    #     tags = "-".join(t.tag for t in m.tag_set.all())
    #     html += f"<li>{m.title} | Tags: {tags}</li>"
    # html += "</ul>"
    # num_queries = len(connection.queries)
    # html = f"<p>Number of queries: {num_queries}</p>" + html
    # return HttpResponse(html)





# ====LAB2======


    # # Build dynamic filter query using Q() expression.
    # query = Q(title__icontains="City") 
    # matching_movies = Movie.objects.filter(query)
    # print(len(matching_movies))
    # html = "<ul></ul>"
    # return HttpResponse(html)

    # Update any field values directly in SQL using F() expression.
    # Rating.objects.update(rating=F('rating') + 1)
    # return HttpResponse("html")

    # Select specific fields using  only() and defer() methods.
    # mov_only = Movie.objects.only('title', 'genres')
    # mov_def=Movie.objects.defer('genres')

    # # Retrieve data as dict using proper ORM method for this.
    # mov_dicts = list(Movie.objects.values('id', 'title', 'genres'))

    # # Retrieve data as tuple using proper ORM method for this.
    # mov_tuples = list(Movie.objects.values_list('id', 'title', 'genres'))

    # Apply index on proper fields in your models
    # DONE

    # Select n values from both indexed and non indexed column, monitor their performance and compare it.
    # start_indexed = time.time()
    # indexed_movies = list(Movie.objects.values_list('title', flat=True)[:1000])
    # end_indexed = time.time()




    # start_non_indexed = time.time()
    # non_indexed_movies = list(Movie.objects.values_list('movieId', flat=True)[:1000])
    # end_non_indexed = time.time()
    # indexed_duration = end_indexed - start_indexed
    # non_indexed_duration = end_non_indexed - start_non_indexed
    # print("indexed_duration:", indexed_duration)
    # print("non_indexed_duration:", non_indexed_duration)
    # return HttpResponse("html")
    # Change conn max age and observe the changes.
    # DONE in settings.py


# =====Lab3=====


    pr = cProfile.Profile()
    # pr.enable()


    # ratings = Rating.objects.select_related('userId', 'movieId').all()[:500] 

    # html = "<ul>"
    # for r in ratings:
    #     html += f"<li>User: {r.userId} | Movie: {r.movieId.title} | Rating: {r.rating}</li>"
    # html += "</ul>"

    # pr.disable()
    # s = io.StringIO()
    # ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    # ps.print_stats(10)  
    # num_queries = len(connection.queries)
    # total_sql_time = sum(float(q.get('time', 0)) for q in connection.queries)

    # html_report = f"""
    #     <h2>Ratings List (Optimized with select_related)</h2>
    #     <p>Total Ratings Loaded: {len(ratings)}</p>
    #     <p>Total Queries Executed: {num_queries}</p>
    #     <p>Total SQL Time: {total_sql_time:.5f}s</p>
    #     {html}
    #     <h3>cProfile Top 10 Functions</h3>
    #     <pre>{s.getvalue()}</pre>
    # """

    # return HttpResponse(html_report)

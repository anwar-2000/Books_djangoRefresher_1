from django.shortcuts import render ,get_object_or_404



from .models import Book # importing the books model && data stored init

def index(request) :
    books = Book.objects.all()
    return render(request,"books_outlet/index.html",{
        "books" : books
    })
def book_detail (request,id):
  #  try:
   #     book = Book.objects.get(pk=id)
   # except :
   #     raise Http404()
    book = get_object_or_404(Book , pk=id)
    return render(request , "books_outlet/book_detail.html" , {
        "title" : book.title,
        "author" : book.author,
        "rating":book.rating,
        "isBestSeller" : book.isBestSelling
    })
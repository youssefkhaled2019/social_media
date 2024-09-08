from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts=[
    {
        "author":"youssef",
        "title":"test1",
        "content":" skdsjkhfsfhsdf ",
        "date_posted":"August 27 ,2018",
    },
    {
        "author":"nader",
        "title":" welcome",
        "content":"second post content ",
        "date_posted":"August 27 ,2018",
    }
]

def home(request):
    context={"posts":posts}
    return render(request,"blog/home.html",context)
def about(request):
    return render(request,"blog/about.html",{"title":"about"})
    # return HttpResponse("about")
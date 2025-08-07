from django.shortcuts import render

def home(request):
    title = "this is my title"
    context = {'title': title}
    return render(request,'posts/home.html',context)


def blogposts(request):
    context = {}
    return render(request,'posts/blogposts.html',context)
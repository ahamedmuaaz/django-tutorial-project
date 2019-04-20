from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
       'Name':'Muaaz',
       'Age':'22',
       'Job':'Software Engineer'
    },
    {
       'Name':'Roy',
       'Age':'24',
       'Job':'QA'

    }
]
# Create your views here.
def home(request):
    context={
        'posts':posts
    }
    m=2*2
    return render(request,'view/home.html',context)

def about(request):
    return render(request,'view/about.html')
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wrddict={}
    for i in wordlist:
        if i in wrddict:
            wrddict[i]+=1
        else:
            wrddict[i]=1
    sw=sorted(wrddict.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'countwrd':len(wordlist),'wrddict':sw})

def about(request):
    return render(request,'About.html')
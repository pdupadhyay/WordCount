import operator
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wordcountdict = {}
    for word in wordlist:
        if word in wordcountdict:
            wordcountdict[word] += 1
        else:
            wordcountdict[word] = 1
    sortedlist = sorted(wordcountdict.items(), key=operator.itemgetter(1), reverse = True)
    return render(request, 'count.html',{'fulltext': fulltext, 'count': len(wordcountdict.keys()), 'sortedlist': sortedlist, 'totalwords': sum(wordcountdict.values())})

def about(request):
    return render(request, 'about.html')
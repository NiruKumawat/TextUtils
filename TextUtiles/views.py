from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return render(request,'index.html')
    
def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get("fullcaps","off")
    newlinerremove = request.POST.get('newlinerremove','off')
    spaceremove = request.POST.get('extraspaceremove','off')
    count = request.POST.get('charcount','off')
    
    if removepunc  =="on":
        punctuations = '''!()-[]{};:'"<>./?@#$%^&*_~'''
        analyzed = ""
        for ch in djtext:
            if ch not in punctuations:
                analyzed = analyzed + ch
        params = {'purpose':'Remove Punctuationns', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if (fullcaps== "on"):
        analyzed=""
        for ch in djtext:
            analyzed = analyzed + ch.upper()
        params = {'purpose':'Upper case', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if(newlinerremove =="on"):
        analyzed=""
        for ch in djtext:
            if ch !="\n" and ch != "\r":
                analyzed = analyzed + ch
        params = {'purpose':'new line remover', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if(spaceremove =='on'):
        analyzed =""
        for ch in djtext:
            if ch != " ":
                analyzed = analyzed + ch
        params = {'purpose':'Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(count == "on"):
        analyzed = len(djtext)
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if(removepunc  !="on" and fullcaps != "on" and newlinerremove !="on" and spaceremove !='on' and count != "on"):
        return HttpResponse("Please select any operation and try again")

    return render(request, 'analyze.html', params)
   
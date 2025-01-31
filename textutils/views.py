from django.http import HttpResponse
from django.shortcuts import render
from sqlparse.tokens import Punctuation


def index(request):
    return render(request,'index.html')

def analyze(request):
    global params
    maintext=request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    capitalize = request.POST.get('capitalize','off')
    newlineremover = request.POST.get('newlineremover','off')
    exraspaceremover = request.POST.get('exraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    print(removepunc)
    print(maintext)

    Punctuations = '''&<>‘*:,…—–!-."?""'';/()[]'''
    analyzed = ""
    if removepunc == 'on':
        for char in maintext:
            if char not in Punctuations:
                analyzed = analyzed + char
        params = {'Purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        maintext = analyzed

    if capitalize == "on":
        analyzed= ""
        for char in maintext:
            analyzed = analyzed + char.upper()
        params = {'Purpose': 'Normal to Capitalize', 'analyzed_text': analyzed}
        maintext = analyzed

    if newlineremover == "on":
        analyzed= ""
        for char in maintext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'Purpose': 'Remove the Newline', 'analyzed_text': analyzed}
        maintext = analyzed

    if exraspaceremover == "on":
        analyzed = maintext[0]
        for char1, char2 in zip(maintext, maintext[1:]):
            if not (char1 == " " and char2 == " "):
                analyzed += char2
        params = {'Purpose': 'Normal to Capitalize', 'analyzed_text': analyzed}
        maintext = analyzed

    if charcount == "on":
        analyzed=len(maintext)
        params = {'Purpose': 'Count the character', 'analyzed_text': analyzed}
        maintext = analyzed

    if removepunc!= "on" and capitalize != "on" and newlineremover!= "on" and exraspaceremover!= "on" and charcount != "on":
        return HttpResponse('Error!!! please select the operations')

    return render(request, 'analyze.html', params)


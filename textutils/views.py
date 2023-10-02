from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse('hello Iam about page')


def analyze(request):
    # Get the text
    dj_text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    cap_all = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremover', 'off')
    extraspaceremove = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    if removepunc == 'on':
        # Analyze the text
        analyzed_text = ''
        punctuations = '''?><{}!@#$%^*`~….,—––:;"'[ ]( )'''
        for letter in dj_text:
            if letter not in punctuations:
                analyzed_text += letter
        params = {
            'purpose': 'Removed Punctuations',
            'analyzed_text': analyzed_text,
        }
        return render(request, 'analyze.html', params)
    elif cap_all == 'on':
        # Analyze text
        analyzed_text = ""
        for char in dj_text:
            analyzed_text += char.upper()

        params = {
            'purpose': 'Captilize all',
            'analyzed_text': analyzed_text,
        }
        return render(request, 'analyze.html', params)

    elif newlineremove == 'on':
        new_analyzed = ''
        for char in dj_text:
            if char != '\n' and char != '\r':
                new_analyzed += char
        params = {
            'purpose': 'New line Removed',
            'analyzed_text': new_analyzed,
        }
        return render(request, 'analyze.html', params)

    elif extraspaceremove == 'on':
        analyzed_text = ''
        for index, char in enumerate(dj_text):
            if not(dj_text[index] == ' ' and dj_text[index+1] == ' '):
                analyzed_text += char
        params = {
            'purpose': 'extra space Removed',
            'analyzed_text': analyzed_text,
        }
        return render(request, 'analyze.html', params)
    elif charcounter == 'on':
        analyzed_text = f'Number of characters in your text: {len(dj_text)}'
        params = {
            'purpose': 'extra space Removed',
            'analyzed_text': analyzed_text,
        }
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")

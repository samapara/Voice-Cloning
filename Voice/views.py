from django.shortcuts import render


# Create your views here.
def indexView(request):
    if request.method == 'GET':
        return render(request, "index.html")
    else:
        text = request.POST.get('inputText', None)
        # voice = function call(text)
        displayObj = {
            'text': text
            # 'voice' = voice
        }
        return render(request, "voice.html", {'displayObj': displayObj})


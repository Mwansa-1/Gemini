from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
import typing_extensions as typing

# class Response(typing.TypedDict):
#   response_item: str
genai.configure(api_key='AIzaSyASINCqIKiWdWEcmz3_Ij-u3ELqSSnBPDQ')
# Initialize the model
model = genai.GenerativeModel('gemini-1.5-pro',
                            #   generation_config={"response_mime_type": "application/json",
                            #                      "response_schema": list[Response]}
                            )

@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        response = model.generate_content(prompt)
        return JsonResponse({'response': response.text})
    return render(request, 'chat/index.html')
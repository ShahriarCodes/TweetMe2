from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Tweet

# Create your views here.


def home_view(request, *args, **kwargs):
    print(args, kwargs)

    return HttpResponse("<h1> hello </h1>")


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    Rest Api view
    Consume by Javascript or Swift
    return json data
    """

    print(args, kwargs)

    data = {
        'id': tweet_id,
    }

    status = 200

    try:
        obj = Tweet.objects.get(id=data['id'])
        # append content to the dictionary
        data['content'] = obj.content
        # data['image_path'] = obj.image.url
    except:
        data['message'] = 'Not Found'
        status = 404

    # json.dumps content_tyoe="application.json"
    return JsonResponse(data, status=status)

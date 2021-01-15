from random import randint
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Tweet

# Create your views here.


def home_view(request, *args, **kwargs):
    print(args, kwargs)

    context = {}
    return render(request, 'tweets/home.html',
                  context=context, status=200)


def tweet_list_view(request, *args, **kwargs):
    """
    REST API View of All Tweets
    Consume by Javascript or Swift
    return json data
    """
    queryset = Tweet.objects.all()

    # list comprehension in queryset
    tweets_list = [{
        'id': x.id,
        'content': x.content,
        'likes': randint(0, 500),
    } for x in queryset]

    data = {
        'isUser': False,
        'response': tweets_list
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API View
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

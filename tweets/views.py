from random import randint
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import is_safe_url
from django.conf import settings

from .models import Tweet
from .forms import TweetForm

# Create your views here.


def home_view(request, *args, **kwargs):
    print(args, kwargs)

    context = {}
    return render(request, 'tweets/home.html',
                  context=context, status=200)


ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    # print('Post data is: ', request.POST)
    next_url = request.POST.get('next') or None
    # this next url is coming from home.thml <input type="hidden" value='/' name="next" />
    print('next_url', next_url)

    if form.is_valid():
        obj = form.save(commit=False)
        # do other form related logic
        obj.save()

        # this url redirect has a bug. form is saved before the url redirect
        if next_url is not None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()

    context = {'form': form}
    return render(request, 'components/form.html', context=context)


def tweet_list_view(request, *args, **kwargs):
    """
    REST API View of All Tweets
    Consume by Javascript or Swift
    return json data
    """
    queryset = Tweet.objects.all().order_by('-id')

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

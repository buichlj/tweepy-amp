from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
import tweepy


from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    tweets = None
    if(request.GET.get('mybtn')=="Click"):
    	tweets = tweet(request.GET.get('twitterHandle'));
    elif(request.GET.get('mybtn')=="Tweet"):
    	updateStatus(request.GET.get('twitterHandle'));

    context = {'latest_question_list': latest_question_list, 'tweets' : tweets}
    return render(request, 'polls/index.html', context)
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def tweet(twitterHandle):
	api = getAPI()
	public_tweets = api.user_timeline(twitterHandle)
	return public_tweets;

def updateStatus(tweet):
	api = getAPI()
	status = api.update_status(status = tweet)
	print(status.id)

def getAPI():
    #consumer, consec
    # key, sec
	auth = tweepy.OAuthHandler("consumer", "consumer_secret")
	auth.set_access_token("key", "key_secret")
	api = tweepy.API(auth)
	return api
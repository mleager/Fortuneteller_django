from django.shortcuts import render
import random

# Create your views here.


def fortune(request):
    tell_fortune = random.choice(fortune_list)
    context = {'fortune': tell_fortune}
    return render(request, 'randomfortune/fortune.html', context)


fortune_list = [
    "All will go well with your new project",
    "If you continually give, you wil continually have",
    "Self-knowledge is a life long process",
    "You are busy, but you are happy",
    "Your abilities are unparalled",
    "Those who care will make the effort",
    "Now is the time to try something new",
    "Miles are covered one step at a time",
    "We all die alone. Happy birthday"
]

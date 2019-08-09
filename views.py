from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Debate
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth


def debate_list(request):
    debates = Debate.objects
    debates_list=Debate.objects.all()
    paginator = Paginator(debates_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'debate_list.html',{'debates':debates,'posts':posts})

def debate_detail(request, debate_id):
    debate_detail = get_object_or_404(Debate, pk=debate_id)
    return render(request, 'debate_detail.html', {'debate':debate_detail})

def add_comment(request, pk):
    debate = get_object_or_404(Debate, pk=debate_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'debate_detail.html', {'form': form})

def agree(request,debate_id):
    debate=get_object_or_404(Debate, pk = debate_id)
    if debate.agree.filter(username=request.user.username).exists():
        debate.agree.remove(request.user)    
    else:
        debate.agree.add(request.user)
    debate.save()
    return redirect('/job_debate/%debate.pk')
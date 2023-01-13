from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import TitleForm

def index(request):
    """Homepage blogs"""
    return render(request, 'blogs/base.html')


def check_blog_owner(request, title):
    """Checks blog owner."""
    if title.owner != request.user:
        raise Http404


def posts(request):
    """It displays list of posts."""
    titles = BlogPost.objects.order_by('-id')
    context = {'titles': titles}
    return render(request, 'blogs/posts.html', context)


@login_required
def new_post(request):
    """It defines new post."""
    if request.method != 'POST':
        # Data didn't send; creates empty form
        form = TitleForm()
    else:
        # sent data POST; to process data
        form = TitleForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:posts')

    # To output an empty or invalid form
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request, title_id):
    """Edits existing record."""
    title = BlogPost.objects.get(id=title_id)
    check_blog_owner(request, title)

    if request.method != 'POST':
        # Original request; the data is filled with the data of the current record
        form = TitleForm(instance=title)
    else:
        # Sent data POST; to process data
        form = TitleForm(instance=title, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:posts')
        # To output an empty or invalid form
    context = {'title': title, 'form': form}
    return render(request, 'blogs/edit_post.html', context)


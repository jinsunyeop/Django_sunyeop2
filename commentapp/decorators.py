from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from articleapp.models import Article
from commentapp.models import Comment
from profileapp.models import Profile


def comment_ownership(func):
    def decorated(request,*args,**kwargs):
        commet = Comment.objects.get(pk=kwargs['pk'])
        if not comment.writer == request.user:
            return HttpResponseForbidden()

        return func(request,*args,**kwargs)
    return decorated
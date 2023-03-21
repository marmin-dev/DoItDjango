from django.views.generic import ListView
from ..models import Answer, Question, Comment
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


class QuestionListView(ListView):
    model = Question
    template_name = 'pybo/question_profile.html'
    context_object_name = 'questions'
    paginate_by = 10
    def get_queryset(self):
        self.user = get_object_or_404(User, pk=self.kwargs['user_id'])
        return Question.objects.filter(author=self.user).order_by('-create_date')


class AnswerListView(ListView):
    model = Answer
    template_name = 'pybo/answer_profile.html'
    context_object_name = 'answers'
    paginate_by = 10
    def get_queryset(self):
        self.user = get_object_or_404(User, pk=self.kwargs['user_id'])
        return Answer.objects.filter(author=self.user).order_by('-create_date')


class CommentListView(ListView):
    model = Comment
    template_name = 'pybo/comment_profile.html'
    context_object_name = 'comments'
    paginate_by = 10
    def get_queryset(self):
        self.user = get_object_or_404(User, pk=self.kwargs['user_id'])
        return Comment.objects.filter(author=self.user).order_by('-create_date')
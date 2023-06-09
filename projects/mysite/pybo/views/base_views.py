from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q,Count

from ..models import Question,Answer
import logging

logger=logging.getLogger('pybo')


def index(request,category="all"):
    """
    pybo 목록 출력
    """
    logger.info("INFO 레벨로 출력")
    page = request.GET.get('page','1') # 페이지
    kw = request.GET.get('kw','')
    so = request.GET.get('so','recent')

    # 카테고라
    if category == 'humor':
        question_list = Question.objects.filter(category='humor').order_by('-create_date')
    elif category == 'free':
        question_list = Question.objects.filter(category='free').order_by('-create_date')
    elif category == 'edu':
        question_list = Question.objects.filter(category='edu').order_by('-create_date')
    else:
        question_list = Question.objects.order_by('-create_date')

    # 정렬
    if so == 'recommend':
        question_list=question_list.annotate(
            num_voter=Count('voter')).order_by('-num_voter','-create_date')
    elif so == 'popular':
        question_list=question_list.annotate(
            num_answer=Count("answer")).order_by('-num_answer','-create_date')
    else: # recent
        question_list=question_list.order_by('-create_date')

    # 검색
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | # 제목 검색
            Q(content__icontains=kw) | # 내용 검색
            Q(author__username__icontains=kw) | # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)
        ).distinct()


    paginator = Paginator(question_list,10) # 페이지 당 10개씩 요청
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj,'page':page,'kw':kw}
    return render(request,'pybo/question_list.html',context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question,pk=question_id)
    ans = request.GET.get('ans','recent')
    page = request.GET.get('page','1')

    if ans == 'recommend':
        answer_list = Answer.objects.annotate(
            num_voter=Count('voter')).filter(question=question).order_by('-num_voter','-create_date')
    else:
        answer_list = Answer.objects.filter(question=question).order_by('-create_date');

    paginator = Paginator(answer_list,10)
    page_obj = paginator.get_page(page)

    context = {'question': question, 'answer_list':page_obj}
    return render(request,'pybo/question_detail.html',context)



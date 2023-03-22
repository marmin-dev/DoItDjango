from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from common.forms import UserForm, PasswordResetForm
def signup(request):
    """
    회원가입
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password=raw_password)
            login(request,user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html',{'form':form})

class PasswordResetView(auth_views.PasswordResetView):
    """
    비밀번호 초기화 - 사용자ID, email 입력
    """
    template_name = 'common/password_reset.html'
    # success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm
    # email_template_name = 'common/password_reset_email.html'


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    """
    비밀번호 초기화 - 메일 전송 완료
    """
    template_name = 'common/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    """
    비밀번호 초기화 - 새로운 비밀번호 입력
    """
    template_name = 'common/password_reset_confirm.html'
    success_url = reverse_lazy('login')

def page_not_found(request, exception):
    """
    404 Page not found
    """
    return render(request,'common/404.html',{})
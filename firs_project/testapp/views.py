from django.shortcuts import render
from testapp.forms import usercreationform
# Create your views here.
def base_view(request):
    return render(request,'testapp/base.html')

def user_register(request):
    form=usercreationform()
    if request.method=='POST':
        form=usercreationform(request.POST)
        if form.is_valid():
            form.save()
        form=usercreationform()
    return render(request,'testapp/reg.html',{'form':form})





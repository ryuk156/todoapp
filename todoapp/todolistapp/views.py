from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import add
# Create your views here.

def home(request):
    if request.method=='POST':
        cont=request.POST['addtext']
        if cont is not None:
            ad=add(content=cont)
            ad.save()
            post=add.objects.all
            showall={'post':post}
            return render(request,"index.html",showall)
        

        
    else:
        post=add.objects.all
        showall={'post':post}
        return render(request,"index.html",showall)

        
def delete(request,list_id):
    item=add.objects.get(pk=list_id)    
    item.delete()
    return redirect('home')
    
def update(request,list_id):
    pass
    

    
        
    




       
        
    

    
    

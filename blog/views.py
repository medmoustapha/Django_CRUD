from django.shortcuts import render,redirect
from .models import Author, Article
from .forms import articleForm

from django.http import HttpResponse
# Create your views here.
def index(request):
    articles=Article.objects.all()
    return render(request,"index.html",{
        "articles":articles,
    })
def create_product(request):
    form=articleForm(request.POST or None)
    if form.is_valid() :
        form.save()
        return redirect('index')
    return render(request,'article-form.html',{ 'form':form})
def update_product(request,id):
    product=Article.objects.get(id=id)
    form=articleForm(request.POST or None,instance=product)
    if form.is_valid() :
        form.save()
        return redirect('index')
    return render(request,'article-form.html',{ 'form':form,'product':product})
def delete_product(request,id):
     product=Article.objects.get(id=id)
     if request.method == 'POST':
         product.delete()
         return redirect('index')
     return render(request,'prod-delete-confirm.html',{'product':product})
from django.shortcuts import render,redirect
from .models import Study

# Create your views here.
def index(request):
    data=Study.objects.all()
    context={"data":data}
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def addstudy(request):
    if request.method=="POST":
        sname=request.POST.get('studyname')
        phase=request.POST.get('studyphase')
        sponsor=request.POST.get('sponsorname')
        description=request.POST.get('description')
        query=Study(sname=sname,phase=phase,sponsor=sponsor,description=description)
        query.save()
    return render(request, "addstudy.html", {"message": "Study added successfully!"})

def selectdata(request,id):
    d=Study.objects.get(id=id)
    context={"d":d}
    return render(request,"select.html",context)

def updatedata(request,id):
    if request.method=="POST":
        sname=request.POST['studyname']
        phase=request.POST['studyphase']
        sponsor=request.POST['sponsorname']
        description=request.POST['description']
        edit=Study.objects.get(id=id)
        edit.sname=sname
        edit.phase=phase
        edit.sponsor=sponsor
        edit.description=description
        edit.save()
        return redirect("/")
    d=Study.objects.get(id=id)
    context={"d":d}
   
    return render(request,"update.html",context)

def delete(request):
    if request.method == "POST":
        record_ids = request.POST.getlist('ids')
        Study.objects.filter(id__in=record_ids).delete()  # Delete the records
        return redirect('/') 
    return render(request,"index.html")
    
   
    

    
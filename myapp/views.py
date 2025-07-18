from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.db import connections

def adminlogin(request):
    return render(request,"adminlogin.html")

def login_check(request):
    cursor=connections['default'].cursor()
    e=request.POST.get("email")
    p=request.POST.get("pass")
    sel="SELECT * FROM admin WHERE aemail='"+str(e)+"' AND apass='"+str(p)+"'"
    cursor.execute(sel)
    data=cursor.fetchall()
    if(len(data)>0):
        request.session['aid']=data[0][0]
        request.session['aname']=data[0][1]

        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponse("Invalid Login")
def logout(request):
    request.session['aid']
    request.session['aname']
    return HttpResponseRedirect('/adminlogin/')
def home(request):
    cursor = connections['default'].cursor()
    sel = "SELECT * FROM products"
    cursor.execute(sel)
    data = cursor.fetchall()
    desc = cursor.description
    alldata = [
        dict(zip([col[0] for col in desc], row))
        for row in data
    ]
    return render(request, "a.html", {'products': alldata})

def about(request):
    arr = {"msg": "I am API"}
    return JsonResponse(arr)

def addstd(request):
    return render(request, "addstd.html")

def insstd(request):
    n = request.POST.get("name")
    d = request.POST.get("dob")
    g = request.POST.get("gender")
    s = request.POST.get("stream")
    data = {'name': n, 'dob': d, 'gen': g, 'stream': s}
    return render(request, "insstd.html", data)

# Admin Panel
def dashboard(request):
    if 'aid' not in request.session:
        return HttpResponseRedirect('/adminlogin/')
    else:
        return render(request, "dashboard.html")

def addProduct(request):
    if 'aid' not in request.session:
        return HttpResponseRedirect('/adminlogin/')
    else:
        return render(request, "addProduct.html")

def insproduct(request):
    cursor = connections['default'].cursor()
    pn = request.POST.get("pname")
    pp = request.POST.get("pprice")
    pd = request.POST.get("pdetails")

    proimg = request.FILES['pimg']
    proimg_name = proimg.name
    with open("mysite/static/product_img/" + proimg_name, "wb+") as destination:
        for chunk in proimg.chunks():
            destination.write(chunk)

    ins = "INSERT INTO products (pname, pprice, pimg, pdetails) VALUES (%s, %s, %s, %s)"
    cursor.execute(ins, [pn, pp, proimg_name, pd])

    return HttpResponseRedirect('/listproducts/')

def listproducts(request):
    if 'aid' not in request.session:
        return HttpResponseRedirect('/adminlogin/')
    else:
        cursor = connections['default'].cursor()
        sel = "SELECT * FROM products"
        cursor.execute(sel)
        data = cursor.fetchall()
        desc = cursor.description
        alldata = [
            dict(zip([col[0] for col in desc], row))
            for row in data
            ]
    return render(request, "listproduct.html", {'products': alldata})

def delproduct(request):
    cursor = connections['default'].cursor()
    pid = request.POST.get("id")
    delp = "DELETE FROM products WHERE pid=%s"
    cursor.execute(delp, [pid])
    return HttpResponseRedirect('/listproducts/')

def editproduct(request):
    cursor = connections['default'].cursor()
    pid = request.POST.get("id")
    sel = "SELECT * FROM products WHERE pid=%s"
    cursor.execute(sel, [pid])
    data = cursor.fetchall()
    desc = cursor.description
    alldata = [
        dict(zip([col[0] for col in desc], row))
        for row in data
    ]
    return render(request, "editproduct.html", {'products': alldata})

def updproduct(request):
    cursor = connections['default'].cursor()
    pid = request.POST.get("id")
    pn = request.POST.get("pname")
    pp = request.POST.get("pprice")
    pd = request.POST.get("pdetails")

    if 'pimg' not in request.FILES:
        ins = "UPDATE products SET pname=%s, pprice=%s, pdetails=%s WHERE pid=%s"
        cursor.execute(ins, [pn, pp, pd, pid])
    else:
        proimg = request.FILES['pimg']
        proimg_name = proimg.name
        with open("mysite/static/product_img/" + proimg_name, "wb+") as destination:
            for chunk in proimg.chunks():
                destination.write(chunk)
        ins = "UPDATE products SET pname=%s, pprice=%s, pimg=%s, pdetails=%s WHERE pid=%s"
        cursor.execute(ins, [pn, pp, proimg_name, pd, pid])

    return HttpResponseRedirect('/listproducts/')

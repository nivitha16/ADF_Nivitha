from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
from .models import user_request, user_response
from .validations import check_vali

def home(request):
    return render(request, 'index.html')

def userinfosubmission(request):
    if request.method == "POST":
        f_name = request.POST["fn"]
        n_name = request.POST["mn"]
        l_name = request.POST["ln"]
        d_o_b = request.POST["d_o_b"]
        gn = request.POST["gn"]
        natio_name = request.POST["nm"]
        state_name = request.POST["sn"]
        pin_co = request.POST["pc"]
        quali = request.POST["qn"]
        sal = request.POST["ss"]
        pan = request.POST["pn"]

        data = user_request(first_name=f_name, middle_name=n_name, last_name=l_name, dob=d_o_b, gender=gn,
                          nationality=natio_name, state=state_name, pin_code=pin_co,
                          qualification=quali, salary=sal, pan_number=pan)

        data.save()
        #return HttpResponse("<h1>saved successfully</h1>")

        data1 = check_vali(d_o_b, gn, natio_name, state_name, sal)
        data2 = user_response(response=data1)
        data2.save()

        return HttpResponse(data1)
    return render(request, "index.html")




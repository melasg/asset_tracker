from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#from django.contrib.admin.views.decorators import staff_member_required



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
'''
@staff_member_required
def import(request):
	if request.method == "POST"
		form = DataImport(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			success = True
			context = {"form": form, "success":success}
			return render_to_response("imported.html", context,
				context_instance=RequestContext(request))
	else:
		form = DataImport()
		context = {"form":form}
		return render_to_response("imported.html", context, 
			context_instance=RequestContext(request))
'''

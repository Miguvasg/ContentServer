import logging
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from filemanage.models import Files

# Create your views here.

logger = logging.getLogger('webserver.filemanage.views')

class UploadView(View):
    template_name = 'upload.html'

    def post(self, request):
        data_to_save = Files(name=request.POST['file_name'], docfile=request.FILES['upload_file'])
        data_to_save.save()
        return render(request, self.template_name)

    def get(self, request):
        return render(request, self.template_name)

class DownloadListView(ListView):
    template_name = 'download.html'
    model = Files
    # def get(self, request):
    #     file_list = Files.objects.all()
    #     return render(request, self.template_name, {'files': file_list})
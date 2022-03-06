import logging
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from filemanage.models import Files
import traceback
from django.db.utils import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

logger = logging.getLogger('webserver.filemanage.views')

class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)

class UploadView(View):
    template_name = 'upload.html'

    def post(self, request):
        notes = ''
        try:
            data_to_save = Files(name=request.POST['file_name'],
                                 size=request.FILES['upload_file'].size,
                                 docfile=request.FILES['upload_file'])
            data_to_save.save()
            notes = 'archivo cargado'
        except IntegrityError:
            notes = 'no fue posible cargar el archivo, el nombre para el archivo ya existe'
        except MultiValueDictKeyError:
            notes = 'no fue posible cargar el archivo, no seleccionaste ningún archivo'
        except Exception as e:
            notes = 'ocurrió un error al subir el archivo'
        finally:
            return render(request, 'message.html', {'message': notes})

    def get(self, request):
        return render(request, self.template_name)

class DownloadListView(ListView):
    template_name = 'download.html'
    model = Files

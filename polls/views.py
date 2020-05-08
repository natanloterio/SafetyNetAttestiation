from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method == 'POST':
        return do_post(request)

    if request.method == 'GET':
        return HttpResponse("RESPOSTA")

def do_post(request):
    
    signed_attestation_stmt =  request.POST['param1']
    process(signed_attestation_stmt)
    return HttpResponse(signed_attestation_stmt)

def process(signed_attestation_stmt):
    smtm = parse_and_verify(signed_attestation_stmt)
    

def parse_and_verify(signed_attestation_stmt):
    
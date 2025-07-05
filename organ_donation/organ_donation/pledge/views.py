from django.shortcuts import render, redirect, get_object_or_404
from .forms import DonorForm
from .models import Donor
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Handles pledge form
def pledge_view(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            donor = form.save()
            # Redirect to generate PDF after successful form submission
         

            return redirect('generate_certificate', donor_id=donor.id)
    else:
        form = DonorForm()
    return render(request, 'pledge/pledge_form.html', {'form': form})


# Shows all pledges
def donor_list(request):
    donors = Donor.objects.all().order_by('-date_pledged')
    
    return render(request, 'donor_list.html', {'donors': donors})


# Generates PDF certificate
def generate_certificate(request, donor_id):
    donor = get_object_or_404(Donor, id=donor_id)
    template = get_template('pledge/certificate.html')  # make sure path is correct
    html = template.render({'donor': donor})
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{donor.name}_certificate.pdf"'
    
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)
    
    return response
from .forms import RecipientForm
from .models import Recipient

def recipient_register(request):
    if request.method == 'POST':
        form = RecipientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipient_list')
    else:
        form = RecipientForm()
    return render(request, 'recipient_form.html', {'form': form})

def recipient_list(request):
    recipients = Recipient.objects.all().order_by('-urgency_level', 'date_added')
    return render(request, 'recipient_list.html', {'recipients': recipients})

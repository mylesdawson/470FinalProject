from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Contact

class IndexView(generic.ListView):
    template_name = 'contacts/index.html'
    context_object_name = 'latest_contact_list'

    def get_queryset(self):
        return Contact.objects.all()

class DetailView(generic.DetailView):
    model = Contact
    template_name = 'contacts/detail.html'

class EditView(generic.DetailView):
    model = Contact
    template_name = 'contacts/edit.html'

class NewView(generic.ListView):
    model = Contact
    template_name = 'contacts/new.html'

def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)

    contact.first_name = request.POST['first_name']
    contact.last_name = request.POST['last_name']
    contact.email = request.POST['email']
    contact.phone_number = request.POST['phone_number']
    contact.notes = request.POST['notes']
    
    contact.save()

    return HttpResponseRedirect(reverse('contacts:detail', args=(contact.id,)))

def add_contact(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    notes = request.POST['notes']

    new_contact = Contact(first_name=first_name, last_name=last_name,
        email=email, phone_number=phone_number, notes=notes)

    new_contact.save()

    return HttpResponseRedirect(reverse('contacts:index'))
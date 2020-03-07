from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Note, AddNoteForm
from django.contrib import messages
import json, os
from datetime import datetime, timedelta 
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from io import BytesIO
from django.conf import settings
from django.template.loader import get_template
#from django.core.signing import BadSignature
from taggit.models import Tag

def welcomepage(request):
    return render(request, 'welcome.html')

def home(request):
    notes = Note.objects.filter(user=request.user).order_by('-updated_at')[:10]
    all_notes = Note.objects.filter(user=request.user).order_by('-updated_at')

    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.user = request.user
            form_data.save()
            # Without this next line the tags won't be saved.
            form.save_m2m()
            form = AddNoteForm()
            messages.success(request, 'Note added successfully!')
            return redirect('notes')
    else:
        form = AddNoteForm()
   
    context = {
        'notes': notes,
        'all_notes': all_notes,
        'add_note_form': form,
    }
    return render(request, 'notes.html', context)


def get_note_details(request, slug):
    note = get_object_or_404(Note, slug=slug)
    if note.user != request.user:
        messages.error(request, 'You are not authenticated to perform this action')
        return redirect('notes')

    notes = Note.objects.filter(user=request.user).order_by('-updated_at')[:10]
    add_note_form = AddNoteForm()

    absolute_url = request.build_absolute_uri(note.get_absolute_url())

    context = {
        'notes': notes,
        'note_detail': note,
        'add_note_form': add_note_form,
        'absolute_url': absolute_url
    }
    return render(request, 'note_details.html', context)


def edit_note_details(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if note.user != request.user:
        messages.error(request, 'You are not authenticated to perform this action')
        return redirect('notes')
    if request.method == 'POST':
        form = AddNoteForm(request.POST, instance=note)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.user = request.user
            form_data.save()
            form.save_m2m()
            return redirect('note_detail', slug=note.slug)
    else:
        form = AddNoteForm(initial={
            'note_title': note.note_title,
            'note_content': note.note_content,
            'tags': ','.join([i.slug for i in note.tags.all()]),
        }, instance=note)
        return render(request, 'modals/edit_note_modal.html', {'form': form})


def confirm_delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if note.user != request.user:
        messages.error(request, 'You are not authenticated to perform this action')
        return redirect('notes')
    # note.delete()
    context = {
        'note_detail': note,
    }
    return render(request, 'modals/delete_note_modal.html', context)

def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if note.user != request.user:
        messages.error(request, 'You are not authenticated to perform this action')
        return redirect('notes')
    note.delete()
    messages.success(request, 'Note deleted successfully!')
    return redirect('notes')


def search_note(request):
    if request.is_ajax():
        q = request.GET.get('term')
        notes = Note.objects.filter(
                note_title__icontains=q,
                user=request.user
            )[:10]
        results = []
        for note in notes:
            note_json = {}
            note_json['slug'] = note.slug
            note_json['label'] = note.note_title
            note_json['value'] = note.note_title
            results.append(note_json)
        data = json.dumps(results)
    else:
        note_json = {}
        note_json['slug'] = None
        note_json['label'] = None
        note_json['value'] = None
        data = json.dumps(note_json)
    return HttpResponse(data)


def get_shareable_link(request, signed_pk):
    try:
        #pk = Note.signer.unsign(signed_pk)
        pk = signed_pk
        note = Note.objects.get(pk=pk)
        context = {
            'note_detail': note
        }
        return render(request, 'shared_note.html', context)
    #except (BadSignature, Note.DoesNotExist):
    #raise Http404('No Order matches the given query.')
    except:
        pass


def get_all_notes_tags(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    all_notes = Note.objects.filter(tags=tag, user=request.user)
    notes = Note.objects.filter(user=request.user).order_by('-updated_at')[:10]
    add_note_form = AddNoteForm()
    context = {
        'tag':tag,
        'all_notes':all_notes,
        'notes': notes,
        'add_note_form': add_note_form
    }
    return render(request, 'tags.html', context)
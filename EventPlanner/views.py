from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_list_or_404

def event_index(request):
    events = Event.objects.all()
    return render(request, 'event_index.html', {'events': events})

def event_add(request):
    if request.method == 'POST':
        new_event = Event(
            title = request.POST.get('title'),
            description = request.POST.get('description'),
            date = request.POST.get('date'),
            location = request.POST.get('location')
        )
        new_event.save()
        return redirect('event_index')
    return render(request, 'event_add.html')

def event_edit(request, title): # იქიდან გამომდინარე, რომ შესაძლოა ივენთებს ჰქონდეთ ერთი და იგივე სახელი, 
                                # კოდი მუშაობს ასე: ჯერ ცდის სახელით წამოღებას ცხრილიდან, თუ რამდენიმე ობიექტი წამოვიდა დაამუშაოს 
                                # except ბლოკმა, რომელიც საშუალებას აძლევს მომხარებელლს ერთი და იგივე სახელიანი ობიექტებიდან 
                                # ხელახლა გააგზავნოს requestი იგივე viewsზე ოღონდ ამჟამად აიდის მიხედვით, რომელიც უნიკალურია
    try:
        if title.isnumeric():
            title = int(title)
            events = Event.objects.get(id = title)
        else:
            events = Event.objects.get(title = title)

        if request.method == 'POST':
            events.title = request.POST.get('title')
            events.description = request.POST.get('description')
            events.date = request.POST.get('date')
            events.location = request.POST.get('location')

            events.save()
            return redirect('event_index')
        return render(request, 'event_edit.html', {'events': events})

    except Event.MultipleObjectsReturned:
        # event = Event.objects.filter(title = title)
        events = get_list_or_404(Event, title=title) # Works the same as objects.filter()
        return render(request, 'event_edit.html', {'events': events})
    
    # აქ დასამთავრებელი მაქვს თვითონ editის ფუნქციონალი

    # როცა მხოლოდ ერთ ობიექტს წამოიღბს, მაგ if ბლოკში უნდა დაემატოს ფორმა რომლითაც დააფდეითდება ივენთი

def event_delete(request, title):
    try:
        if title.isnumeric():
            title = int(title)
            events = Event.objects.get(id = title)
        else:
            events = Event.objects.get(title = title)
        if request.method == 'POST':
            events.delete()
            return redirect('event_index')
        return render(request, 'event_delete.html', {'events': events})
    
    except Event.MultipleObjectsReturned:
        events = get_list_or_404(Event, title = title)
        return render(request, 'event_delete.html', {'events': events})

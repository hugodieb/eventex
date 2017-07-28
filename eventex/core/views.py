from django.shortcuts import render, get_object_or_404

from eventex.core.models import Speaker, Talk


def home(request):
    speakers = Speaker.objects.all()
    return render(request, 'index.html', {'speakers': speakers})

def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'core/speaker_detail.html', {'speaker':speaker})

def talk_list(request):
    speaker = Speaker(name='Hugo Dieb', slug='hugo-dieb')
    courses = [
        dict(title='Título do Curso',
             start='9:00',
             description='Descrição do Curso',
             speakers={'all': [speaker]})
    ]
    context = {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(),
        'courses': courses
    }
    return render(request, 'core/talk_list.html', context)

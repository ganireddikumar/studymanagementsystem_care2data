import logging
from django.shortcuts import render, get_object_or_404, redirect
from .models import Study
from .forms import StudyForm

# Initialize logger
logger = logging.getLogger(__name__)

def study_list(request):
    try:
        studies = Study.objects.all()
        return render(request, 'studies/study_list.html', {'studies': studies})
    except Exception as e:
        logger.error(f"Error fetching studies: {str(e)}")
        return render(request, 'studies/error.html', {'error': "Error fetching studies."})

def add_study(request):
    if request.method == "POST":
        form = StudyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('study_list')
            except Exception as e:
                logger.error(f"Error saving study: {str(e)}")
                return render(request, 'studies/error.html', {'error': "Error saving study."})
    else:
        form = StudyForm()
    return render(request, 'studies/add_study.html', {'form': form})

def view_study(request, pk):
    try:
        study = get_object_or_404(Study, pk=pk)
        return render(request, 'studies/view_study.html', {'study': study})
    except Exception as e:
        logger.error(f"Error viewing study: {str(e)}")
        return render(request, 'studies/error.html', {'error': "Error viewing study."})

def edit_study(request, pk):
    study = get_object_or_404(Study, pk=pk)
    if request.method == "POST":
        form = StudyForm(request.POST, instance=study)
        if form.is_valid():
            try:
                form.save()
                return redirect('study_list')
            except Exception as e:
                logger.error(f"Error updating study: {str(e)}")
                return render(request, 'studies/error.html', {'error': "Error updating study."})
    else:
        form = StudyForm(instance=study)
    return render(request, 'studies/edit_study.html', {'form': form, 'study': study})


# Delete Study
def delete_study(request, pk):
    study = get_object_or_404(Study, pk=pk)
    if request.method == "POST":
        study.delete()
        return redirect('study_list')
    return render(request, 'studies/delete_study.html', {'study': study})
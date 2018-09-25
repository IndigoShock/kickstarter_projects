from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Project


def project_list_view(request):
    # import pdb; pdb.set_trace()
    projects = get_list_or_404(Project)

    context = {
        'projects': projects
    }

    return render(request, 'projects/project_list.html', context)


def project_detail_view(request, pk):
    context = {
        'project': get_object_or_404(Project, pk=pk)
    }

    return render(request, 'projects/project_detail.html', context)

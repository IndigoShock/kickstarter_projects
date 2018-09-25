from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from .models import Project


def project_list_view(request):
    # import pdb; pdb.set_trace()
    projects_query = get_list_or_404(Project)
    paginator = Paginator(projects_query, 20)

    page = request.GET.get('page')
    projects = paginator.get_page(page)

    context = {
        'projects': projects
    }

    return render(request, 'projects/project_list.html', context)


def project_detail_view(request, pk):
    context = {
        'project': get_object_or_404(Project, pk=pk)
    }

    return render(request, 'projects/project_detail.html', context)

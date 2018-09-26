from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.conf import settings
from .models import Project


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
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
        'project': get_object_or_404(Project, ID=pk)
    }

    return render(request, 'projects/project_detail.html', context)

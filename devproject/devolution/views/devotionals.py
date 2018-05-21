from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404
from devolution.models.devotional import Devotional, lookup_devotional


def devotionals(request):
    devotionals_list = get_list_or_404(Devotional)
    return render(request, 'devolution/main.html', {'devotionals_list': devotionals_list})


def title_page(request, devo_id):
    devo = lookup_devotional(devo_id)
    if devo is not None:
        return render(request, 'devolution/title.html', {'devo': devo})
    else:
        raise Http404("Devotional not found")


def table_of_contents(request, devo_id):
    devo = lookup_devotional(devo_id)
    if devo is not None:
        return render(request, 'devolution/contents.html',
                      {'devo': devo, 'entries': devo.entry_set.order_by('sequenceNum')})
    else:
        raise Http404("Devotional not found")


def entry(request, devo_id, entry_id):
    return HttpResponse("You're looking at the devotional entry: '%s / %s'" %
                        (devo_id, entry_id))


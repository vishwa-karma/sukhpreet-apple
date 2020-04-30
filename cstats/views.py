from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import ClusterForm
from .models import Cluster

# Create your views here.
def cluster_list(request):
    clusters = Cluster.objects.all()
    context = {'clusters':clusters}
    return render(request, 'cstats/clusters.html',{'clusters':clusters})


def cluster_edit(request,pk):
    post = get_object_or_404(Cluster, pk=pk)
    if request.method == "POST":
        form = ClusterForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('cstats:cluster_list')
    else:
        form = ClusterForm(instance=post)
    return render(request, 'cstats/cluster_edit.html', {'form': form})


from django.shortcuts import render, redirect
from django.urls import reverse
from rbac import models
from rbac import forms


# Create your views here.
def roles_list(request):
    """
    增加角色
    :param request:
    :return:
    """
    queryset = models.Role.objects.all()
    return render(request, 'rbac/roles_list.html', {'queryset': queryset, "username": request.session.get("user_info").get("name")})


def roles_add(request):
    """
    增加角色
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = forms.RolesModelForm()
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})

    form = forms.RolesModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('roles_list'))
    return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})


def roles_edit(request, nid):
    """

    :param request:
    :return:
    """
    obj = models.Menu.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = forms.RolesModelForm(instance=obj)
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})
    form = forms.RolesModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('roles_list'))
    else:
        return render(request, 'form.html', {'form': form, "username": request.session.get("user_info").get("name")})


def roles_del(request, nid):
    """

    :param request:
    :return:
    """
    models.Menu.objects.filter(id=nid).delete()
    return redirect(reverse('roles_list'))

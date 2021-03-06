from django.shortcuts import render, HttpResponse


# Create your views here.

def upload(request):
    """
    上传文件操作
    :param request: 
    :return: 
    """
    if request.method == "POST":
        # 从上传的文件数据中拿到 avatar对应的文件对象
        file_obj = request.FILES.get("avatar")
        # 在服务端新建一个和上传文件同名的新文件
        with open(file_obj.name, "wb") as f:
            # 从上传文件对象中一点一点读数据
            for i in file_obj:
                # 写入服务端新建的文件
                f.write(i)
        return HttpResponse("上传成功")

    return render(request, "upload.html")


def upload_ajax(request):
    """
    使用ajax方式上传
    :param request:
    :return:
    """
    return render(request, "upload_ajax.html")


def upload_avatar(request):
    """
    预览头像并上传
    :param request:
    :return:
    """
    return render(request, "upload_avatar.html")

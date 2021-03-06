from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
import random
from django.contrib.auth.decorators import login_required
from fault_reporting.forms import UserUpdateForm
from fault_reporting.forms import RegisterForm
from fault_reporting import models
from django.http import JsonResponse
from django.forms import model_to_dict
from django.db.models import Count


# Create your views here.


def register(request):
    """
    用户注册
        1. 前端使用ajax提交
        2. res 返回给前端js的字典，前端用过判断code值来返回对应的页面。
    :param request:
    :return:
            1. get 请求，返回form_obj对象，在页面展示
            2. post 请求,
                1. 生成一个res字典用于返回给前端页面
                2. 拿到request.POST中的数据去form_obj中校验
                3. form_obj.is_valid 如果校验通过，开始创建数据
                    1. 由于RegisterForm 中没有re_password字段，需要先删除cleaned_data中删除
                    2. 头像（avatar）无法从cleaned_data中获取，需要从request.FILES.get中获取时刻
                    3. 拿到数据开始创建，由于密码是加密的，所以需要使用create_user创建，而不是直接
                        使用orm 的 create创建，**form_obj.cleaned_data 是打散字典的操作，头像赋值给
                        avatar
                    4. 创建成功给用户返回一个url
                4. 校验失败
                    1. 把校验状态改成1， 并返回错误信息
                5. 通过JsonResponse返回字典给JS，这里返回的是json字典对象。前端可以做响应的处理
    """
    form_obj = RegisterForm()
    if request.method == "POST":
        res = {"code": 0}
        form_obj = RegisterForm(request.POST)
        if form_obj.is_valid():
            form_obj.cleaned_data.pop("re_password")
            avatar_obj = request.FILES.get("avatar")
            models.UserInfo.objects.create_user(**form_obj.cleaned_data, avatar=avatar_obj)
            res["url"] = "/login/"
        else:
            res["code"] = 1
            res["error"] = form_obj.errors
        return JsonResponse(res)

    return render(request, "register.html", locals())


def login(request):
    """
    用户登录页面
        1. get 请求： 返回用户登录页面，用户登录的时候不需要显示用户名，user = ""
        2. post 请求：
                    1. 取到用户名，密码，请求的页面，验证码
                    2. 忽略验证码大写小，判断验证码和session中存的是否一致
                        1. 验证码一致，
                        2. 使用auth组件的authenticate方法校验用户
                            1. 校验通过
                            2. 使用auth组件login方法创建session
                            3. 并返回用户请求页面，如果没有默认请求页面则跳转到/index/页面
                                next = request.GET.get("next", "/index/") 如果取不到next的值，默认值是/index/
                        3. 校验失败 返回错误信息给页面，并返回用户名给input的value，不需要用户在填用户名
                    3. 验证码不一致，则返回错误页面，并返回用户给input的value，不要用户在填写用户名
    :param request:
    :return:
    """

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password")
        next = request.GET.get("next", "/index/")
        v_code = request.POST.get("v_code")
        if v_code.upper() == request.session.get("v_code"):
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(next)
            else:
                return render(request, "login.html", {"error_msg": "*用户或者密码错误！", "user": username})
        else:
            return render(request, "login.html", {"code_msg": "*验证码有误！", "user": username})

    return render(request, "login.html", {"user": ""})


def index(request, *args):
    """
    首页
        1. 在前端页面需要显示的分类（两种方法：1、反向查询（一次查询操作2张表） 2、聚合分组查询（效率高））
                1. class_list 通过分组聚合取到所有的产品线名称，只取name和num字段
                2. tag_list 通过分组聚合取所有的表标签名称,只取name和num字段
                3. archive_list 由于orm没有时间格式化的功能，需要通过orm执行原生sql，时间格式化只取年-月(2018-9)，
                    只取日期和num字段，当使用mysql的时候需要这样写：
                    select={"ym": "date_format(create_time, '%%Y-%%m')"}  # MySQL日期格式化的写法
        2. user = 通过auth取到用户名
        3. 如果args没有值，返回index页面，并返回所有的报障信息 
            fault_list = 默认显示所有的报障内容
        4. 如果args有值，并且是2个值
            1. 如果args[0] == "class"  fault_list  = 对应产品线的名称
            2. 如果args[0] == "tag":   fault_list  = 对应标签的名称
            3. 如果args[0] == "archive":  fault_list  =  对应月份的时间
                注意：  year, month = args[1].split("-") 只能切割 2018-9类似这样格式的日期，如果是其他格式则会报错，这里
                        使用try捕捉异常，如果捕捉到 fault_list = []
    :param request:
    :param args  args[0] = class|tag|archive
                 args[1] = classify__name|tags__name|时间（2018-9）
    :return:
    """
    user = auth.get_user(request).username
    class_list = models.Classify.objects.all().annotate(num=Count("fault")).values("name", "num")
    tag_list = models.Tag.objects.all().annotate(num=Count("fault")).values("name", "num")
    archive_list = models.Fault.objects.all().extra(select={
        "ym": "strftime('%%Y-%%m', create_time)"}).values("ym").annotate(num=Count("id")).values("ym", "num")
    fault_list = models.Fault.objects.all()
    if args and len(args) == 2:
        if args[0] == "class":
            fault_list = fault_list.filter(classify__name=args[1])
        elif args[0] == "tag":
            fault_list = fault_list.filter(tags__name=args[1])
        else:
            try:
                year, month = args[1].split("-")
                fault_list = fault_list.filter(create_time__year=year, create_time__month=month)
            except Exception:
                fault_list = []

    return render(request, "index.html", locals())


@login_required
def logout(request):
    """
    注销用户
         auth.logout 删除session并返回到登录页面
    :param request:
    :return:
    """
    auth.logout(request)
    return redirect("/login/")


@login_required
def p_center(request):
    """
    编辑中心
        1. 取到当前用户名
        2. 根据用户名取到用户对象（即orm对象）
        3. 请求是get :
            1. 把用户对象转成字典 model_to_dict（）
            2. 把用户对象传值给form并返回给页面
        4. 请求是post ：
            1. 拿到request.POST中数据到form进行校验
            2. 如果校验通过
                1. 更新cleaned_data中的数据到orm对象中
                2. 文件格式的数据需要request.FILES.get("avatar")取值，
                    1. 用户编辑头像的时候没有修改头像，则使用原来的头像，如果传值了则使用新值
                3. 保存对象
                4. 并返回到个人中心页面
    :param request:
    :return:
    """
    user = auth.get_user(request)
    user_obj = models.UserInfo.objects.filter(username=user).first()
    user_dict = model_to_dict(user_obj)
    form_obj = UserUpdateForm(user_dict)
    if request.method == "POST":
        form_obj = UserUpdateForm(request.POST)
        if form_obj.is_valid():
            user_obj.phone = form_obj.cleaned_data.get("phone")
            user_obj.email = form_obj.cleaned_data.get("email")
            user_obj.avatar = request.FILES.get("avatar") if request.FILES.get("avatar") else user_obj.avatar
            user_obj.save()
            return redirect("/p_center/")

    return render(request, "p_center.html", locals())


@login_required
def set_password(request):
    """
    修改密码
        1. get 请求 返回修改密码页面
        2. post 请求 
            1. 用户POST中取到 原始密码，新密码，确认密码
            2. 使用auth组件对原始密码进行校验
                1. 校验通过
                    1. 对比新密码和确认密码是否一致，如果不一致则返回错误页面
                    2. 如果一致，则使用auth修改密码，并保存
                    3. 跳转到 index 页面
                2. 校验不通过
                    返回错误信息
    :param request:
    :return:
    """
    user = auth.get_user(request)
    if request.method == "POST":
        password_old = request.POST.get("password_old")
        password_new_1 = request.POST.get("password_new_1")
        password_new_2 = request.POST.get("password_new_2")

        if user.check_password(password_old):
            if password_new_1 == password_new_2:
                user.set_password(password_new_2)
                user.save()
                return redirect("/index/")
            else:
                return render(request, "set_password.html", {"user": user, "error_msg_pwd": "*两次密码不一致"})
        else:
            return render(request, "set_password.html", {"user": user, "error_msg": "*原始密码不正确"})

    return render(request, "set_password.html", {"user": user})


def v_code(request):
    """
     随机验证码
        1. ImageDraw.Draw 创建一个随机颜色的图片对象
        2. ImageFont.truetype 加载一个字体对象
        3. for i in range(5) 生成随机5位验证码
            1. 包含大小写字母，数字
            2. 每生成一个写到图片上，draw_obj.text((15 * i + 10, 0), r, fill=random_color(), font=font_obj)
        4. 将验证码保存到session中
        5. from io import BytesIO 直接在内存中保存图片替代io操作
    :param request:
    :return:
    """
    from PIL import Image, ImageDraw, ImageFont

    def random_color():
        """
        定义一个生成随机颜色代码的函数
        :return: 返回一个随机颜色，元组格式的rgb
        """
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    image_obj = Image.new(
        "RGB",
        (100, 33),
        (255, 255, 140)
    )
    draw_obj = ImageDraw.Draw(image_obj)
    font_obj = ImageFont.truetype('static/fonts/kumo.ttf', 28)
    tmp = []
    for i in range(5):
        l = chr(random.randint(97, 122))
        u = chr(random.randint(65, 90))
        n = str(random.randint(0, 9))
        r = random.choice([l, u, n])
        draw_obj.text((15 * i + 10, 0), r, fill=random_color(), font=font_obj)
        tmp.append(r)

    # 添加干扰线
    width = 250  # 图片宽度（防止越界）
    height = 35
    for i in range(3):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw_obj.line((x1, y1, x2, y2), fill=random_color())

    # 添加噪点
    for i in range(20):
        draw_obj.point([random.randint(0, width), random.randint(0, height)], fill=random_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw_obj.arc((x, y, x + 4, y + 4), 0, 90, fill=random_color())
    v_code = "".join(tmp).upper()
    request.session["v_code"] = v_code
    from io import BytesIO
    f1 = BytesIO()
    image_obj.save(f1, format="PNG")
    img_data = f1.getvalue()
    return HttpResponse(img_data, content_type="image/png")

#!/usr/bin/python
# -*- coding:utf-8 -*-
import json
import requests
import os
from config import settings
from .base import BaseHandler
from ..plugins import get_server_info


class AgentHandler(BaseHandler):
    """
    继承BaseHandler，继承类的属性并现实接口方法
    """
    def cmd(self, command, hostname=None):
        """
        使用agent引擎采集，agent运行在需要采集的主机上面调用subprocess可直接执行采集命令
        :param command: 采集指令（处理任意的采集指令，不局限于网卡，硬盘，内存）
        :param hostname: 需要采集的主机，agent模式不需要获取此参数
        :return: 采集结果（未处理）
        """
        import subprocess
        return subprocess.getoutput(command)

    def handler(self):
        """
        处理Agent模式下的资产采集：网卡、内存、硬盘
        1. 使用get_server_info获取所有资产的信息：网卡，内存，硬盘...
        2. 发送采集结果给api
        3. 打印api返回值
        :return:
        """
        info = get_server_info(self)
        # 获取采集到的主机名
        hostname = info.get("basic").get("data").get("hostname")

        # 判断主机名是否修改
        # 1. 新的主机，直接汇报
        if not os.path.exists(settings.CERT_FILE_PATH):
            """
            如果文件不存在，则是新的主机，直接汇报即可
            """
            info["type"] = "create"
        # 2. 已经存在的主机，更新
        else:
            with open(settings.CERT_FILE_PATH, "r") as f:
                cert_hostname = f.read()
            # 1. 如果没有更新主机名则直接汇报更新
            if hostname == cert_hostname:
                info["type"] = "update"
            # 2. 更新了主机名，需要更新主机名
            else:
                info["cert"] = cert_hostname
                info["type"] = "update_hostname"

        r1 = requests.post(
            url=self.asset_api,
            data=json.dumps(info).encode('utf-8'),
            headers={
                'Content-Type': 'application/json'
            }
        )
        result = r1.json()

        # 如果采集主机成功，则把主机名写入到cert文件中
        if result.get("status"):
            with open(settings.CERT_FILE_PATH, "w") as f:
                f.write(result.get("hostname"))

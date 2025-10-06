#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
用户登录功能测试脚本
"""

import requests
import json

# 服务器地址
BASE_URL = "http://localhost:8000"

def test_register():
    """测试用户注册"""
    print("测试用户注册...")

    # 注册数据
    register_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword123"
    }

    try:
        response = requests.post(f"{BASE_URL}/auth/register", json=register_data)
        print(f"注册响应状态码: {response.status_code}")
        print(f"注册响应内容: {response.json()}")

        if response.status_code == 200:
            print("用户注册成功!")
            return response.json()
        else:
            print(f"注册失败: {response.text}")
            return None
    except Exception as e:
        print(f"注册请求异常: {e}")
        return None

def test_login():
    """测试用户登录"""
    print("\n测试用户登录...")

    # 登录数据
    login_data = {
        "username": "testuser",
        "password": "testpassword123"
    }

    try:
        response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
        print(f"登录响应状态码: {response.status_code}")
        print(f"登录响应内容: {response.json()}")

        if response.status_code == 200:
            print("用户登录成功!")
            return response.json()
        else:
            print(f"登录失败: {response.text}")
            return None
    except Exception as e:
        print(f"登录请求异常: {e}")
        return None

def test_wrong_password():
    """测试错误密码登录"""
    print("\n测试错误密码登录...")

    # 错误的登录数据
    login_data = {
        "username": "testuser",
        "password": "wrongpassword"
    }

    try:
        response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
        print(f"错误密码登录响应状态码: {response.status_code}")
        print(f"错误密码登录响应内容: {response.json()}")

        if response.status_code == 401:
            print("正确处理了错误密码!")
        else:
            print(f"未正确处理错误密码: {response.text}")
    except Exception as e:
        print(f"错误密码登录请求异常: {e}")

def main():
    """主函数"""
    print("开始测试用户登录功能...")

    # 先测试注册
    register_result = test_register()

    # 如果注册成功，测试登录
    if register_result:
        login_result = test_login()

        # 测试错误密码
        test_wrong_password()

        print("\n测试完成!")
    else:
        print("注册失败，无法继续测试登录功能")

if __name__ == "__main__":
    main()
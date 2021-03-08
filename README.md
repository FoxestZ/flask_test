项目说明
===========================

###########环境依赖

    Flask==1.1.2
    
    Flask_Script==2.0.6
    
    Flask_SQLAlchemy==2.4.1
    
    alembic==0.9.3
    
    Flask_Mail==0.9.1
    
    Flask_Migrate==2.0.4
    
    Werkzeug==1.0.1
    
    SQLAlchemy==1.3.15
    
    gunicorn
    
    gevent

###########部署步骤
1. 下载并安装成功mysql

2. 根据实际需求（拟使用的本地 MySQL 服务器登录用户名及密码）修改config.py中的参数

        USERNAME = 'root'
            
        PASSWORD = '123456'

3. 根据config.py中的“ DATABASE = 'zlktqa_demo' ”创建数据库

        create DATABASE zlktqa_demo    
        
4. 根据requirements.txt 创建并进入虚拟环境

    win10用户：
    
        mkvirtualenv 307demo
        workon 307demo
     
     进入项目根目录
     
        pip install -r requirements.txt

5. 控制台cd进入项目根目录，并创建数据表及映射 

        cd [项目根目录路径]
        python manage.py db init   
        python manage.py db migrate   

    ######若migrations目录，删除migrations目录所以文件（2021-3-8更新，此步无需进行）
    
6. 运行项目

        python.exe -m flask run


###########V1.0.0 版本内容更新（2021-3-7更新）
1. 新更改	加入了Dockerfile、gunicorn.conf.py（暂时无法使用） 

##
###########V1.0.1 版本内容更新（2021-3-8更新）
1. 新更改	针对复现中实验环境运行产生的BUG

        “ModuleNotFoundError: No module named 'MySQLdb'” 
   参考https://www.it610.com/article/1297037632215261184.htm 对exts.py
   、requirements.txt 进行小幅度修改
   
2. 新更改	针对复现实验环境中,以命令行代码形式运行代码时的问题，将项目项目运
   行入口文件名修改为
   
        app.py
   
##
###########个人学习笔记

2021-3-7更新：

学习了Docker的部署
#
主要参考：https://zhuanlan.zhihu.com/p/160842402
#
小结：

    Docker打包镜像，对windows用户不太友好，不能在打包前使用
    gunicorn命令run，调试。只能打包成镜像后在docker容器中运行才能
    通过运行结果进行调试
#


建议：


    win10用户，建议项目在本地正常调试完毕后再进行docker打包
    另外此次实验发现命令
    
    “docker run -it --rm -p 5000:5000 [项目ID]”
    
    运行后不知如何查看docker分配的IP地址
    后使用命令
    
    “ docker run -d -p 127.0.0.1:5001:5000 [项目ID]  (默认绑定tcp端口)”
    
    （参考https://blog.csdn.net/qq_38695182/article/details/81583432）
    
    点击127.0.0.1:5001成功访问
    
    (反思后认为可通过https://www.runoob.com/docker/docker-container-usage.html 
    的“运行一个 web 应用”进行ip地址查看问题的参考)



#

###########其他说明：

    RandomMath.py 为实现了一半的邮箱验证码验证模块，暂不参与到项目
    的正常运行
#
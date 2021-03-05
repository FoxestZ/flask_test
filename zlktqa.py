from flask import Flask, request, session, redirect, url_for
from flask import render_template #后台渲染模板
from models import User,Question,Answer
import config
from exts import db
from edcorators import login_required
from flask_mail import Message,Mail


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
mail = Mail()


# @app.route('/')
# def hello_world():
#     return render_template('index.html')
    # return render_template('text.html')

@app.route('/')
def hello_world():
    context = {
        'questions': Question.query.order_by('create_time').all()
        # 按照时间（.order_by('create_time')）进行排序
    }
    return render_template('index.html' ,**context)

# @app.route('/1/')
# def test():
#     # return render_template('index.html')
#     return render_template('text.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone,User.password == password).first()
        if user:
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('hello_world'))
        else:
            return u'手机号码或者密码错误，请确认后再登录！'






@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # 手机号码验证，如果被注册了，就不能再注册了
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return u'该手机号码已被注册，请更换手机号码！'
        else:
            # password1要和password2相等才可以
            if password1 != password2:
                return u'两次密码不相等，请核对后再填写！'
            else:
                user = User(telephone=telephone, username=username, password=password1)
                db.session.add(user)
                db.session.commit()
                # 如果注册成功，就让页面跳转到登录的页面
                return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    # session.pop('user_id')
    # del session['user_id']
    session.clear()  #退出全部
    return redirect(url_for('login'))


@app.route('/question/', methods=['GET', 'POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title, content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        question.author = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('hello_world'))

@app.route('/detail/<question_id>')
def detail(question_id):
    question_model = Question.query.filter(Question.id == question_id).first()
    return render_template('detail.html', question=question_model)


@app.route('/add_answer/',methods=['POST'])
@login_required
def add_answer():
    content = request.form.get('answer_content')
    question_id = request.form.get('question_id')
    user_id = session['user_id']
    user = User.query.filter(User.id == user_id).first()
    answer = Answer(content=content)
    answer.author = user
    question = Question.query.filter(Question.id == question_id).first()
    answer.question = question
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('detail', question_id=question_id))

@app.route('/search/')
def search():
    search_content = request.args.get('search_content')
    # title,content
    # 或
    # condition = or_(Question.title.contains(q),Question.content.contains(q))
    # questions = Question.query.filter(condition).order_by('-create_time')
    # 与
    questions = Question.query.filter(Question.title.contains(search_content), Question.content.contains(search_content))
    return render_template('index.html', questions=questions)


# @app.route('/email_captcha/')
# @login_required
# def email_captcha():
#   email = request.args.get('email')
#   if not email:
#     return restful.params_error('请输入邮箱') #restful. 封装的函数，返回前端数据
#   '''
#   生成随机验证码，保存到memcache中，然后发送验证码，与用户提交的验证码对比
#   '''
#   captcha = str(uuid.uuid1())[:6] # 随机生成6位验证码
#   # 给用户提交的邮箱发送邮件
#   message = Message('Python论坛邮箱验证码', recipients=[email], body='您的验证码是：%s' % captcha)
#   try:
#     mail.send(message) # 发送
#   except:
#     return restful.server_error()
#   mbcache.set(email, captcha)
#   return restful.success()


@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        return {'user': user}
    return {}


if __name__ == '__main__':
    app.run()

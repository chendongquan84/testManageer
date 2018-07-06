# -*- coding:utf-8 -*- 
'''
Created on 2016年1月20日

@author: chendq
'''
import web
from web import form
from pip._vendor.distlib._backport.tarfile import pwd

render = web.template.render('templates') # your templates

vpass = form.regexp(r".{3,20}$", 'must be between 3 and 20 characters')
vemail = form.regexp(r".*@.*", "must be a valid email address")

register_form = form.Form(
    form.Textbox("username", description="Username"),
    form.Textbox("email", vemail, description="E-Mail"),
    form.Password("password", vpass, description="Password"),
    form.Password("password2", description="Repeat password"),
    form.Button("submit", type="submit", description="Register"),
    validators = [
        form.Validator("Passwords did't match", lambda i: i.password == i.password2)]

)

f = register_form.inputs
print f

class register:
    def GET(self):
        # do $:f.render() in the template
        f = register_form()
        return render.register(f)

    def POST(self):
        f = register_form()
        if not f.validates():
            return render.register(f)
        else:
            username = f.username.render()
            #email = f.E-Mail.render()
            pwd = f.password.render()
            print pwd
            print username
            return  # do whatever is required for registration


if __name__ == "__main__":
    urls = ('/parseIpa','register') 
    app = web.application(urls, globals()) 
    app.run()

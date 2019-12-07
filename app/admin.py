from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, current_user
from app import app, models, db, login
from app.models import User, Post, Comment
from flask import render_template, flash, redirect, url_for

class SecureView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('index'))

admin.add_view(SecureView(User, db.session))
admin.add_view(SecurelView(Post, db.session))
admin.add_view(SecureView(Comment, db.session))


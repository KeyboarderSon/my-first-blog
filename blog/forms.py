from django import forms
from .models import Post

# forms.ModelForm : 장고에게 이 폼이 modelform임을 알려줌
class PostForm(forms.ModelForm):
    #폼 만들기 위해서 어떤 model이 쓰이는지 장고에게 알려줌
    class Meta:
        model = Post
        fields = ('title', 'text',)
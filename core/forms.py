from django import forms
from .models import Comment,Post,Category

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
        # fields = ('content')



class CreatePost(forms.ModelForm):
    # cat_id = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)

    class Meta:
        model = Post
        fields = ("title", "content","tags")#cat_id

    # def save(self, commit=True):
    #     post = super(CreatePost, self).save(commit=False)

    #     post.category_id = self.cleaned_data['cat_id']
    #     print("post.category_id------------>",post.category_id)
    #     if commit:
    #         post.save()

    #     return post

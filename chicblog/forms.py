from django import forms

from .models import Comment


class CommentCreateForm(forms.ModelForm):
    def is_valid(self):
        comment = self.instance
        
        if comment.author is None or comment.post is None: #ToDo: Change THIS!
            return False
        return super().is_valid()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': ''
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 2})
        }

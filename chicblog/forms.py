from django import forms

from .models import Comment


class CommentCreateForm(forms.ModelForm):
    def is_valid(self):
        comment = self.instance
        
        if comment.author is None or comment.post is None:
            return False
        return super().is_valid()

    class Meta:
        model = Comment
        fields = ['content']
from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'content', 'is_completed']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '할 일 제목을 입력하세요'}),
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': '세부 내용 (선택)'}),
        }
        error_messages = {
            'title': {
                'required': '제목은 필수 입력 항목입니다.',
                'max_length': '제목은 200자 이하로 입력하세요.',
            },
        }

    def clean_title(self):
        title = (self.cleaned_data.get('title') or '').strip()
        if not title:
            raise forms.ValidationError('제목은 공백만으로 입력할 수 없습니다.')
        if len(title) < 2:
            raise forms.ValidationError('제목은 2자 이상 입력하세요.')
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if content and len(content) > 1000:
            raise forms.ValidationError('세부 내용은 1000자 이하로 입력하세요.')
        return content

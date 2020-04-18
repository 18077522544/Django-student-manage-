from typing import Any

from  django import forms
from  .models import Student


class StudentForm(forms.ModelForm):
    # def __new__(cls) -> Any:
    #     return super().__new__(cls)

    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字！')

    class Meta:
        model = Student
        fields = {
            'name', 'sex', 'profession',
            'email', 'qq', 'phone'
        }
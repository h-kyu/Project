from django import forms
from .models import Landmark



class LandmarkForm(forms.ModelForm): # ModelForm 은 장고 모델 폼
    class Meta: # 장고 모델 폼은 반드시 내부에 Meta 클래스 가져야 함
        model = Landmark
        fields = ['imgfile']
        labels = {
            'imgfile': ''}

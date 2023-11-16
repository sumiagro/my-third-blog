from django import forms
from .models import GOAL22,CPA22,RHDT
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class GOAL22Q1Form(forms.ModelForm):

    class Meta():
        model = GOAL22
        fields = ('GOAL22A1','GOAL22AP','GOAL22B1','GOAL22BP','GOAL22C1','GOAL22CP','GOAL22D1','GOAL22DP','GOAL22E1','GOAL22EP','GOAL22F1','GOAL22FP','GOAL22G1','GOAL22GP')
        labels = {'GOAL22A1':"meta1",'GOAL22B1':"meta2",'GOAL22C1':"meta3",'GOAL22D1':"meta4",'GOAL22E1':"meta5",'GOAL22F1':"meta6",'GOAL22G1':"meta7",'GOAL22AP':"peso% de meta1",'GOAL22BP':"peso% de meta2",'GOAL22CP':"peso% de meta3",'GOAL22DP':"peso% de meta4",'GOAL22EP':"peso% de meta5",'GOAL22FP':"peso de meta6",'GOAL22GP':"peso% de meta7"}
        widgets = {
            'GOAL22A1':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22B1':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22C1':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22D1':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22E1':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22F1':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22G1':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22AP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'GOAL22BP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'GOAL22CP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'GOAL22DP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'GOAL22EP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'GOAL22FP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'GOAL22GP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            }

class GOAL22Q2Form(forms.ModelForm):

    class Meta():
        model = GOAL22
        fields = ('GOAL22A2','GOAL22B2','GOAL22C2','GOAL22D2','GOAL22E2','GOAL22F2','GOAL22G2')
        labels = {'GOAL22A2':"meta1",'GOAL22B2':"meta2",'GOAL22C2':"meta3",'GOAL22D2':"meta4",'GOAL22E2':"meta5",'GOAL22F2':"meta6",'GOAL22G2':"meta7"}
        widgets = {
            'GOAL22A2':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22B2':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22C2':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22D2':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22E2':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22F2':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22G2':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            }

class GOAL22Q3Form(forms.ModelForm):

    class Meta():
        model = GOAL22
        fields = (
            'GOAL22A3','GOAL22B3','GOAL22C3','GOAL22D3','GOAL22E3','GOAL22F3','GOAL22G3',
        )
#        labels = {'GOAL22A3':"meta1",'GOAL22B3':"meta2",'GOAL22C3':"meta3",'GOAL22D3':"meta4",'GOAL22E3':"meta5",'GOAL22F3':"meta6",'GOAL22G3':"meta7"}
        widgets = {
            'GOAL22A3':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22B3':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22C3':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22D3':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22E3':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22F3':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22G3':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            }


class GOAL22Q3AForm(forms.ModelForm):

    class Meta():
        model = GOAL22
        fields = (
            'GOAL22AR','GOAL22BR','GOAL22CR','GOAL22DR','GOAL22ER','GOAL22FR','GOAL22GR',
            'GOAL22AJ','GOAL22BJ','GOAL22CJ','GOAL22DJ','GOAL22EJ','GOAL22FJ','GOAL22GJ',
        )
        widgets = {
            'GOAL22AR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'GOAL22BR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'GOAL22CR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'GOAL22DR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'GOAL22ER':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'GOAL22FR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'GOAL22GR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'GOAL22AJ':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22BJ':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22CJ':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22DJ':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22EJ':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22FJ':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            'GOAL22GJ':forms.Textarea(attrs={'rows':2, 'cols':33, 'style': 'border-color:white'}),
            }


class CPA22CForm(forms.ModelForm):

    class Meta():
        model = CPA22
        fields = (
            'CPA22A1C','CPA22A2C','CPA22A3C','CPA22B1C','CPA22B2C','CPA22B3C','CPA22C1C','CPA22C2C','CPA22C3C','CPA22D1C','CPA22D2C','CPA22D3C','CPA22E1C','CPA22E2C','CPA22E3C',
            'CPA22A1K','CPA22A2K','CPA22A3K','CPA22B1K','CPA22B2K','CPA22B3K','CPA22C1K','CPA22C2K','CPA22C3K','CPA22D1K','CPA22D2K','CPA22D3K','CPA22E1K','CPA22E2K','CPA22E3K',
            'CPA22A1P','CPA22A2P','CPA22A3P','CPA22B1P','CPA22B2P','CPA22B3P','CPA22C1P','CPA22C2P','CPA22C3P','CPA22D1P','CPA22D2P','CPA22D3P','CPA22E1P','CPA22E2P','CPA22E3P',
            )
        widgets = {
            'CPA22A1C':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22A2C':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22A3C':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22B1C':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22B2C':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22B3C':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22C1C':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22C2C':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22C3C':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22D1C':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22D2C':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22D3C':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22E1C':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22E2C':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22E3C':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
#            'CPA22A1C':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
#            'CPA22A2C':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
#            'CPA22A3C':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
#            'CPA22B1C':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
#            'CPA22B2C':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
#            'CPA22B3C':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
#            'CPA22C1C':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
#            'CPA22C2C':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
#            'CPA22C3C':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
#            'CPA22D1C':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
#            'CPA22D2C':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
#            'CPA22D3C':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
#            'CPA22E1C':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
#            'CPA22E2C':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
#            'CPA22E3C':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'CPA22A1K':forms.Textarea(attrs={'rows':2, 'cols':50, 'style': 'border-color:white'}),
            'CPA22A2K':forms.Textarea(attrs={'rows':2, 'cols':50, 'style': 'border-color:white'}),
            'CPA22A3K':forms.Textarea(attrs={'rows':2, 'cols':50, 'style': 'border-color:white'}),
            'CPA22B1K':forms.Textarea(attrs={'rows':2, 'cols':50, 'style': 'border-color:white'}),
            'CPA22B2K':forms.Textarea(attrs={'rows':2, 'cols':50, 'style': 'border-color:white'}),
            'CPA22B3K':forms.Textarea(attrs={'rows':2, 'cols':50, 'style': 'border-color:white'}),
            'CPA22C1K':forms.Textarea(attrs={'rows':2, 'cols':50, 'style': 'border-color:white'}),
            'CPA22C2K':forms.Textarea(attrs={'rows':2, 'cols':50, 'style': 'border-color:white'}),
            'CPA22C3K':forms.Textarea(attrs={'rows':2, 'cols':50, 'style': 'border-color:white'}),
            'CPA22D1K':forms.Textarea(attrs={'rows':2, 'cols':50, 'style': 'border-color:white'}),
            'CPA22D2K':forms.Textarea(attrs={'rows':2, 'cols':50, 'style': 'border-color:white'}),
            'CPA22D3K':forms.Textarea(attrs={'rows':2, 'cols':50, 'style': 'border-color:white'}),
            'CPA22E1K':forms.Textarea(attrs={'rows':2, 'cols':50, 'style': 'border-color:white'}),
            'CPA22E2K':forms.Textarea(attrs={'rows':2, 'cols':50, 'style': 'border-color:white'}),
            'CPA22E3K':forms.Textarea(attrs={'rows':2, 'cols':50, 'style': 'border-color:white'}),
            'CPA22A1P':forms.Textarea(attrs={'rows':2, 'cols':50, 'style': 'border-color:white'}),
            'CPA22A2P':forms.Textarea(attrs={'rows':2, 'cols':50, 'style': 'border-color:white'}),
            'CPA22A3P':forms.Textarea(attrs={'rows':2, 'cols':50, 'style': 'border-color:white'}),
            'CPA22B1P':forms.Textarea(attrs={'rows':2, 'cols':50, 'style': 'border-color:white'}),
            'CPA22B2P':forms.Textarea(attrs={'rows':2, 'cols':50, 'style': 'border-color:white'}),
            'CPA22B3P':forms.Textarea(attrs={'rows':2, 'cols':45, 'style': 'border-color:white'}),
            'CPA22C1P':forms.Textarea(attrs={'rows':2, 'cols':45, 'style': 'border-color:white'}),
            'CPA22C2P':forms.Textarea(attrs={'rows':2, 'cols':45, 'style': 'border-color:white'}),
            'CPA22C3P':forms.Textarea(attrs={'rows':2, 'cols':45, 'style': 'border-color:white'}),
            'CPA22D1P':forms.Textarea(attrs={'rows':2, 'cols':45, 'style': 'border-color:white'}),
            'CPA22D2P':forms.Textarea(attrs={'rows':2, 'cols':45, 'style': 'border-color:white'}),
            'CPA22D3P':forms.Textarea(attrs={'rows':2, 'cols':45, 'style': 'border-color:white'}),
            'CPA22E1P':forms.Textarea(attrs={'rows':2, 'cols':45, 'style': 'border-color:white'}),
            'CPA22E2P':forms.Textarea(attrs={'rows':2, 'cols':45, 'style': 'border-color:white'}),
            'CPA22E3P':forms.Textarea(attrs={'rows':2, 'cols':45, 'style': 'border-color:white'}),
            }

class TIMEForm(forms.ModelForm):
    class Meta():
        model = RHDT
        fields = ('TIME',)
        widgets = {'TIME':forms.Select(attrs={'style': 'width:15ch; border-color:white; background-color:white'}),}

class CPA22AForm(forms.ModelForm):

    class Meta():
        model = CPA22
        fields = (
            'CPA22A1A','CPA22A2A','CPA22A3A','CPA22B1A','CPA22B2A','CPA22B3A','CPA22C1A','CPA22C2A','CPA22C3A','CPA22D1A','CPA22D2A','CPA22D3A','CPA22E1A','CPA22E2A','CPA22E3A',
            )
        widgets = {
            'CPA22A1A':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22A2A':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22A3A':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22B1A':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22B2A':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22B3A':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22C1A':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22C2A':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22C3A':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22D1A':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22D2A':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22D3A':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22E1A':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22E2A':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            'CPA22E3A':forms.Select(attrs={'style': 'width:8ch; border-color:white; background-color:white'}),
            }


from django import forms

class PrimerInputForm(forms.Form):
    target_sequence = forms.CharField(widget=forms.Textarea, label="Target Sequence")
    primer_length = forms.IntegerField(label="Primer Length", initial=20)
    tm = forms.FloatField(label="Melting Temperature (Tm)", initial=60.0)
    gc_content = forms.FloatField(label="GC Content", initial=50.0)
    product_size = forms.IntegerField(label="Product Size", initial=200)

from django import forms


class QueryForm(forms.Form):
    clade = forms.ChoiceField(
            label='Clade',
            choices = [('1', 'Clade 1'), ('2', 'Clade 2')],
            widget = forms.RadioSelect, required = False)
    
    subclade = forms.ChoiceField(
            label='Subclade',
            choices = [('a', 'A'), ('b', 'B')],
            widget = forms.RadioSelect, required = False)
    
    gisaid_accession = forms.CharField(max_length=200, required=False)

    type = forms.ChoiceField(
        label = "Choose a type",
        choices=[('cssr', 'CSSR'),
                 ('issr', 'ISSR'),
                 ('ssr', 'SSR'),
                 ('vntr', 'VNTR')],
         widget=forms.Select, required=True
    )


    
    
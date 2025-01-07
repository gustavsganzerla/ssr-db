from django import forms


class QueryForm(forms.Form):
    clade = forms.ChoiceField(
            label='Clade',
            choices = [('1', 'Clade 1'), ('2', 'Clade 2')],
            widget = forms.RadioSelect(attrs={'id':'id_for_clade'}), 
            required = False
            )
    
    subclade = forms.ChoiceField(
            label='Subclade',
            choices = [('a', 'a'), ('b', 'b')],
            widget = forms.RadioSelect(attrs={'id':'id_for_subclade'}), 
            required = False
            )
    
    gisaid_accession = forms.CharField(
        widget=forms.TextInput(attrs={'id':'id_for_gisaid_accession'}),
        max_length=200, 
        required=False
        )

    type = forms.ChoiceField(
        label = "Choose a type",
        choices=[('', 'Select an option'),
                 ('cssr', 'CSSR'),
                 ('issr', 'ISSR'),
                 ('ssr', 'SSR'),
                 ('vntr', 'VNTR')],
         widget=forms.Select(attrs={'id':'id_for_type'}), 
         required=True
        )
    
    length = forms.ChoiceField(
        label = "Choose a length",
        choices=[('', 'Select an option'),
                 (1, 'Mono'),
                 (2, 'Di'),
                 (3, 'Tri'),
                 (4, 'Tetra'),
                 (5, 'Penta'),
                 (6, 'Hexa'),
                 ('h6', '>6')],
         widget=forms.Select(attrs={'id':'id_for_length'}), 
         required=True
        )


    
    
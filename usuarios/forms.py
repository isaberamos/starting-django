from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Franco De Mel"
            }
    ))
    senha=forms.CharField(
        label = "Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    
class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Username",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Franco De Mel"
            }
        )
    )
    email=forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joao.silva@gmail.com"
            }
        )
     )
    senha_1=forms.CharField(
        label = "Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    senha_2=forms.CharField(
        label = "Confirmação de senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        ),
    )
     
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        print(f"Validando o campo nome_cadastro: {nome}")


        if nome:
            #nome = nome.strip()
            if nome != nome.strip():
                raise forms.ValidationError("Espaços não são permitidos nesse campo")
            
            return nome
         
         
    def clean_senha_2(self):
         senha_1 = self.cleaned_data.get("senha_1")
         senha_2 = self.cleaned_data.get("senha_2")
         
         if senha_1 and senha_2:
             if senha_1 != senha_2:
                 raise forms.ValidationError("Senhas não são iguais!")
             else:
                 return senha_2
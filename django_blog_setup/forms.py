from django import forms


class BlogSettingForm(forms.Form):
    title = forms.CharField(
        label="title",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Title"}),
    )
    description = forms.CharField(
        label="description",
        max_length=100,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Description",
                "rows": "5",
                "style": "height: 140px;",
            }
        ),
    )
    name = forms.CharField(
        label="name",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"}),
    )
    email = forms.EmailField(
        label="email",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}),
    )
    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
    )
    default_language = forms.CharField(
        label="default language",
        max_length=2,
        help_text="like 'en' or 'de'",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Default language"}
        ),
    )

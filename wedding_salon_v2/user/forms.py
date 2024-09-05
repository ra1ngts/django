from allauth.account.forms import SignupForm, LoginForm, ChangePasswordForm, ResetPasswordForm, ResetPasswordKeyForm


class UserSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        help_texts = {
            'email': 'Введите действующий адрес электронной почты.',
            'username': 'Имя пользователя может содержать буквы, цифры и @/./+/-/_ символы.',
            'password1': 'Пароль не должен быть короче 8 символов и состоять из одних цифр.',
            'password2': 'Повторите пароль для подтверждения.',
        }

        for name, field in self.fields.items():
            for_email = 'Адрес электронной почты'
            for_username = 'Имя пользователя'
            for_password1 = 'Пароль'
            for_password2 = 'Пароль (еще раз)'
            if name == 'email':
                field.widget.attrs.update({'placeholder': for_email})
            if name == 'username':
                field.widget.attrs.update({'placeholder': for_username})
            if name == 'password1':
                field.widget.attrs.update({'placeholder': for_password1})
            if name == 'password2':
                field.widget.attrs.update({'placeholder': for_password2})

            if name in help_texts:
                field.help_text = help_texts[name]

            field.widget.attrs.update({'class': 'form-control'})


class UserLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            for_login = 'Адрес электронной почты'
            for_password = 'Пароль'
            if name == 'login':
                field.widget.attrs.update({'placeholder': for_login})
            if name == 'password':
                field.widget.attrs.update({'placeholder': for_password})
            if name == 'remember':
                field.widget.attrs.update({'class': 'custom-checkbox'})
            else:
                field.widget.attrs.update({'class': 'form-control'})


class PasswordChangeForm(ChangePasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        help_texts = {
            'oldpassword': 'Введите действующий пароль.',
            'password1': 'Пароль не должен быть короче 8 символов и состоять из одних цифр.',
            'password2': 'Повторите пароль для подтверждения.',
        }

        for name, field in self.fields.items():
            for_oldpassword = 'Текущий пароль'
            for_password1 = 'Новый пароль'
            for_password2 = 'Новый пароль (ещё раз)'
            if name == 'oldpassword':
                field.widget.attrs.update({'placeholder': for_oldpassword})
            if name == 'password1':
                field.widget.attrs.update({'placeholder': for_password1})
            if name == 'password2':
                field.widget.attrs.update({'placeholder': for_password2})

            if name in help_texts:
                field.help_text = help_texts[name]

            field.widget.attrs.update({'class': 'form-control'})


class PasswordResetForm(ResetPasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            for_email = 'Адрес электронной почты'
            if name == 'email':
                field.widget.attrs.update({'placeholder': for_email})
            field.widget.attrs.update({'class': 'form-control'})


class PasswordResetKeyForm(ResetPasswordKeyForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            for_password1 = 'Новый пароль'
            for_password2 = 'Новый пароль (ещё раз)'
            if name == 'password1':
                field.widget.attrs.update({'placeholder': for_password1})
            if name == 'password2':
                field.widget.attrs.update({'placeholder': for_password2})
            field.widget.attrs.update({'class': 'form-control'})

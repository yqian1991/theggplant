from wtforms import Form, HiddenField, TextField, PasswordField, validators


class SignupForm(Form):
    email = TextField(validators=[validators.Required(), validators.Email()])
    password = PasswordField(validators=[
        validators.Required(),
        validators.Length(min=6),
        validators.EqualTo('confirm')
    ])
    confirm = PasswordField()

    def __init__(self, data, _):
        super(SignupForm, self).__init__(data)
        self._fields['email'].label.text = _('Email')
        self._fields['email'].validators[0].message = _("Email is required.")
        self._fields['email'].validators[1].message = _("Email is not in a wrong format.")
        self._fields['password'].label.text = _('Password')
        self._fields['password'].validators[0].message = _("Password is required.")
        self._fields['password'].validators[1].message = _("The length of password needs to be at least 6.")
        self._fields['password'].validators[2].message = _("Passwords must match.")
        self._fields['confirm'].label.text = _('Confirm Password')

class LoginForm(Form):
    email = TextField(validators=[validators.Required(), validators.Email()])
    password = PasswordField(validators=[validators.Required()])
    def __init__(self, data, _):
        super(LoginForm, self).__init__(data)
        self._fields['email'].label.text = _('Email Address')
        self._fields['email'].validators[0].message = _("Email is required.")
        self._fields['email'].validators[1].message = _("Email is not in a wrong format.")
        self._fields['password'].label.text = _('Password')
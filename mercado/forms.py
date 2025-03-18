from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from mercado.models import User

class CadastroForm(FlaskForm):
    def validate_username(self, check_user):
        user = User.query.filter_by(usuario=check_user.data).first()
        if user:
            raise ValidationError("Usuário ja existe ! Cadastre outro nome de usuário")
        
    def validate_email(self, check_email):
        email = User.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError("Email já existe ! Cadastre outro email.")
        
    def validate_senha(self, check_senha):
        senha = User.query.filter_by(senha=check_senha.data).first()
        if senha:
            raise ValidationError("Senha já existe ! Cadastre outra senha")
        
    usuario = StringField(label='Username', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    senha1 = PasswordField(label='Senha:', validators=[Length(min=6), DataRequired()])
    senha2 = PasswordField(label='Confirmação de senha', validators=[EqualTo('senha1'), DataRequired()])
    submit = SubmitField(label='Cadastrar')

class LoginForm(FlaskForm):
    usuario = StringField(label="Usuário:", validators=[DataRequired()])
    senha = PasswordField(label="Senha:", validators=[DataRequired()])
    submit = SubmitField(label="Login")

class CompraProdutoForm(FlaskForm):
    submit = SubmitField(label="Comprar Produto")

class VendaProdutoForm(FlaskForm):
    submit = SubmitField(label="Vender produto!")
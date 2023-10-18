from django.db import models
from stands.models import Stand
from users.models import User 
# Create your models here.

class Reserva(models.Model):
    cnpj = models.CharField(max_length=11)
    nome_empresa = models.CharField(max_length=150)
    categoria_empresa = models.CharField(max_length=150)
    quitado = models.BooleanField(default=False)
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)  # Ou substitua 'None' pelo usuário padrão desejado

    def __str__(self):
        return self.nome_empresa

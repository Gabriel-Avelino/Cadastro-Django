from django.db import migrations, models

def remove_duplicates(apps, schema_editor):
    Usuario = apps.get_model('app_cadastro_usuarios', 'Usuario')
    duplicates = Usuario.objects.values('nome').annotate(count=models.Count('id')).filter(count__gt=1)

    for duplicate in duplicates:
        usuario = Usuario.objects.filter(nome=duplicate['nome']).order_by('id_usuario')[1:]
        usuario.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_usuarios', '0002_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.TextField(max_length=255, unique=True),
        ),
    ]
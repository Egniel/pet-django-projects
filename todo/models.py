from django.db import models


class Todo(models.Model):
    """Model definition for Todo."""
    text = models.CharField(verbose_name='text', max_length=128)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        verbose_name='created at', auto_now=True)

    class Meta:
        """Meta definition for Todo."""

        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        """Unicode representation of Todo."""
        return self.text

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

UserModel = get_user_model()


@receiver(signal=post_save, sender=UserModel)
def send_email_on_successful_sign_up(instance, created, **kwargs):
    if not created:
        return

    email_content = render_to_string('email_templates/successful_sign_up.html', {
            'user': instance,
        })
    send_mail(
        subject='Welcome to Petstagram!',
        message='You just signed up!',
        from_email=email_content,
        recipient_list=(instance.email,),
    )
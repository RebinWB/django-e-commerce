from e_shop.celery import app
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


@app.task
def send_email_for_add_to_cart(user_name, user_email, product_name):
	
	context = {
		'user_name': user_name,
		'product': product_name,
	}

	email_subject = f'You Added {product_name} to Your Cart!'
	email_body = render_to_string('email_body.txt', context)

	email = EmailMessage(
		subject=email_subject,
		body=email_body,
		from_email=settings.DEFAULT_FROM_EMAIL,
		to=[user_email, ],
		)

	return email.send(fail_silently=False)



from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from EXPIRYFY.models import Product
from django.core.mail import send_mail
from datetime import timedelta

def check_expiry_job():
    today = timezone.now().date()
    alert_date = today + timedelta(days=3)
    products = Product.objects.filter(expiry_date=alert_date)

    for product in products:
        subject = f"Expiry Alert: {product.product_name}"
        message = (
            f"Dear Shopkeeper,\n\n"
            f"The product '{product.product_name}' "
            f"(Batch: {product.batch_no}, Rack: {product.rack_no}) "
            f"is going to expire on {product.expiry_date}.\n\n"
            f"Please take necessary action.\n\n"
            f"- Your Inventory System"
        )
        send_mail(subject, message, None, ["atchayathiyagu21@gmail.com"], fail_silently=False)

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_expiry_job, 'cron', hour=10, minute=30)  # every day 9 AM
    scheduler.start()

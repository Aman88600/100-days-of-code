from plyer import notification

def tell_user(price):
    notification.notify(
    title="Price Drop",
    message=f"Price = {price}",
    timeout=3  # seconds
    )

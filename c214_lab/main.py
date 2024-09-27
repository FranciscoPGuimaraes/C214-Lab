class MessageSender:
    def send(self, message: str):
        raise NotImplementedError("Este método deve ser implementado por subclasses.")

class EmailSender(MessageSender):
    def send(self, message: str):
        print(f"Enviando e-mail com a mensagem: {message}")

class SmsSender(MessageSender):
    def send(self, message: str):
        print(f"Enviando SMS com a mensagem: {message}")

class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def notify(self, message: str):
        self.sender.send(message)

class NotificationController:
    def __init__(self, service: NotificationService):
        self.service = service

    def send_notification(self, message: str):
        print("Controlador recebendo a solicitação para enviar notificação...")
        self.service.notify(message)
        print("Notificação enviada pelo controlador.")

if __name__ == "__main__":
    email_sender = EmailSender()
    notification_service_email = NotificationService(email_sender)
    notification_controller_email = NotificationController(notification_service_email)
    notification_controller_email.send_notification("Você tem um novo e-mail!")

    sms_sender = SmsSender()
    notification_service_sms = NotificationService(sms_sender)
    notification_controller_sms = NotificationController(notification_service_sms)
    notification_controller_sms.send_notification("Você tem um novo SMS!")

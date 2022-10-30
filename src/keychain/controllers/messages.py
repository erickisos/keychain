from ..models.components import Components
from ..models.messages import Message
from ..ports.http_outputs import send_message


def send(message: Message, components: Components) -> Message:
    # TODO: Si queremos guardar el mensaje en base, este es el lugar
    # En esta función se hace todo el procesamiento que queremos para el
    # controller de send_message, actualmente, solo usamos el output
    # para enviar el mensaje.
    return send_message(message, components)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Message

@api_view(['GET'])
def get_messages(request):
    messages = Message.objects.all()
    data = [{"id": msg.id, "content": msg.content} for msg in messages]
    return Response(data)

@api_view(['POST'])
def add_message(request):
    content = request.data.get('content')
    message = Message(content=content)
    message.save()
    return Response({"id": message.id, "content": message.content})

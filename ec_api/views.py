from rest_framework import viewsets
from .serializers import NoteSerializer
from .models import Note


class TaskView(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

# @api_view(['GET'])
# def getRoute(request):

#     routes = [
#         {
#             'Endpoint': '/notes/',
#             'method': 'GET',
#             'body': None,
#             'completed': False,
#             'description': 'Returns an array of notes'
#         },
#         {
#             'Endpoint': '/notes/id',
#             'method': 'GET',
#             'body': None,
#             'completed': False,
#             'description': 'Returns a single note object'
#         },
#         {
#             'Endpoint': '/note/create/',
#             'method': 'POST',
#             'body': {'body': ''},
#             'completed': False,
#             'description': 'Creates a new note with data sent in post request'
#         },
#         {
#             'Endpoint': '/note/id/update/',
#             'method': 'PUT',
#             'body': {'body': ''},
#             'completed': False,
#             'description': 'Creates an existing note with data sent in put request'
#         },
#         {
#             'Endpoint': '/note/id/delete/',
#             'method': 'DELETE',
#             'body': None,
#             'completed': False,
#             'description': 'Delete an existing note'
#         },
#     ]

#     return Response(routes)


# @api_view(['GET'])
# def getNotes(request):
#     notes = Note.objects.all()
#     serializer = NoteSerializer(notes, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def getNote(request, pk):
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)


# @api_view(['POST'])
# def createNote(request):
#     data = request.data
#     note = Note.objects.create(
#         body=data['body']
#     )
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)


# @api_view(['PUT'])
# def updateNote(request, pk):
#     data = request.data
#     note = Note.objects.get(id=pk)
#     note.completed = data['completed']
#     note.body = data['body']
#     note.save()
#     serializer = NoteSerializer(note, data=data)
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['DELETE'])
# def deleteNote(request, pk):
#     note = Note.objects.get(id=pk)
#     note.delete()
#     return Response('Note was deleted!')

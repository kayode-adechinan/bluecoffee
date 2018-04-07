from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from core.serializers import PostSerializer, ReporterSerializer, ApiResponseSerializer, FileHandlerSerializer
from core.models import Post, Reporter, FileHandler
from django.views.generic.edit import CreateView

from django.forms.models import model_to_dict


class FileHandlerView(generics.ListCreateAPIView):
    serializer_class = FileHandlerSerializer
    queryset = FileHandler.objects.all()



class ReporterView(generics.ListCreateAPIView):
    serializer_class = ReporterSerializer
    queryset = Reporter.objects.all()

class ReporterViewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReporterSerializer
    queryset = Reporter.objects.all()

class ReporterAuthenticationView(views.APIView):

    #def get_object(self, email):
        #try:
            #return User.objects.get(email=email)
        #except User.DoesNotExist:
            #raise Http404

    def post(self, request):
        serializer =  ReporterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                reporter = Reporter.objects.get(Q(email__iexact=serializer.data['email']),Q(password__iexact=serializer.data['password']))
                rs= ReporterSerializer(reporter)
                return Response(rs.data)
            except Reporter.DoesNotExist:
                return Response({'klll':'error'})

class ReporterPasswordReset(views.APIView):
    """
    Set user password.
    """
    def get_object(self, email):
        try:
            return Reporter.objects.get(email=email)
        except Reporter.DoesNotExist:
            raise Http404

    def get(self, request, email, format=None):
        reporter = self.get_object(email)
        #password = generate_user_password()
        #user.set_password(password)
        #user.save()
        #serializer = UserSerializer(user)
        #send_password_reset_mail(user.email, password)
        #return Response(serializer.data)

class PostView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('-created')

class PostViewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostSearchView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):

        if 'u' in self.request.query_params:

            user_id = self.request.query_params.get('u', None)
            query = self.request.query_params.get('q', None)

            posts = Post.objects.filter(
                Q(reporter__pk=user_id),
                Q(body__icontains=query) | Q(title__icontains=query) )

            return posts


        query = self.request.query_params.get('q', None)

        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query) |
            Q(reporter__name__icontains=query) | Q(reporter__email__icontains=query)
        )
        return posts

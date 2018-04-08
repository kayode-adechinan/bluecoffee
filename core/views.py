from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from core.serializers import PostSerializer, ReporterSerializer
from core.models import Post, Reporter
from django.views.generic.edit import CreateView
from core.helpers import generate_user_password, send_password_reset_mail
from django.http import Http404



class ReporterView(generics.ListCreateAPIView):
    serializer_class = ReporterSerializer
    queryset = Reporter.objects.all()

class ReporterViewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReporterSerializer
    queryset = Reporter.objects.all()

class ReporterAuthenticationView(views.APIView):

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
        password = generate_user_password()
        reporter.password = password
        reporter.save()
        serializer = ReporterSerializer(reporter)
        send_password_reset_mail(reporter.email, password)
        return Response(serializer.data)

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

            reporter_id = self.request.query_params.get('u', None)
            query = self.request.query_params.get('q', '')

            posts = Post.objects.filter(
                Q(reporter__pk=reporter_id),
                Q(body__icontains=query) | Q(title__icontains=query) )

            return posts


        query = self.request.query_params.get('q', '')

        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query) |
            Q(reporter__name__icontains=query) | Q(reporter__email__icontains=query)
        )
        return posts

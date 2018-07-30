from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogSerialize
from .models import Blog
from rest_framework import status

class BlogList(APIView):

    def get(self, request):
        blogs = Blog.objects.all()
        blogserial = BlogSerialize(blogs, many=True)
        return Response(blogserial.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialize = BlogSerialize(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return  Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetail(APIView):

    def get_blog(self,pk):
        try:
            blog = Blog.objects.get(pk=pk)
            return  blog
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, pk):
       OneBlog = Blog.objects.get(pk=pk)
       resp = BlogSerialize(OneBlog)
       return Response(resp.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        UpdateBlog = Blog.objects.get(pk=pk)
        serialized = BlogSerialize(UpdateBlog, data=request.data)
        if serialized.is_valid():
            return Response(serialized.data, status=status.HTTP_200_OK)
        return Response(serialized.errors, status=status.HTTP_304_NOT_MODIFIED)

    def delete(self, request, pk):
        BlogToDelete = Blog.objects.get(pk=pk)
        BlogToDelete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from .models import Post
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import  BlogPostForm
from rest_framework.permissions import IsAuthenticated



class PostDetailAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'post.html'
    permission_classes = [IsAuthenticated]

    
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = BlogPostForm(instance=post)  # Pass instance to form
        return Response({'form': form, 'post': post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = BlogPostForm(request.POST, instance=post)  # Pass instance to form
        if form.is_valid():
            form.save()
            return redirect('home')
        return Response({'form': form, 'post': post})
    
    
class PostDeleteAPI(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('home')



        

    

    
    

        

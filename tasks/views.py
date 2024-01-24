from django.db.models import F
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import generics, status, viewsets, permissions
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task
from .forms import TaskForm


# Create your views here.
class TaskListAPI(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['priorities'] = ['High', 'Medium', 'Low']
        return context

    def get_queryset(self):
        queryset = Task.objects.all().order_by(F('priority').asc())
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(title__icontains=query))

        creation_date = self.request.GET.get('creation_date')
        if creation_date:
            queryset = queryset.filter(creation_date__date=creation_date)

        due_date = self.request.GET.get('due_date')
        if due_date:
            queryset = queryset.filter(due_date__date=due_date)

        priority = self.request.GET.get('priority')
        if priority:
            queryset = queryset.filter(priority=priority)

        complete = self.request.GET.get('complete')
        if complete == '1':
            queryset = queryset.filter(complete=True)

        elif complete == '0':
            queryset = queryset.filter(complete=False)

        return queryset


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_details.html'
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(UpdateView):
    model = Task
    template_name = 'task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')


class TaskDelete(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')

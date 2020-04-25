from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView
from .forms import TodoListForm
from .models import TodoList, BoardList


# This class List View lists all the boards under /boards url
class BoardsListView(ListView):
    model = BoardList
    template_name = 'boards.html'
    context_object_name = 'board_list'
    # paginate_by = 5
    ordering = ['-id']

    def get_queryset(self):
        queryset = super(BoardsListView, self).get_queryset()
        queryset = queryset.filter(userid=self.request.user)
        return queryset


class BoardListView(LoginRequiredMixin, TemplateView):
    template_name = 'todolist.html'

    def get_context_data(self, **kwargs):
        context = super(BoardListView, self).get_context_data(**kwargs)
        board_id = int((self.request.path.strip("/")).split("/")[1])
        context['board_get_id'] = board_id
        context['board_id'] = board_id
        context['todo_list'] = TodoList.objects.filter(userid=self.request.user.id, board_id=board_id).order_by(
            '-created_date')
        context['board_list'] = BoardList.objects.filter(userid=self.request.user.id).order_by('id')
        self.request.session['current_board_id'] = board_id
        return context


class BoardCreateView(LoginRequiredMixin, CreateView):
    model = BoardList
    fields = ['board_name']
    template_name = 'addboard.html'
    extra_context = {'button_name': 'Create Board'}

    def get_form_kwargs(self):
        kwargs = super(BoardCreateView, self).get_form_kwargs()
        if kwargs['instance'] is None:
            kwargs['instance'] = BoardList()
        kwargs['instance'].userid = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('board', args=(self.object.id,))

    # def test_func(self):
    #     board = self.get_object()
    #     if self.request.user == board.userid:
    #         return True
    #     return False
    # def form_valid(self, form):
    #     form.instance.userid_id = self.request.user
    #     return super().form_valid(form)


class BoardDeleteView(LoginRequiredMixin, DeleteView):
    model = BoardList
    success_url = '/'
    template_name = 'boardlist_confirm_delete.html'

    def test_func(self):
        user = self.get_object()
        if self.request.user.id == user.userid:
            return True
        return False


class BoardUpdateView(UserPassesTestMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = BoardList
    fields = ['board_name']
    template_name = 'addboard.html'
    success_url = '/'
    success_message = "Board name Updated"
    extra_context = {'button_name': 'Update Board'}

    def test_func(self):
        board = self.get_object()
        if self.request.user == board.userid:
            return True
        return False


# function to delete single item
@login_required
def delete_items(request, list_id):
    try:
        # Deleting the item from list by logged in user
        item = TodoList.objects.get(pk=list_id, userid=request.user.id)
        item.delete()
        messages.success(request, "Item has been Deleted")
        # This return will redirect back to the same page
        return redirect(request.META.get('HTTP_REFERER', '/'))
    except:
        return redirect('boards')


# function to cross title of an item
@login_required
def strike(request, list_id):
    try:
        # Updating the completed column of item to True
        item = TodoList.objects.get(pk=list_id, userid=request.user.id)
        if item.completed:
            item.completed = False
        else:
            item.completed = True
        item.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    except:
        return redirect('boards')


@login_required
def additem(request):
    if request.method == "POST":
        request.POST = request.POST.copy()
        # Assigning logged in user id value to form userid
        request.POST['userid'] = request.user.id
        # Getting board id from url by using get_board_id function
        request.POST['board_id'] = request.session['current_board_id']
        # request.POST['board_id'] = int(get_board_id(request.path))
        form = TodoListForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return redirect('boards')
    else:
        return redirect(request.META.get('HTTP_REFERER', '/'))


# function to delete board, this will delete all items as well because of Foreign key
@login_required()
def deleteboard(request, board_id):
    try:
        # Deleting Board row from DB filtering PK and userid
        item = BoardList.objects.get(pk=board_id, userid=request.user.id)
        item.delete()
        messages.success(request, "Board has been Deleted")
        return redirect('boards')
    except:
        return redirect('boards')


# function to get board id from url
def get_board_id(mixed_url):
    return (mixed_url.strip("/")).split("/")[1]

# function to add new board
# def addboard(request):
#     if request.method == "POST":
#         if request.POST['board_name']:
#             request.POST = request.POST.copy()
#             # Assigning logged in user id value to form userid
#             request.POST['userid'] = request.user.id
#             form = BoardListForm(request.POST or None)
#             if form.is_valid():
#                 form.save()
#                 # fetching id of newly created board by user
#                 lastest_added_board_list = BoardList.objects.filter(userid_id=request.user.id).latest('id')
#                 redirect_url = 'board/' + str(lastest_added_board_list.id)
#                 messages.success(request, "New Board is added")
#                 return redirect(redirect_url)
#             else:
#                 return redirect('addboard')
#         else:
#             messages.success(request, "Enter Board name")
#             return redirect('addboard')
#
#     elif request.method == "GET":
#         return render(request, 'addboard.html')
#     else:
#         return redirect('home')


# def home(request):
#     is_user_login = False
#     if request.user.is_authenticated:
#         return redirect('boards')
#     else:
#         #user login request check
#         if request.method == "POST":
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user is not None:
#                 auth.login(request, user)
#                 return redirect('boards')
#             else:
#                 messages.error(request, "Login Failed. Enter Correct Username and Password.")
#                 return redirect('home')
#         else:
#             return render(request, 'login.html')


# class ItemDeleteView(LoginRequiredMixin, DeleteView):
#     model = TodoList
#     success_url = '/'
#     def get_success_url(self):
#         return self.request.META.get('HTTP_REFERER', '/')
#
#     def test_func(self):
#         listitem = self.get_object()
#         if self.request.user == listitem.userid:
#             messages.success(self.request, "Item has been Deleted")
#             return True
#         return False


# function to delete each item under specific Board


# Store new created board into DB
# def board(request, board_id):
#     is_user_login = False
#     if request.user.is_authenticated:
#         is_user_login = True
#         try:
#             # check id board id in url is valid of not
#             board_id_check = BoardList.objects.get(pk=board_id, userid=request.user.id)
#             # Getting board id from url by using get_board_id function
#             board_get_id = int(get_board_id(request.path))
#             # Fetching Board list to show under every board
#             board_list = BoardList.objects.filter(userid_id=request.user.id)
#             # Fetching list of item for given board id
#             todo_list = TodoList.objects.filter(userid=request.user.id, board_id=board_id)
#             # checking the same board url for POST and GET method
#             if request.method == "POST" and request.POST['form_name'] == "add_list":
#                 request.POST = request.POST.copy()
#                 # Assigning logged in user id value to form userid
#                 request.POST['userid'] = request.user.id
#                 # Getting board id from url by using get_board_id function
#                 request.POST['board_id'] = int(get_board_id(request.path))
#                 form = TodoListForm(request.POST or None)
#                 if form.is_valid():
#                     form.save()
#                     messages.success(request, "New item is added in the list")
#                     return render(request, 'todolist.html',
#                                   {'todo_list': todo_list,
#                                    'is_user_login': is_user_login,
#                                    'board_id': board_id,
#                                    'board_list': board_list,
#                                    'board_get_id': board_get_id
#                                    })
#                 else:
#                     return redirect('home')
#             # This else condition is for GET method
#             else:
#                 if todo_list is not None:
#                     return render(request, 'todolist.html',
#                                   {'todo_list': todo_list,
#                                    'is_user_login': is_user_login,
#                                    'board_id': board_id,
#                                    'board_list': board_list,
#                                    'board_get_id': board_get_id
#                                    })
#                 else:
#                     return redirect('boards')
#         except:
#             return redirect('boards')
#     else:
#         return redirect('home')


# function to list all the boards of logged in user
# def boards(request):
#     is_user_login = False
#     if request.user.is_authenticated:
#         is_user_login = True
#         # Fetching all boards created by Logged in User
#         board_list = BoardList.objects.filter(userid_id=request.user.id)
#         return render(request, 'boards.html', {'board_list': board_list, 'is_user_login': is_user_login})
#     else:
#         return redirect('home')

# # user logout functionality
# def logout(request):
#     auth.logout(request)
#     return redirect('home')
# class ListItemCreateView(LoginRequiredMixin, CreateView):
#     model = TodoList
#     template_name = 'todolist.html'
#     fields = ['item']


# function to uncross title of an item
# @login_required
# def uncross(request, list_id):
#     try:
#         # Updating the completed column of item to False
#         item = TodoList.objects.get(pk=list_id, userid=request.user.id)
#         item.completed = False
#         item.save()
#         # This return will redirect back to the same page
#         return redirect(request.META.get('HTTP_REFERER', '/'))
#     except:
#         return redirect('boards')

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def teacher_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        ''' (^ ^) '''
        '''
            Using user groups, to group according to user type.
            Good For complex role based users
        '''
        # if request.user.groups.filter(name='teacher').exists(): #

        '''
            Using 'is_teacher' field directly to check if teacher, (CustomUser usage)
        '''
        if request.user.is_teacher:
            return view_func(request, *args, **kwargs)
        else:
            # return redirect('access_denied')  # Redirect to an appropriate page
            return redirect('/')  # Redirect to an appropriate page

    return wrapper

from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'UserName',
            'id': 'id_username'
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'type': 'password',
            'placeholder': 'Password',
            'id': 'id_password',
        }))


class RoomForm(ModelForm):
    class Meta:
        model = Room
        labels = {'r_number': 'Room Number'}
        fields = ['r_number', 'seating_capacity']


class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        labels = {'uid': 'Instructor ID', 'name': 'Instructor Name'}
        fields = ['uid', 'name']


class MeetingTimeForm(ModelForm):
    class Meta:
        model = MeetingTime
        fields = ['pid', 'time', 'day']
        widgets = {
            'pid': forms.TextInput(),
            'time': forms.Select(),
            'day': forms.Select(),
        },
        labels = {
            "pid": "ID",
            
        }


class CourseForm(ModelForm):
    class Meta:
        model = Course
        labels = {'max_numb_students': 'Maximum students',  'num_class_in_week': 'Total classes in a week'}
        fields = [
            'course_number', 'course_name', 'max_numb_students', 'instructors', 'num_class_in_week'
        ]


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        labels = {'dept_name': 'Department name'}
        # fields = ['dept_name', 'courses']
        fields = ['dept_name']


class SectionForm(ModelForm):
    class Meta:
        model = Section
        labels = {"section_id": "Class ID"}
        # fields = ['section_id', 'department', 'num_class_in_week', 'courses']
        fields = ['section_id', 'department', 'courses']

"""
Teacher_preference_module starts
"""
class TeacherPreferenceForm(forms.ModelForm):
    class Meta:
        model = TeacherPreference
        fields = ["section", "course", "weekday", "timeslot", "teacher"]
        widgets = {
            "teacher": forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)
        self.fields["section"].queryset = Section.objects.all()
        if self.request and self.request.user.is_authenticated:
            self.fields["teacher"].initial = self.request.user

        if "section" in self.data:
            try:
                section_id = int(self.data.get("section"))
                self.fields["course"].queryset = Course.objects.filter(
                    section__id=section_id
                )
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields["course"].queryset = self.instance.section.courses.all()

        if "course" in self.data:
            try:
                course_id = int(self.data.get("course"))
                self.fields["timeslot"].queryset = MeetingTime.objects.all()
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields["timeslot"].queryset = MeetingTime.objects.all()

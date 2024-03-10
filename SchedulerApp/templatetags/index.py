from django import template
from django.utils.html import mark_safe
register = template.Library()

@register.filter
def dictKey(d, k):
    '''Returns the given key from a dictionary.'''

    return ', '.join(d[k]) or ''

"""
<td>
    <div style="margin-bottom: 0rem;text-align: center;">
    ITEC-HCI HCI
    </div>
        
    <div style="display: flex;justify-content: space-between;"> 
    <span>c101</span><span>Ghulam Jillani</span> 
    </div>
</td>
"""
# sub schedule section.section_id week.0 time.0
@register.simple_tag
def sub(s, d, w, t):
    '''Returns the subject-teacher for a department, weekday and time period'''
    for c in s:
        # if c.department.dept_name == d and c.meeting_time.day == w and c.meeting_time.time == t:
        if c.section == d and c.meeting_time.day == w and c.meeting_time.time == t:
            # return f'Room: {c.room} - {c.course.course_name} ({c.instructor.name})'
            return mark_safe(
                f"""
                        <div style="margin-bottom: 0rem;text-align: center;">
                            <input class='input' value='{c.course.course_name}' readonly/> 
                        </div>
                            
                        <div style="display: flex;justify-content: space-between;"> 
                            <span>
                                <input class='input' value='{c.room}' readonly/> 
                            </span>
                            <span>
                                <input class="instructor-name input"  style="text-align: right;" value='{c.instructor.name}' readonly/>
                            </span> 
                        </div>
                    """
            )

    return ''


@register.simple_tag
def sub_teacher(s, d, w, t):
    """Returns the subject-teacher for a department, weekday and time period"""
    for c in s:
        if (
            c.instructor == d
            and c.meeting_time.day == w
            and c.meeting_time.time == t
        ):
            return mark_safe(
                f"""
                        <div>
                            {c.course.course_name} 
                        </div>
                            
                        <div> 
                            <span>{c.room}</span>
                            <span>{c.instructor.name}</span> 
                        </div>
                    """
            )
    return ""


# @register.simple_tag
# def sub_teacher(s, teacher_id, w, t):
#     """Returns the subject-course for a teacher, weekday, and time period"""
#     for c in s:
#         if (
#             c.instructor.id == teacher_id
#             and c.meeting_time.day == w
#             and c.meeting_time.time == t
#         ):
#             return mark_safe(
#                 f"""
#                         <div style="margin-bottom: 0rem;text-align: center;">
#                             {c.course.course_name}
#                         </div>
#                         <div style="display: flex;justify-content: space-between;">
#                             <span>{c.room}</span>
#                             <span>{c.section.section_id} ({c.section.department})</span>
#                         </div>
#                     """
#             )
#     return ""


@register.tag
def active(parser, token):
    args = token.split_contents()
    template_tag = args[0]
    if len(args) < 2:
        raise (template.TemplateSyntaxError, f'{template_tag} tag requires at least one argument')
    return NavSelectedNode(args[1:])

class NavSelectedNode(template.Node):
    def __init__(self, patterns):
        self.patterns = patterns
    def render(self, context):
        path = context['request'].path
        for p in self.patterns:
            pValue = template.Variable(p).resolve(context)
            if path == pValue:
                return 'active'
        return ''

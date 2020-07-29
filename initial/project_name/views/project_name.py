from django.shortcuts import render
from django.views import View

class {{ camel_case_project_name }}View(View):
    template_name = '{{ project_name }}/{{ project_name }}.html'
    page_title = '{{ camel_case_project_name }}'


    def get(self, request):
        context = {
            'project_name': '{{ project_name }}',
            'page_title': self.page_title,
        }

        return render(request, self.template_name, context=context)

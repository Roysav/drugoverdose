from django.views.generic import DetailView, FormView
from . import forms
from . import models


class AskQuestion(FormView):
    template_name = 'new_question.html'
    form_class = forms.NewQuestionForm
    success_url = '/'

    def form_valid(self, form: forms.NewQuestionForm):
        form.instance.author = self.request.user
        form.instance.type = models.PostType.QUESTION

        form.save()
        return super().form_valid(form)
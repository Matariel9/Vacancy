from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.db.models import Count, Avg, Q, F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from p1.settings import TOTAL_ON_PAGE
from vac.models import Vacancy, Skill
from .serializers import VacancyListSerializor, VacancyDetailSerializor, VacancyCreateSerializer, VacancyUpdateSerializer, VacancyDestroySerializer, SkillSerializer

import json

# Create your views here.


def hello(request):
    return HttpResponse("Hello world!")
    

class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


@method_decorator(csrf_exempt, name = "dispatch")
class VacancyListView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializor

    def get(self, request, *args, **kwargs):
        vacancy_text=request.GET.get('text',None)
        if vacancy_text:
            self.queryset = self.queryset.filter(
                text__contains = vacancy_text
                #icontains used as i would use .lower()
            )
            
        # skill_name = request.GET.get("skill", None)
        # if skill_name:
        #     self.queryset = self.queryset.filter(
        #         skills__name__contains = skill_name
        #     )

        skills = request.GET.getlist("skill", None)
        skills_q = None
        for skill in skills:
            if skills_q is None:
                skills_q = Q( skills__name__contains = skill)
            else:
                skills_q |= Q( skills__name__contains = skill)
        if skills_q:
            self.queryset = self.queryset.filter(skills_q)
        return super().get(request, *args, **kwargs)


@method_decorator(csrf_exempt, name = "dispatch")
class VacancyDetailView(RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyDetailSerializor



@method_decorator(csrf_exempt, name = "dispatch")
class VacancyCreateView(CreateAPIView):
    queryset= Vacancy.objects.all()
    serializer_class = VacancyCreateSerializer



@method_decorator(csrf_exempt, name = "dispatch")
class VacancyUpdateView(UpdateAPIView):
    queryset= Vacancy.objects.all()
    serializer_class = VacancyUpdateSerializer


@method_decorator(csrf_exempt, name = "dispatch")
class VacancyDeleteView(DestroyAPIView):
    queryset= Vacancy.objects.all()
    serializer_class = VacancyDestroySerializer

class VacancyLikeView(UpdateAPIView):
    queryset= Vacancy.objects.all()
    serializer_class = VacancyDetailSerializor

    def put(self, request, *args, **kwargs):
        Vacancy.objects.filter(pk__in=request.data).update(likes=F('likes') + 1)

        return JsonResponse((
            VacancyDetailSerializor((Vacancy.objects.filter(pk__in=request.data)), many=True).data
        ), safe = False)
from rest_framework import serializers
from .models import Vacancy, Skill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model= Skill
        fields = '__all__'

# class VacancySerializor(serializers.Serializer):
#     id = serializers.IntegerField()
#     text = serializers.CharField(max_length = 2000)
#     slug = serializers.SlugField(max_length = 50)
#     status = serializers.CharField(max_length = 50)
#     created = serializers.DateField()
#     user = serializers.CharField(max_length=100

class VacancyListSerializor(serializers.ModelSerializer):
    user = serializers.CharField()
    skills = serializers.SlugRelatedField(
        many=True,
        read_only = True,
        slug_field = "name"
    )
    class Meta:
        model = Vacancy
        fields=["id","text","slug","status","created","user","skills"]

class VacancyDetailSerializor(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(
        many=True,
        read_only = True,
        slug_field = "name"
    )
    class Meta:
        model = Vacancy
        fields='__all__'

class VacancyCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required = False)
    skills = serializers.SlugRelatedField(
        required = False,
        many = True,
        queryset = Skill.objects.all(),
        slug_field = "name"
    )

    class Meta:
        model = Vacancy
        fields = '__all__'

    def is_valid(self, raise_exception = False):
        self._skills = self.initial_data.pop("skills")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        vacancy = Vacancy.objects.create(**validated_data)
        for skill in self._skills:
            skill_obj, _ = Skill.objects.get_or_create(name=skill)
            vacancy.skills.add(skill_obj)
        vacancy.save()
        return vacancy

class VacancyUpdateSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(read_only = True)
    created = serializers.DateField(read_only = True)
    skills = serializers.SlugRelatedField(
        required = False,
        many = True,
        queryset = Skill.objects.all(),
        slug_field = "name"
    )

    class Meta:
        model = Vacancy
        fields = ["id","text","status","slug","skills", "user", "created"]

    def save(self):
        vacancy = super().save()
        for skill in self.skills:
            skill_obj, _ = Skill.objects.get_or_create(name=skill)
            vacancy.add(skill_obj)
        
        vacancy.save()
        return vacancy

class VacancyDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ["id"]
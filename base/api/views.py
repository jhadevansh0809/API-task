from base.models import CustomUser,ParagraphItem
from .serializers import UserSerializer,ParagraphSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import APIView
from email_validator import validate_email,EmailNotValidError
import re

import datetime
def validateDOB(date_text):
    try:
        datetime.date.fromisoformat(date_text)
        return True
    except ValueError:
        return False

def validemailchecker(email):
    try:
        v = validate_email(email)
        email = v["email"] 
        return True
    except EmailNotValidError as e:
        return False


def strongpasswordchecker(password):
    while True:
        if (len(password)<=8):
            return False
        elif not re.search("[a-z]", password):
            return False
        elif not re.search("[A-Z]", password):
            return False
        elif not re.search("[0-9]", password):
            return False
        elif not re.search("[_@$]" , password):
            return False
        elif re.search("\s" , password):
            return False
        else:
            return True

class Register(GenericAPIView,CreateModelMixin):
    permission_classes = []
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    def post(self,request):
        data = request.data
        username=data['username']
        email=data['email']
        dob=data['dob']
        password=data['password']

        if(username.find(' ')==-1): 
            if(validemailchecker(email)): 
                if(validateDOB(dob)):
                    if(strongpasswordchecker(password)):
                        if CustomUser.objects.filter(username=username).exists():
                                return Response (
                                {
                                "message":"Username already exists!",
                                "status" : False,
                                }
                                )
                        else:
                            if CustomUser.objects.filter(email=email).exists():
                                return Response (
                                {
                                "message":"Email already exists!",
                                "status" : False,
                                }
                                )
                            else:
                                user=CustomUser.objects.create_user(username=username,email=email,dob=dob,password=password)
                                user.save()
                                return Response (
                                {
                                "message":"User created successfully!",
                                "status" : True,
                                }
                                )
                        
                    else:
                        return Response (
                            {
                            "message":" Passwords is not strong! Primary conditions for password validation: 1.Minimum 8 characters. 2.The alphabet must be between [a-z]. 3.At least one alphabet should be of Upper Case [A-Z]. 4.At least 1 number or digit between [0-9]. 5.At least 1 character from [ _ or @ or $ ].",
                            "status" : False,
                            }
                            )
                else:
                    return Response (
                            {
                            "message":"Invalid date field. Correct pattern is YYYY-MM-DD",
                            "status" : False,
                            }
                            )
                        
            else:
                  return Response (
                        {
                        "message":"Enter valid email!",
                        "status" : False,
                        }
                        )
                      
        else:
            return Response (
                {
                "message":"Username should contain one word only!",
                "status" : False,
                }
                )



class Login(APIView):
    permission_classes = []

    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            response = {"message": "Login Successfull", "tokens": user.auth_token.key}
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message": "Invalid email or password"})
        


class Paragraphs(GenericAPIView,CreateModelMixin):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        paragraph_group=request.data['paragraphs']
        paragraph_group_list=paragraph_group.split('\n\n')

        for paragraph in paragraph_group_list:
            initialparagraph=paragraph
            paragraph=paragraph.replace("\n",' ')
            paragraph = re.sub(r'[.,"\'-?:!;]', '', paragraph)
            words=paragraph.split()
            words=list(map(lambda word:word.lower(),words))
            ParagraphItem.objects.create(paragraph=initialparagraph, words=words)

        return Response( {"message":"data received","status":True})
    


class FindParagraphs(GenericAPIView,CreateModelMixin):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        word=request.data['word'].lower()

        result = ParagraphItem.objects.filter(words__contains=[word])
        serialized_data = ParagraphSerializer(result,many=True)
        temp=[]

        for object in serialized_data.data:
            temp.append({"paragraph":object["paragraph"],"target_count":object["words"].count(word)})

        newlist = sorted(temp, key=lambda d: d['target_count'],reverse=True) 

        if(len(newlist)>10):
            return Response({"Final Result":newlist[:10]})

        return Response({"Final Result":newlist})
from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from Kilimo.mkulima.serializers import *
from Kilimo.researcher.serializers import *
from Kilimo.officer.serializers import *
from Kilimo.utils.index import sendNotification
from .models import *
# from .serializers import *
# from Kiepe.kibanda.models import *
import string, random
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View
import datetime
from .serializers import *
import json

# Create your views here.
class UserDetalsAPIView(APIView):
    def post(self, request, *args, **kwargs):
        
        user_id = request.data.get('user_id')
        print('this is user id ', user_id)
        try:
            user = get_user_model().objects.get(id=int(user_id))
            if hasattr(user, 'mkulima'):
                mkulima = user.mkulima
                serialize = MkulimaProfileSerializer(mkulima)
                return Response(serialize.data, status=status.HTTP_200_OK)
            
            if hasattr(user, 'researcher'):
                researcher = user.researcher
                serialize = ResearcherProfileSerializer(researcher)
                return Response(serialize.data, status=status.HTTP_200_OK)
            
            if hasattr(user, 'officer'):
                officer = user.officer
                serialize = OfficerProfileSerializer(officer)
                return Response(serialize.data, status=status.HTTP_200_OK)
            return Response({"details": "Unrecognized user group"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
user_details = UserDetalsAPIView.as_view()


class DeleteUserAPIView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        try:
            user = get_user_model().objects.get(id=int(user_id))
            user.delete()
            return Response({"details": "User deleted successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

delete_user = DeleteUserAPIView.as_view()


class CompleteOfficerProfile(APIView):
    def post(self, request):
        try:
            user_id = request.data.get("user_id")
            name = request.data.get("name")
            gender = request.data.get("gender")
            profile = request.data.get("profile")
            address =request.data.get("address")
            user = get_user_model().objects.get(id=int(user_id))
           
            if hasattr(user, "officer"):
                officer = user.officer

                officer.name = name
                officer.gender = gender
                officer.physical_address = address
                if (profile != 'null' and profile != None):
                    officer.image = profile

                officer.is_active = False
                officer.profile_is_completed = True

                officer.save()

                serializer = OfficerProfileSerializer(officer)

                return Response(serializer.data, status=status.HTTP_200_OK)
            
            else:
                return Response({ "details": "This intended only for officer"}, status=status.HTTP_406_NOT_ACCEPTABLE)


        except Exception as e:
            print("Error ", str(e))
            return Response({ "details": str(e) }, status=status.HTTP_400_BAD_REQUEST)

complete_officer_profile = CompleteOfficerProfile.as_view()


class CompleteResearcherProfile(APIView):
    def post(self, request):
        try:
            user_id = request.data.get("user_id")
            name = request.data.get("name")
            gender = request.data.get("gender")
            profile = request.data.get("profile")
            address = request.data.get("address")

            user = get_user_model().objects.get(id=int(user_id))
            
            print(dir(user))
            if hasattr(user, "researcher"):
                researcher = user.researcher

                researcher.name = name
                researcher.gender = gender
                researcher.physical_address = address

                if (profile != 'null' and profile != None):
                    researcher.image = profile

                researcher.is_active = False
                researcher.profile_is_completed = True

                researcher.save()

                serializer = ResearcherProfileSerializer(researcher)

                return Response(serializer.data, status=status.HTTP_200_OK)

            else:
                return Response({ "details": "This intended only for researcher"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except Exception as e:
            print("Error ", str(e))
            return Response({ "details": str(e) }, status=status.HTTP_400_BAD_REQUEST)
        
complete_researcher_profile = CompleteResearcherProfile.as_view()

class CreateResearchArticle(APIView):
    def post(self, request):
        print("Im get called")
        title = request.data.get('title')
        content = request.data.get('content')
        category = request.data.get('category')
        user_id = request.data.get("user_id")
        total_files = request.data.get('total_media')

        print("Media file ", total_files)
        # this total_files will tell us how many files get uploaded if its "media2" then there 
        # are two files get uploaded "media", "media1"
        # print("media", media)
        try:
            user = get_user_model().objects.get(id=int(user_id))

            author = user
            rpost = RawPost.objects.create(
                title = title,
                content = content,
                author = author,
                category = category
            )

            for index in range(int(total_files[-1])):
                print("index ", index)
                if index == 0:
                    media = request.data.get('media')
                    print("This is initial media uploaded ", media)
                    print("media ", media)
                    pmedia = PostMedia.objects.create(
                        media = media
                    )
                    pmedia.save()

                    rpost.media.add(pmedia)
                
                else:
                    print(index)
                    field = 'media' + str(index)
                    print('field ', field)
                    media = request.data.get(field)
                    print("These are other media uploaded ", media)
                    pmedia = PostMedia.objects.create(
                        media = media
                    )
                    pmedia.save()

                    rpost.media.add(pmedia)


            rpost.save()
            serializer = RawPostSerializer(rpost)

            return Response(serializer.data, status=status.HTTP_200_OK)


        except Exception as err:
            print("Exception ", str(err))
            return Response({ "details": str(err)}, status=status.HTTP_400_BAD_REQUEST)


create_article = CreateResearchArticle.as_view()

class ResearcherArticles(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")

        user = get_user_model().objects.get(id=int(user_id))    
        posts = user.posts.all()
        posts = reversed(posts)
        serializer = RawPostSerializer(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

r_articles = ResearcherArticles.as_view()

class ArticlesList(APIView):
    def get(self, request):
        try:
            posts = RawPost.objects.all()
            posts = reversed(posts)
            serializer = RawPostSerializer(posts, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
articles_list = ArticlesList.as_view()

class UpdateArticle(APIView):
    def post(self, request):
        try:
            post_id = request.data.get("post_id")
            title = request.data.get("title")
            content = request.data.get("content")
            category = request.data.get("category")
            total_files = request.data.get('total_media')
            trimmed_media = request.data.get("trimmed_media")
            print(post_id, title, content, category)
            print("total files ", total_files)
            print("trimmed media ", trimmed_media)
            for tm in json.loads(trimmed_media):
                media = PostMedia.objects.get(id=int(tm))
                media.delete()

            post = RawPost.objects.get(id=int(post_id))
            post.title = title
            post.content = content
            post.category = category

            # no need to send back the urls of files already added to the server in 
            # some cases if the file is trimmed we need you to send us the ids of the files
            # which are trimmed so that we can delete them from the server

            for index in range(int(total_files[-1])):
                print("index ", index)

                if index == 0:
                    media = request.data.get('media')
                    print("This is initial media uploaded ", media)
                    print("media ", media)
                    pmedia = PostMedia.objects.create(
                        media = media
                    )
                    pmedia.save()

                    post.media.add(pmedia)
                
                else:
                    print(index)
                    field = 'media' + str(index)
                    print('field ', field)
                    media = request.data.get(field)
                    print("These are other media uploaded ", media)
                    pmedia = PostMedia.objects.create(
                        media = media
                    )
                    pmedia.save()

                    post.media.add(pmedia)

            post.save()
            serializer = RawPostSerializer(post)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            print("THESE ARE ERRORS ", str(e))
            return Response({"details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

update_article = UpdateArticle.as_view()
class OfficerPosts(APIView):
    def post(self, request):
        try:
            user_id = request.data.get("user_id")
            user = get_user_model().objects.get(id=int(user_id))
            officer = user.officer
            posts = officer.officerposts.all()
            posts = reversed(posts)
            serializer = RawPostSerializer(posts, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
officer_posts = OfficerPosts.as_view()
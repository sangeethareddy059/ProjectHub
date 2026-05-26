
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from .models import Reviews, Users, Projecttitles, ChatMessage

import json
import re


@csrf_exempt
def reviews(request):

    if request.method == 'GET':

        all_reviews = Reviews.objects.all().order_by('-created_at')

        data = []

        for review in all_reviews:

            data.append({

                'student_name': review.student_name,

                'project_domain': review.project_domain,

                'rating': review.rating,

                'review_text': review.review_text,

                'improvement_text': review.improvement_text,

                'created_at': review.created_at.strftime("%d %B %Y")

            })

        return JsonResponse(data, safe=False)


    if request.method == 'POST':

        data = json.loads(request.body)

        Reviews.objects.create(

            student_name=data['student_name'],

            project_domain=data['project_domain'],

            rating=data['rating'],

            review_text=data['review_text'],

            improvement_text=data['improvement_text']

        )

        return JsonResponse({

            'message': 'Review Added Successfully'

        })






@csrf_exempt
def project_list(request):

    # GET PROJECTS

    if request.method == 'GET':

        projects = Projecttitles.objects.all()

        data = []


        for project in projects:

            data.append({

                'id': project.id,

                'title': project.title,

                'domain': project.domain,

                'technologies':
                project.technologies,

                'description':
                project.description
                if project.description
                else "",

                'image':
                request.build_absolute_uri(
                    project.image.url
                ) if project.image
                else "",

            })


        return JsonResponse(
            data,
            safe=False
        )



    # ADD PROJECT

    elif request.method == 'POST':

        data = json.loads(
            request.body
        )


        Projecttitles.objects.create(

            title=data.get('title'),

            domain=data.get('domain'),

            technologies=data.get(
                'technologies'
            ),

            description=data.get(
                'description'
            )

        )


        return JsonResponse({

            'message':
            'Project Added Successfully'

        })




@csrf_exempt
def delete_project(request, id):

    if request.method == 'DELETE':

        project = Projecttitles.objects.get(
            id=id
        )

        project.delete()


        return JsonResponse({

            'message':
            'Project Deleted Successfully'

        })


    return JsonResponse({

        'message':
        'Delete API Working'

    })


@csrf_exempt
def register(request):

    if request.method == 'POST':

        data = json.loads(request.body)

        name = data.get('name')

        email = data.get('email')

        password = data.get('password')


        email_pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'


        if not re.match(email_pattern, email):

            return JsonResponse({

                'error':
                'Email must be in @gmail format'

            }, status=400)


        password_pattern = (
            r'^(?=.*[A-Z])'
            r'(?=.*\d)'
            r'(?=.*[@$!%*?&])'
            r'[A-Za-z\d@$!%*?&]{6,}$'
        )


        if not re.match(
            password_pattern,
            password
        ):

            return JsonResponse({

                'error':
                'Password must contain minimum 6 letters, 1 capital letter, 1 number and 1 special character'

            }, status=400)


        existing_user = Users.objects.filter(
            email=email
        ).first()


        if existing_user:

            return JsonResponse({

                'error':
                'Email already registered'

            }, status=400)


        Users.objects.create(

            name=name,

            email=email,

            password=password

        )


        return JsonResponse({

            'message':
            'Registered Successfully'

        })




@csrf_exempt
def login(request):

    if request.method == 'POST':

        data = json.loads(request.body)

        email = data.get('email')

        password = data.get('password')


        user = Users.objects.filter(
            email=email
        ).first()


        if not user:

            return JsonResponse({

                'error':
                'Incorrect credentials. Please enter correct details.'

            }, status=400)


        if user.password != password:

            return JsonResponse({

                'error':
                'Incorrect credentials. Please enter correct details.'

            }, status=400)


        return JsonResponse({

            'message':
            'Login Successful',

            'username':
            user.name

        })


@csrf_exempt
def forgot_password(request):

    if request.method == 'POST':

        try:

            data = json.loads(
                request.body
            )

            email = data.get(
                'email'
            )

            new_password = data.get(
                'new_password'
            )


            user = Users.objects.filter(
                email=email
            ).first()


            if not user:

                return JsonResponse({

                    'error':
                    'Email not registered'

                }, status=400)


            password_pattern = (
                r'^(?=.*[A-Z])'
                r'(?=.*\d)'
                r'(?=.*[@$!%*?&])'
                r'[A-Za-z\d@$!%*?&]{6,}$'
            )


            if not re.match(
                password_pattern,
                new_password
            ):

                return JsonResponse({

                    'error':
                    'Password must contain minimum 6 letters, 1 capital letter, 1 number and 1 special character'

                }, status=400)


            user.password = new_password

            user.save()


            return JsonResponse({

                'message':
                'Password Changed Successfully'

            })


        except Exception as e:

            return JsonResponse({

                'error':
                str(e)

            }, status=500)


    return JsonResponse({

        'message':
        'Forgot Password API Working'

    })



@csrf_exempt
def send_message(request):

    if request.method == 'POST':

        data = json.loads(
            request.body
        )

        username = data.get(
            'username'
        )

        message = data.get(
            'message'
        )


        ChatMessage.objects.create(

            username=username,

            message=message

        )


        return JsonResponse({

            'message':
            'Message Sent Successfully'

        })


    return JsonResponse({

        'message':
        'Chat API Working'

    })



@csrf_exempt
def admin_login(request):

    if request.method == 'POST':

        data = json.loads(
            request.body
        )

        email = data.get(
            'email'
        )

        password = data.get(
            'password'
        )


        if (

            email == "sangeethareddy059gmail.com"

            and

            password == "Chinni@123"

        ):

            return JsonResponse({

                'message':
                'Admin Login Successful'

            })


        return JsonResponse({

            'error':
            'Invalid Admin Credentials'

        }, status=400)


    return JsonResponse({

        'message':
        'Admin Login API Working'

    })
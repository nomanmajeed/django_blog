from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from home.models import Profile
from common.helpers import generate_random_string

class RegisterView(APIView):

    def post(self, request):
        response = {'status': 500, 'message': 'Something went wrong'}
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')

            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')
            check_user = User.objects.filter(
                username=data.get('username')).first()
            if check_user:
                response['message'] = 'username  already taken'
                raise Exception('username  already taken')

            user_obj = User.objects.create(email=data.get('username'),
                                           username=data.get('username').split('@')[0])
            user_obj.set_password(data.get('password'))
            user_obj.save()
            token = generate_random_string(20)
            # set verified user
            Profile.objects.create(user=user_obj, token=token,
                                   is_verified=True)
            # send_mail_to_user(token , data.get('username'))
            response['message'] = 'User created '
            response['status'] = 200
        except Exception as e:
            print(e)

        return Response(response)


RegisterView = RegisterView.as_view()
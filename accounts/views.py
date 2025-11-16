import logging
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, LoginSerializer, AuthResponseSerializer, UserSerializer

logger = logging.getLogger('gatoflix.auth')


class AuthThrottle(AnonRateThrottle):
    """Rate limit for authentication endpoints."""
    scope = 'auth'
    THROTTLE_RATES = {'auth': '5/min'}


class RegisterView(views.APIView):
    """
    User registration endpoint.
    POST /auth/register/
    Returns: {user, access, refresh}
    """
    
    permission_classes = []
    authentication_classes = []
    # throttle_classes = [AuthThrottle]
    
    def post(self, request):
        """Register new user."""
        username = request.data.get('username', 'unknown')
        
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            # Generate tokens
            refresh = RefreshToken.for_user(user)
            
            logger.info(f"User registered successfully: {username} (ID: {user.id})")
            
            response_data = {
                'user': UserSerializer(user).data,
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
            
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        logger.warning(f"Registration failed for username: {username}. Errors: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    """
    User login endpoint with JWT tokens.
    POST /auth/login/
    Accepts: {username, password}
    Returns: {user, access, refresh}
    """
    
    serializer_class = LoginSerializer
    permission_classes = []
    authentication_classes = []
    # throttle_classes = [AuthThrottle]
    
    def post(self, request, *args, **kwargs):
        """Login user and return tokens with user data."""
        username = request.data.get('username', 'unknown')
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            try:
                user = User.objects.get(username=request.data.get('username'))
                logger.info(f"Successful login: {username} (ID: {user.id})")
            except User.DoesNotExist:
                logger.warning(f"Failed login attempt - invalid credentials for username: {username}")
                return Response(
                    {'detail': 'Credenciais inválidas.'},
                    status=status.HTTP_401_UNAUTHORIZED
                )
            
            response_data = {
                'user': UserSerializer(user).data,
                'access': str(serializer.validated_data.get('access')),
                'refresh': str(serializer.validated_data.get('refresh')),
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
        
        logger.warning(f"Failed login attempt for username: {username}. Invalid credentials.")
        return Response(
            {'detail': 'Credenciais inválidas.'},
            status=status.HTTP_401_UNAUTHORIZED
        )


class UserDetailView(views.APIView):
    """
    Get current authenticated user details.
    GET /auth/me/
    Returns: {id, username, email, first_name, last_name}
    """
    
    def get(self, request):
        """Get current user info."""
        if not request.user.is_authenticated:
            return Response(
                {'detail': 'Não autenticado.'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

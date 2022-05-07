import uuid

from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_superuser(self, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.'
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.'
            )
        return self.create_user(username, password, **other_fields)

    def create_user(self, username, password, **other_fields):
        if not username:
            raise ValueError(
                'You must provide username'
            )
        user = self.model(username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def register_admin(self, payload):
        print(f'Debug = {payload}')
        user = self.model(
            username=payload.get('username'),
            email=payload.get('email'),
            first_name=payload.get('first_name'),
            last_name=payload.get('last_name'),
            role="ADMIN",
            mobile_number=payload.get('mobile_number'),
            is_active=True,
            is_verified=True
        )

        user.parent_code = uuid.uuid4()
        user.save()

        username = user.first_name[0] + user.last_name
        password = f"{username}@admin"

        user.set_password(password)
        user.save()
        return user

    def register_general_user(self, request, username):
        print(f'Debug = {request.data}')
        
        user = self.model(
            username=username,
            email=request.data.get('email'),
            first_name=request.data.get('first_name'),
            last_name=request.data.get('last_name'),
            role=request.data.get('role'),
            mobile_number=request.data.get('mobile_number'),
            parent_code=request.user.parent_code,
            is_active=True,
            is_verified=True
        )

       
        password = f"{username}@tutor"

        user.set_password(password)
        user.save()
        return user    

    def find_by_email(self, email):
        return self.filter(email=email).first()    

    def find_by_username(self, username):
        return self.filter(username=username).first()

    def find_users_by_role(self, role):
        return self.filter(role__icontains=role)

    def find_by_uuid(self, pk):
        return self.filter(id=pk).first()

    
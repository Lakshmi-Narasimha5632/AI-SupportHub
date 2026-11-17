
# AI SupportHub - API Documentation

## 1. API Overview

Base URL (development):

http://127.0.0.1:8000/api/

API Format: JSON

Authentication: JWT Bearer Token

## 2. Authentication APIs

### 2.1 Customer Registration

Endpoint:
POST /api/auth/register/

Authentication:
Not required.

Request:

{
    "full_name": "Narasimha",
    "email": "narasimha@example.com",
    "password": "StrongPass@123",
    "password2": "StrongPass@123"
}

Success Response: 201 Created

{
    "message": "Customer registered successfully.",
    "user": {
        "id": 1,
        "full_name": "Narasimha",
        "email": "narasimha@example.com",
        "role": "CUSTOMER"
    }
}

Possible Errors:
- 400: Invalid input.
- 400: Email already exists.
- 400: Passwords do not match.
- 400: Password does not meet validation rules.

### 2.2 User Login

Endpoint:
POST /api/auth/login/

Authentication:
Not required.

Request:

{
    "email": "narasimha@example.com",
    "password": "StrongPass@123"
}

Success Response: 200 OK

{
    "message": "Login successful",
    "user": {
        "id": 1,
        "full_name": "Narasimha",
        "email": "narasimha@example.com",
        "role": "CUSTOMER"
    },
    "tokens": {
        "access": "<access_token>",
        "refresh": "<refresh_token>"
    }
}

Possible Errors:
- 400: Invalid email or password.
- 400: Account is inactive.
- 429: Too many login attempts.

### 2.3 JWT Token Refresh

Endpoint:
POST /api/auth/token/refresh/

Authentication:
Refresh token required in request body.

Request:
{
    "refresh": "<refresh_token>"
}

Success Response: 200 OK

{
    "access": "<new_access_token>",
    "refresh": "<new_refresh_token>"
}

Possible Errors:
- 401: Invalid refresh token.
- 401: Expired refresh token.
- 401: Blacklisted refresh token.

Refresh Token Rotation:
- Generates a new access token.
- Generates a new refresh token.
- Blacklists the previous refresh token.


### 2.4 User Logout API

Endpoint:
POST /api/auth/logout/

Authentication:
Valid refresh token required in request body.

Request:

{
    "refresh": "<refresh_token>"
}

Success Response: 200 OK

{
    "message": "Logout successful."
}

Possible Errors:
- 400: Invalid or expired refresh token.
- 400: Unable to blacklist token.

Functionality:
- Validates the refresh token.
- Adds the refresh token to the blacklist.
- Prevents future use of that refresh token.
- Frontend must clear stored access and refresh tokens.


### 2.5 User Profile API

#### Retrieve Profile

Method: GET

Endpoint: /api/auth/profile/

Authentication: Required (JWT Access Token)

Success Response: 200 OK

Returns the authenticated user's profile.

#### Update Profile

Method: PATCH

Endpoint: /api/auth/profile/

Authentication: Required (JWT Access Token)

Request:

{
    "full_name": "Lakshmi Narasimha"
}

Success Response: 200 OK

Returns the updated user profile.

Possible Errors:
- 400: Invalid input.
- 401: Authentication required.

Security:
- Users can only access their own profiles.
- Email and role cannot be modified through this endpoint.
- Account status is read-only.


## 3. JWT Authentication

For protected endpoints, include the access token in the request header.

Authorization: Bearer <access_token>

Access token lifetime: 15 minutes.

Refresh token lifetime: 7 days.

## 4. Planned Authentication Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /api/auth/token/refresh/ | Refresh JWT tokens |
| POST | /api/auth/logout/ | Logout and blacklist refresh token |
| GET | /api/auth/profile/ | Get current user profile |
| PATCH | /api/auth/profile/ | Update user profile |
| POST | /api/auth/google/ | Google authentication |

## 5. Planned Customer APIs

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /api/customers/ | List customers |
| GET | /api/customers/{id}/ | Customer details |
| PATCH | /api/customers/{id}/ | Update customer |

## 6. Planned Ticket APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /api/tickets/ | Create ticket |
| GET | /api/tickets/ | List tickets |
| GET | /api/tickets/{id}/ | Ticket details |
| PATCH | /api/tickets/{id}/ | Update ticket |
| POST | /api/tickets/{id}/comments/ | Add comment |
| POST | /api/tickets/{id}/assign/ | Assign agent |

## 7. Planned AI APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /api/ai/analyze-ticket/ | Analyze ticket |
| POST | /api/ai/suggest-reply/ | Generate reply suggestion |
| POST | /api/ai/chat/ | FAQ chatbot |

## 8. Response Status Codes

| Code | Meaning |
|---|---|
| 200 | Successful request |
| 201 | Resource created |
| 400 | Bad request |
| 401 | Authentication required |
| 403 | Permission denied |
| 404 | Resource not found |
| 429 | Too many requests |
| 500 | Internal server error |

## 9. Documentation Maintenance

Update this document whenever a new API endpoint is created or modified.

Only mark an endpoint as implemented after it has been tested successfully.

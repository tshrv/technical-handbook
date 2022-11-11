# Authentication
- Verify you who you say you are
  - what you know - password, pin, pattern etc.
  - what you possess - key, phone, bluetooth, etc.
  - what you are - biometrics
- Done via username and password
- Multiple layers such as MFA, OTP, etc.


# Authorization
- Username associated with a set of permissions
  - RBAC - role based
  - ABAC - attribute based, more granular, adds other attributes such as geographical data, etc.

# Password Hashers in Django
How password is hashed, algo used, password matching on login etc. [https://docs.djangoproject.com/en/4.1/topics/auth/passwords/](https://docs.djangoproject.com/en/4.1/topics/auth/passwords/)

The password attribute of a User object is a string in this format: `<algorithm>$<iterations>$<salt>$<hash>`

By default, Django uses the `PBKDF2` algorithm with a `SHA256` hash, a password stretching mechanism recommended by **NIST**. This should be sufficient for most users: it’s quite secure, requiring massive amounts of computing time to break.

```python
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.ScryptPasswordHasher',
]
```

For storing passwords, Django will use the **first hasher** in `PASSWORD_HASHERS`. To store new passwords with a different algorithm, put your preferred algorithm first in `PASSWORD_HASHERS`.

For verifying passwords, Django will find the hasher in the list that matches the algorithm name in the stored password. If a stored password names an algorithm not found in `PASSWORD_HASHERS`, trying to verify it will raise `ValueError`.

# Types of Authentication
- BasicAuth
  - Requires username and password everytime
  
- TokenAuth - generates a token, which has an expiry. All further requests need to have this token. Near expiry, get a new token via something like `refresh_token_api`
  - Preferable between server-server connections.
  - Example - Azure PAT, Access tokens for dev apis, they will expire after a date.
  - No user auth performed, if a request comes in and has the token which is valid, request passes through, irrespective of who sent the request. No way to link user to token.
  - Authentication details stored at user
  - Request has token for authentication 

- SessionAuth
  - Preferable for server-client connections. Where server can invalidate sessions.
  - Authentication details stored at server
  - Request has cookie for authentication 
  - Server send cookie to user, which is later used to track user activity and create a better user experience, reducing storage responsibilities on the server.

- JWT
  - xxxxx.yyyyy.zzzzz
  - **Header** - The header typically consists of two parts: the type of the token, which is JWT, and the signing algorithm being used, such as `HMAC SHA256` or `RSA`.
    - ```json
      {
        "alg": "HS256",
        "typ": "JWT"
      }
      ```
    - Then, this JSON is `Base64Url` encoded to form the first part of the JWT.
  - **Payload**
    -  contains the claims
    -  Claims are statements about an entity (typically, the user) and additional data
    -  There are three types of claims: `registered`, `public`, and `private` claims(actual data being shared between parties).
       -  `registered` - 
          -  not mandatory but recommended
          -  Some of them are: `iss` (issuer), `exp` (expiration time), `sub` (subject), `aud` (audience), and others
       -  `public` - 
          -  These can be defined at will by those using JWTs.
       -  `private` - 
          -  custom claims created to share information between parties that agree on using them
    - ```json
       {
         "sub": "1234567890",
         "name": "John Doe",
         "admin": true
       }
       ```
    - The payload is then `Base64Url` encoded to form the second part of the JSON Web Token.
    - **Note** Do note that for signed tokens this information, though protected against tampering, is readable by anyone. Do not put secret information in the payload or header elements of a JWT unless it is encrypted.
  
  - **Signature**
    - To create the signature part you have to take the encoded header, the encoded payload, a secret, the algorithm specified in the header, and **sign that**.
    - ```js
      HMACSHA256(
        base64UrlEncode(header) + "." +
        base64UrlEncode(payload),
        secret
      )
      ```
    - The signature is used to verify the message wasn't changed along the way
    - In the case of tokens *signed with a private key*, it can also verify that the sender of the JWT is who it says it is.

  - The output is three Base64-URL strings separated by dots that can be easily passed in `HTML` and `HTTP` environments, while *being more compact when compared to `XML`-based standards such as `SAML`*.

  - Whenever the user wants to access a protected route or resource, the user agent should send the `JWT`, typically in the **Authorization** header using the **Bearer** schema.
    ```
    Authorization: Bearer <token>
    ```
  - This can be, in certain cases, a stateless authorization mechanism.
  - If the JWT contains the necessary data, the need to query the database for certain operations may be reduced, though this may not always be the case.
  - If the token is sent in the `Authorization` header, `Cross-Origin Resource Sharing (CORS)` won't be an issue as it doesn't use cookies.

- OAuth

- SSO
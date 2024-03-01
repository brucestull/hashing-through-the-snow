# Hashing Through the Snow (Password Hashing in Django)

- [GitHub Repository](https://github.com/brucestull/hashing-through-the-snow)

## Virtual Environment Location

- `C:\Users\FlynntKnapp\.virtualenvs\hashing-through-the-snow-rZsDGVvg\`

## Django Commands


Django app to learn about password hashing.

## Django Example Admin Credentials

- SECRET_KEY: 'django-insecure-vzs&-rw)0on5#h$%zlsr)#hs0%5ady9aiquz3t(rei#jpz%2^y'

### Username: FlynntKnapp
- `python manage.py createsuperuser --email FlynntKnapp@email.app --username FlynntKnapp`
- Password: 1234test

- ID: 1
- Algorithm: pbkdf2_sha256
- Iterations: 720000
- Salt: zr9jWICTX5VFI2kulq90CF
- Hash: hnwgpKgfDxZw0dkkVr6WebLdDJGlaZM3JBaFYB0vJ0I=

### Username: FlynntKnapq
- `python manage.py createsuperuser --email FlynntKnapp@email.app --username FlynntKnapq`
- Password: 1234test

- ID: 2
- Algorithm: pbkdf2_sha256
- Iterations: 720000
- Salt: L4k0CovAjpoTGk3zmb754P
- Hash: 4sQ/Gh7iJlx+LnyHscltzSGm9rG/nr6pehnOZ1TlOy8=

### Username: FlynntKnapq
- `python manage.py createsuperuser --email FlynntKnapp@email.app --username FlynntKnapq`
- Password: 1234test

- ID: 3
- Algorithm: pbkdf2_sha256
- Iterations: 720000
- Salt: e2N78fBDRO8EZdgdHKr0c9
- Hash: VXUVN9xUq+vzc5n87T/PwwuH8V0PtWggBsnmM/SGmWg=


### Username: FlynntKnapq
1. `generic_user = User(pk=1, username="FlynntKnapq", email="FlynntKnapp@email.app")`
1. `generic_user.save(force_insert=True)`
1. `generic_user.set_password("1234test")`
1. `generic_user.save()`

- ID: 2
- Algorithm: pbkdf2_sha256
- Iterations: 720000
- Salt: 3QvKB5g2go6CHtpliYOtYR
- Hash: CvoHLiPqj+gTYTWFmrfXjDb912Jjvut+QAk5Blq6UXQ=

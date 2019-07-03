Application to measure loading time of our website and few other competitors. If our site is slower than one of competitors application should send email, if our site is two times slower then application should send message via sms.

Todo:
- [ ] Write more tests
- [ ] Provide more docstrings
- [ ] Fix syntactical and stylistic problems (linter)

Instalation:
```
pip install -r requirements.txt
```

Unit tests:
```
bolt ut
```

Configuration config.json:
```
// config.json
{
    "DEFAULT": {
        "PORT" : 465,
        "SMTP_SERVER" : "smtp.gmail.com",
        "SENDER_EMAIL" : "my@gmail.com",
        "RECEIVER_EMAIL" : "your@gmail.com",
        "PASSWORD" : "password"
    }
}
```

Run script:
```
python src/main.py
```

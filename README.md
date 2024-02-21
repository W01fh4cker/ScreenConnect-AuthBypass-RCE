# ScreenConnect-AuthBypass-POC-EXP

# How to use

```
pip install requests
python poc.py
python exp.py
```

![](https://github.com/W01fh4cker/ScreenConnect-AuthBypass-POC-EXP/assets/101872898/9f9be7be-d607-4fcf-97dc-2d8a4939db5e)

# What you need to change

Change it to the username and password you want to add, and customize the domain (this variable is not important, for example poc.com)

![](https://github.com/W01fh4cker/ScreenConnect-AuthBypass-POC-EXP/assets/101872898/905ef456-75f5-472d-a996-798f8cec8640)

# Cyberspace mapping statement

## Odin

```
services.modules.http.headers.server:"screenconnect"
```

## Zoomeye
```
app:"ScreenConnect Remote Management Software"
```

## Censys

```
services.http.response.headers:(key: `Server` and value.headers: `ScreenConnect`)
```

## Shodan

```
"Server: ScreenConnect"
```

## Hunter.how

```
product.name="ConnectWise ScreenConnect software"
```

## Fofa

```
app="ScreenConnect-Remote-Support-Software"
```

# Reference

https://www.connectwise.com/company/trust/security-bulletins/connectwise-screenconnect-23.9.8

https://github.com/watchtowrlabs/connectwise-screenconnect_auth-bypass-add-user-poc
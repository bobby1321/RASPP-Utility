# Repeated Automated Sprocket Part Placement Utility (RASPP)
This tool allows you to easily place items in the game Sprocket in patterns by modifying the blueprint file for your vehicle. 


<img src="https://user-images.githubusercontent.com/36699941/181866912-ce38f0ba-054c-4754-ac23-568f5764b45a.gif" alt="position" width="500"/><img src="https://user-images.githubusercontent.com/36699941/181866937-afd2a876-b9a7-44f1-afdc-48c028dbe5e3.png" alt="position" width="300"/>

## How to use RASPP
Here is a not-so-quick guide on how to use RASPP:

 1. Place the desired part on your vehicle in Sprocket. Make sure to place it where you want the pattern to start, and that it is correctly rotated and scaled the way you want.
 2. Save the vehicle in Sprocket
 3. **SAVE A COPY OF THE VEHICLE BEFORE MAKING ANY CHANGES TO THE BLUEPRINT FILE!** I am not responsible for you messing up your blueprint.
 4. Open your Sprocket blueprints folder, which can be found at `C:\Users\[You]\Documents\My games\Sprocket\Factions\[Your Faction]\Blueprints\Vehicles`
 5. Open the `.blueprint` file of your vehicle
 6. Find the part that you want to clone. This can be tricky, so look at the part reference number (**REF**) (lookup table coming soon) and the compartment ID (**CID**), as well as the location/rotation/scale of the part to try to find the right one.
 7. Copy the part information into RASPP by pasting it in the `Input` popup. It should look like this:
	 ```
	 {
      "REF": "0633ffdf766e3394eb79f8e8a7be24ba",
      "CID": 0,
      "T": [
        -0.46639204,
        0.591725945,
        -3.118866,
        3.58584948E-05,
        89.99991,
        245.606354,
        0.799310863,
        0.500000238,
        0.9819551,
        0.0
      ],
      "DAT": []
    }, 
    ```
    After pasting the information, hit the `OK` button to automatically fill the information into the boxes in RASPP.
    
8. Use the buttons in the top row to select how you want the part to be cloned. You can enter either an amount of parts, or select an axis to move on until a certain coordinate is hit. 
9. Enter increment amounts for each axis you want to be incremented. This value changes how far apart each part is or how much more it is rotated or scaled.
10. Change any values that you want to change. You can move the part, rotate it or scale it (RASPP *cannot* scale parts beyond the limits of the game) however you like. 
11. Select where you want to save the output file and give it a name using `File -> Change Save Location` or `Ctrl + S`
12. Once you have all of your values filled, press the `Go!` button. The output file you saved before should now be populated with parts.
13. **Paste the output over the original part**. Otherwise, you can end up with stacked parts, or any changes you made to the part might not be saved.
14. Save and close the `.blueprint` file. 
15. In Sprocket, open the vehicle you changed. Even if it is already open, re-open it.
16. If you are happy with the changes, save your vehicle in-game. Otherwise, start over and change some numbers.

## FAQ

 - **Q: Where do I find the blueprint files?** A: RTFM.
 - **Q: Where do I look in the file to find a part?** A: Parts are after the `Compartments` and  vehicle options (`SS, TRK, ENG, etc`) sections. If you scroll all the way down to the bottom of the `blueprint` file you can find them and go up from there. You can also look for the "ext" tag in whatever text editor you're using.
 - **Q: My output file is blank!** A: check to make sure that your amount is not zero, or that your limit is not inside of your increment (If you are trying to go from 0.75 to 1.25 in steps of 1, then you can't ever have a part, can you?). Also, make sure you are looking in the correct file. The file location can be found in `File -> Change Save Location`.
 - **Q: How do I know which axis is which / which way negative or positive is?** A: The values are ordered in the `blueprint` the same way they are ordered in RASPP: Position (X, Y, Z), Rotation (X, Y, Z), Scale (X, Y, Z). The X axis is from left to right, with right being positive, Y is up/down with up being positive, and Z is front/back with front being positive.  In the pictures below, X is red, Y is blue and Z is green.
 
	<img src="https://user-images.githubusercontent.com/36699941/181866228-a537e6f9-32fc-44d1-bcb7-7e4e16f51806.png" alt="position" width="250"/>
	<img src="https://user-images.githubusercontent.com/36699941/181866229-a6299564-b33a-4168-84a8-a6465e387b85.png" alt="position" width="250"/>
	<img src="https://user-images.githubusercontent.com/36699941/181866232-b4dc5bab-c4fe-4344-aef5-6bffb1c91b26.png" alt="position" width="250"/>

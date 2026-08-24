-- Optional PolyCraft menu for 3ds Max 2027+.
-- fileIn this after the repo path is known. Sets a global to the max/ folder.

(
    if (maxVersion())[1] < 29000 then
    (
        format "PolyCraft menu skipped: need Max 2027 (29000).\n"
    )
    else
    (
        global POLYCRAFT_MAX_DIR = getFilenamePath (getThisScriptFilename())

        macroScript PolyCraftBootstrap
            category:"PolyCraft"
            tooltip:"Bootstrap units, grid, layers"
            buttonText:"Bootstrap scene"
        (
            local p = POLYCRAFT_MAX_DIR + "polycraft_bootstrap.ms"
            if POLYCRAFT_MAX_DIR != undefined and doesFileExist p then
                fileIn p
            else
                messageBox "fileIn max/polycraft_bootstrap.ms from the PolyCraft repo (menu lost the path)." title:"PolyCraft"
        )

        try
        (
            local mainMenu = menuMan.getMainMenuBar()
            local existing = menuMan.findMenu "PolyCraft"
            if existing != undefined then menuMan.unRegisterMenu existing

            local pcMenu = menuMan.createMenu "PolyCraft"
            local action = menuMan.createActionItem "PolyCraftBootstrap" "PolyCraft"
            pcMenu.addItem action -1
            local sub = menuMan.createSubMenuItem "PolyCraft" pcMenu
            mainMenu.addItem sub (mainMenu.numItems() + 1)
            menuMan.updateMenuBar()
            format "PolyCraft menu registered from %\n" POLYCRAFT_MAX_DIR
        )
        catch
        (
            format "PolyCraft menu registration failed; drag polycraft_bootstrap.ms instead. %\n" (getCurrentException())
        )
    )
)

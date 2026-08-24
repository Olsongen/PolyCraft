-- PolyCraft scene bootstrap — 3ds Max 2027 (R29 / 29000)
-- Run via:  python -m polycraft max bootstrap
-- Emergency: Scripting > Run Script (do not make drag-and-drop the loop).
-- Studio only: display meters, system centimeters, 0.5 m grid, generic layers.
-- Do not create kit-prefixed nodes here. Kit jobs live under kits/<id>/max/.

(
    if (maxVersion())[1] < 29000 then
    (
        messageBox "PolyCraft requires 3ds Max 2027 (maxVersion 29000 / R29)." title:"PolyCraft"
    )
    else undo "PolyCraft Bootstrap" on
    (
        units.SystemType = #centimeters
        units.SystemScale = 1.0
        units.DisplayType = #Metric
        units.MetricType = #meters

        -- 50 cm = 0.5 m. Majors every 2 lines = 1 m.
        SetGridSpacing 50.0
        SetGridMajorLines 2
        try (gridPrefs.spacing = 50.0) catch ()
        try (gridPrefs.majorLines = 2) catch ()
        try (gridPrefs.inhibitGridSubdivision = true) catch ()

        snapMode.active = true
        snapMode.type = #3D

        -- Studio bands only. Kit-specific layers (ARCH, VAULT, VEG, …) come from the kit script.
        local layerNames = #(
            "00_REF",
            "10_BLOCKOUT",
            "20_CRAFT",
            "60_ASSEMBLY",
            "90_QA"
        )
        for n in layerNames do
        (
            if LayerManager.getLayerFromName n == undefined then
                LayerManager.newLayerFromName n
        )

        local meterPlane = getNodeByName "PC_QA_meter_plane"
        if meterPlane == undefined then
        (
            meterPlane = Plane length:100 width:100 lengthsegs:1 widthsegs:1
            meterPlane.name = "PC_QA_meter_plane"
            meterPlane.wirecolor = color 180 140 70
            meterPlane.pivot = meterPlane.min
            meterPlane.pos = [0, 0, 0]
        )
        local qaLayer = LayerManager.getLayerFromName "90_QA"
        if qaLayer != undefined then qaLayer.addNode meterPlane

        local formatted = units.formatValue 400.0
        format "PolyCraft bootstrap OK. Display meters, system cm. 400 cm formats as %.\n" formatted
        format "Home grid 0.5 m, majors 1 m. Snap 3D. Studio node: PC_QA_meter_plane.\n"
        format "Next: python -m polycraft max job <kit-id> first-assembly\n"
        OK
    )
)

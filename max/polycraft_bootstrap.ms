-- PolyCraft scene bootstrap — 3ds Max 2027 (R29 / 29000)
-- DROP THIS FILE into a viewport (or Scripting > Run Script).
-- Display meters, system centimeters, 0.5 m grid, MHWR layers.

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

        local layerNames = #(
            "00_REF",
            "10_BLOCKOUT",
            "20_ARCH",
            "30_VAULT",
            "40_OVERLAY",
            "50_VEG",
            "60_ASSEMBLY",
            "90_QA"
        )
        for n in layerNames do
        (
            if LayerManager.getLayerFromName n == undefined then
                LayerManager.newLayerFromName n
        )

        local meterPlane = getNodeByName "MHWR_QA_meter_plane"
        if meterPlane == undefined then
        (
            meterPlane = Plane length:100 width:100 lengthsegs:1 widthsegs:1
            meterPlane.name = "MHWR_QA_meter_plane"
            meterPlane.wirecolor = color 180 140 70
            meterPlane.pivot = meterPlane.min
            meterPlane.pos = [0, 0, 0]
        )
        local qaLayer = LayerManager.getLayerFromName "90_QA"
        if qaLayer != undefined then qaLayer.addNode meterPlane

        local formatted = units.formatValue 400.0
        format "PolyCraft bootstrap OK. Display meters, system cm. 400 cm formats as %.\n" formatted
        format "Home grid 0.5 m, majors 1 m. Snap 3D. Next drop: max/mhwr_first_assembly.ms\n"
        OK
    )
)

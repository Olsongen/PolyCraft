-- Middlehelm wetlands — FIRST ASSEMBLY (blockout only)
-- Run via: python -m polycraft max job middlehelm-wetlands-ruins first-assembly
-- This is a kit script. Studio bootstrap must not create MHWR_ nodes.
-- FPS walk: two 4 m arcade bays + one 8 m wide bay, aisle, waterline, one standing vault.
-- System units = cm. 1.0 display meter = 100 cm.

(
    if (maxVersion())[1] < 29000 then
    (
        messageBox "PolyCraft requires 3ds Max 2027." title:"PolyCraft"
    )
    else if units.SystemType != #centimeters then
    (
        messageBox "Run max/polycraft_bootstrap.ms first (system units must be centimeters)." title:"PolyCraft"
    )
    else undo "MHWR First Assembly" on
    (
        local function ensureLayer n =
        (
            local lyr = LayerManager.getLayerFromName n
            if lyr == undefined then LayerManager.newLayerFromName n else lyr
        )

        local function addBox name w l h pos col layerName =
        (
            -- w=X, l=Y, h=Z in cm. Pivot at min corner, pos = that corner.
            local b = Box width:w length:l height:h
            b.name = name
            b.wirecolor = col
            b.pivot = b.min
            b.pos = pos
            local lyr = ensureLayer layerName
            lyr.addNode b
            b
        )

        -- Nave along +Y. Arcade on X=0. Nave floor X=100..500 (4 m). Aisle X=-200..100 (2 m + 1 m pier).
        -- Piers 1x1 m at Y = 0, 400, 800, 1600 along X=0.
        local colFloor = color 70 90 110
        local colWall = color 190 170 140
        local colPier = color 160 145 120
        local colTrim = color 90 140 120
        local colVault = color 210 195 170
        local colAisle = color 60 80 70

        -- Floors: two 4 m nave + one 8 m (wide bay)
        addBox "MHWR_floor_nave_4m_A" 400 400 8 [100, 0, 0] colFloor "10_BLOCKOUT"
        addBox "MHWR_floor_nave_4m_B" 400 400 8 [100, 400, 0] colFloor "10_BLOCKOUT"
        addBox "MHWR_floor_nave_8m" 400 800 8 [100, 800, 0] colFloor "10_BLOCKOUT"

        -- Aisle floors (2 m wide)
        addBox "MHWR_floor_aisle_2m" 200 1600 6 [-200, 0, 0] colAisle "10_BLOCKOUT"

        -- Arcade walls: 4 m, 4 m, 8 m — 8 m tall, 0.5 m thick, sitting on X=0 looking into nave
        addBox "MHWR_wall_arcade_4m_A" 50 400 800 [0, 0, 0] colWall "20_ARCH"
        addBox "MHWR_wall_arcade_4m_B" 50 400 800 [0, 400, 0] colWall "20_ARCH"
        addBox "MHWR_wall_arcade_8m" 50 800 800 [0, 800, 0] colWall "20_ARCH"

        -- Aisle outer wall
        addBox "MHWR_aisle_wall_2m" 50 1600 600 [-200, 0, 0] colWall "20_ARCH"

        -- Piers 1 m (at arcade / nave)
        addBox "MHWR_pier_1m_A" 100 100 800 [0, 0, 0] colPier "20_ARCH"
        addBox "MHWR_pier_1m_B" 100 100 800 [0, 400, 0] colPier "20_ARCH"
        addBox "MHWR_pier_1m_C" 100 100 800 [0, 800, 0] colPier "20_ARCH"
        addBox "MHWR_pier_1m_D" 100 100 800 [0, 1600, 0] colPier "20_ARCH"

        -- Waterline trim at 1.0 m (kit law), 0.1 m tall, along arcade face
        addBox "MHWR_trim_waterline_1m" 12 1600 10 [50, 0, 100] colTrim "20_ARCH"

        -- Standing vault over first 4 m bay only (open sky after)
        addBox "MHWR_vault_stand_4m" 400 400 40 [100, 0, 800] colVault "30_VAULT"

        -- FPS eye
        local lookAt = Targetobject pos:[300, 600, 160]
        lookAt.name = "MHWR_QA_fps_eye.Target"
        local cam = Targetcamera pos:[300, -150, 170] target:lookAt
        cam.name = "MHWR_QA_fps_eye"
        cam.fov = 90
        local qa = ensureLayer "90_QA"
        qa.addNode cam
        qa.addNode lookAt
        viewport.setCamera cam

        format "MHWR first assembly dropped. Walk the camera (eye 1.7 m). Do not detail yet.\n"
        format "Vaulted bay then open bay then 8 m wide bay. Waterline at 1.0 m.\n"
        OK
    )
)

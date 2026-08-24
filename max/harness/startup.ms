-- PolyCraft harness startup. fileIn from Max user startup, or via:
--   polycraft max install-harness
-- Agents drive Max through the API/CLI/MCP. Artists do not drag this.

(
    if (maxVersion())[1] < 29000 then
    (
        format "PolyCraft harness skipped: need Max 2027 (29000).\n"
    )
    else
    (
        local here = getFilenamePath (getThisScriptFilename())
        python.ExecuteFile (here + "listener.py")
    )
)

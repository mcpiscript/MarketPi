import os


def set_username(username: str):
    os.environ["MCPI_USERNAME"] = username
    
def set_render_distance(distance: str):
    if distance.upper() not in ["TINY", "SHORT", "NORMAL", "FAR"]:
        raise Exception("Invalid render distance")
    else:
        os.environ["MCPI_RENDER_DISTANCE"] = distance.upper()
        
def set_hud(options: str):
    os.environ["GALLIUM_HUD"] = options
        

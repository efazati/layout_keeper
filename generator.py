from config_4k_2k import modes, positions

def header_render():
    return """@echo off
set %ERRORLEVEL%=0

cmdow /ma"""

def apps_render(mode):
    app_cmd = []
    for app in mode['apps']:
        pos = positions[app['pos']]
        template = f"""
REM {app['pos']}
cmdow "*{app['name']}*" /Res
cmdow "*{app['name']}*" /mov {pos['pos'][0]} {pos['pos'][1]}
cmdow "*{app['name']}*" /siz {pos['siz'][0]} {pos['siz'][1]}
        """
        app_cmd.append(template)
            
    return app_cmd

def render():
    for mode in modes:
        cmd = ""
        cmd += header_render()
        print(f"Mode render: {mode['name']}")
        app_cmd = apps_render(mode)
        cmd += "\n"
        cmd += "\n".join(app_cmd)
        cmd += "\n"
        cmd += f"""cmdow "*{mode['active']}*" /act"""
        f = open(f"{mode['name']}.cmd", "wb")
        f.write(bytes(cmd, "UTF8"))
        f.close()

render()

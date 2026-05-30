bl_info = {
    "name": "Codex AI Assistant",
    "author": "Zeppelin",
    "version": (1, 2, 1),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > Codex",
    "description": "AI 驱动的 Blender 建模助手，支持文字描述和图片识别转 3D",
    "category": "3D View",
    "support": "COMMUNITY",
    "tracker_url": "https://github.com/7eppelinyy/blender-codex/issues",
}

import bpy
from . import preferences
from . import operators
from . import panel

modules = (preferences, operators, panel)


def register():
    for mod in modules:
        try:
            mod.register()
        except Exception as e:
            print(f"[Codex] 注册模块 {mod.__name__} 失败: {e}")


def unregister():
    for mod in reversed(modules):
        try:
            mod.unregister()
        except Exception as e:
            print(f"[Codex] 注销模块 {mod.__name__} 失败: {e}")

import bpy
from .operators import (
    CODEX_OT_send_prompt,
    CODEX_OT_execute_code,
    CODEX_OT_clear_history,
    CODEX_OT_copy_code,
    CODE_HISTORY,
    LAST_CODE,
)


class CODEX_PT_main(bpy.types.Panel):
    bl_label = "Codex AI Assistant"
    bl_idname = "CODEX_PT_main"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Codex"
    bl_order = 0

    def draw(self, context):
        layout = self.layout

        # --- Prompt input ---
        col = layout.column(align=True)
        col.label(text="描述你想创建的内容：", icon="TEXT")
        col.prop(context.scene, "codex_prompt", text="")
        col.operator(CODEX_OT_send_prompt.bl_idname, icon="EXPORT")

        layout.separator()
        row = layout.row()
        row.label(text="生成的脚本", icon="SCRIPT")
        if LAST_CODE:
            row.operator(CODEX_OT_copy_code.bl_idname, text="", icon="COPYDOWN")

        box = layout.box()
        col = box.column(align=True)
        if LAST_CODE:
            lines = LAST_CODE.strip().split("\n")
            display = "\n".join(lines[:40])
            if len(lines) > 40:
                display += f"\n\n…（还有 {len(lines) - 40} 行）"
            for line in display.split("\n"):
                col.label(text=line[:100] or " ")
        else:
            col.label(text="AI 生成的代码将显示在这里。", icon="INFO")

        # --- Execute / Clear ---
        layout.separator()
        row = layout.row(align=True)
        row.operator(CODEX_OT_execute_code.bl_idname, icon="PLAY")
        row.operator(CODEX_OT_clear_history.bl_idname, icon="TRASH")

        # --- Status ---
        if context.scene.codex_status:
            layout.separator()
            box = layout.box()
            icon = "ERROR" if any(w in context.scene.codex_status for w in ("Error", "出错", "失败")) else "INFO"
            box.label(text=context.scene.codex_status, icon=icon)


def register():
    bpy.types.Scene.codex_prompt = bpy.props.StringProperty(
        name="Prompt",
        description="Describe what you want in natural language",
        default="",
        subtype="NONE",
    )
    bpy.types.Scene.codex_status = bpy.props.StringProperty(
        name="Status",
        description="Last operation status",
        default="",
    )
    bpy.utils.register_class(CODEX_PT_main)


def unregister():
    bpy.utils.unregister_class(CODEX_PT_main)
    del bpy.types.Scene.codex_prompt
    del bpy.types.Scene.codex_status

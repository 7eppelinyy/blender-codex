# Blender Codex AI Assistant

自然语言驱动的 Blender 建模助手 —— 支持 OpenAI 和 DeepSeek 等兼容模型，支持图片识别转 3D 和联网搜索。

![Blender Version](https://img.shields.io/badge/Blender-4.0%2B-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 功能

- **AI 生成建模代码** — 用自然语言描述需求，AI 自动生成 Blender Python 脚本
- **图片转 3D** — 上传参考图片，视觉模型分析后生成建模代码
- **联网搜索** — 可选启用 DuckDuckGo 搜索，搜索结果自动注入 AI 上下文
- **一键执行** — 生成的代码在 Blender 中直接运行
- **对话历史** — 多轮对话上下文，逐步迭代优化
- **多模型支持** — GPT-4o / GPT-4 Turbo / o3-mini / GPT-4.1 / DeepSeek-V3 / DeepSeek-R1 / DeepSeek-V4 Pro
- **零依赖** — 仅使用 Python 标准库，兼容 Blender 内置 Python

## 安装

1. 从 [Releases](https://github.com/7eppelinyy/blender_codex/releases) 下载最新 `.zip` 文件
2. Blender 中：**编辑 → 偏好设置 → 插件 → 安装…**
3. 选择下载的 `.zip` 文件
4. 勾选启用 **"Codex AI Assistant"**

### 开发安装

```bash
cd "%APPDATA%\Blender Foundation\Blender\<version>\scripts\addons\"
git clone https://github.com/7eppelinyy/blender_codex.git
```

## 设置

1. **编辑 → 偏好设置 → 插件 → Codex AI Assistant → 偏好设置**
2. 填入 API Key（OpenAI: `sk-…` / DeepSeek: `sk-…`）
3. 选择模型（推荐 DeepSeek-V4 Pro 或 GPT-4o）
4. DeepSeek 用户需将 API Base 改为 `https://api.deepseek.com`
5. 可选开启联网搜索

## 使用

1. 在 3D 视图按 **N** 键打开侧边栏
2. 点击 **Codex** 标签
3. 输入描述，如：
   - *"创建一个有 20 级台阶的螺旋楼梯"*
   - *"添加一个立方体，细分后应用置换修改器"*
   - *"创建一个金属红色材质并分配给选中物体"*
   - *"布置三点光源"*
   - *"生成发射发光球体的粒子系统"*
4. 可选：选择一张参考图片用于视觉识别
5. 点击 **"发送到 AI"**
6. 检查生成的代码，点击 **"执行生成脚本"**

## 支持的模型

| 模型 | 说明 |
|------|------|
| **GPT-4o** | 快速、能力强，推荐默认 |
| **GPT-4 Turbo** | 复杂多步脚本 |
| **o3-mini** | 轻量推理模型 |
| **GPT-4.1** | 最新旗舰 |
| **DeepSeek-V3** | 快速、高性价比 |
| **DeepSeek-R1** | 深度推理模型 |
| **DeepSeek-V4 Pro** | 最新旗舰，最强 |

## 隐私

- 提示词发送至所选 API 服务商处理
- 插件本身不在本地存储任何数据
- 对话历史仅保存在内存中，重载后清除

## 许可

MIT — 详见 [LICENSE](LICENSE)

## 贡献

欢迎提交 Issue 和 PR！请先开 Issue 讨论您想修改的内容。

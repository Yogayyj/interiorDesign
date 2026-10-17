# 空间灵感图片馆

纯 HTML/CSS/JavaScript，无需安装依赖。支持图片网格概览、逐张滚动浏览、大图左右切换和浏览器本地收藏。

## 使用仓库里的图片

1. 将图片放到仓库中（例如 `images/` 文件夹）。
2. 在仓库根目录运行 `python3 tools/scan_images.py` 更新 `images.json`。
3. 运行 `python3 -m http.server 8000`，通过 HTTP 打开 `index.html`。也可以将仓库发布到 GitHub Pages。

新增或移除仓库图片后请重新扫描，并一同提交生成的 `images.json`。

## 使用本地图片

也可以直接打开 `index.html`，点击“添加图片”或“选择文件夹”。本地文件不会上传，刷新后需要重新选择；选择相同文件后会恢复对应收藏。

收藏保存在当前浏览器的 localStorage 中，不会跨设备同步。清除浏览器数据会清除收藏。大图支持左右方向键，Esc 关闭。

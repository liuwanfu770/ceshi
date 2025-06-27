# 视频压缩工具

该仓库包含一个用于批量压缩视频的脚本 `compress_videos.py`。

## 使用方法

```bash
python3 compress_videos.py <视频所在目录>
```

脚本会遍历指定目录及其子目录中的 `.mp4` 和 `.mov` 文件，并使用以下参数调用 `ffmpeg` 进行压缩：

```
ffmpeg -i input.mp4 -vcodec libx264 -crf 24 -preset slow -acodec aac -b:a 128k output.mp4
```

压缩后的视频文件名会在原文件名基础上追加 `_compressed` 标记。

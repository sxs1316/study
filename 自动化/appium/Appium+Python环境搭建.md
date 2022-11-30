## 搭建准备
- Python
- Pycharm
- Appium
- JAVA
- Node
- Android_SDK

### 配置环境变量

```
JAVA_HOME

C:\Program Files\Java\jdk1.8.0_201
```

```
ANDROID_HOME

C:\Users\SXS\AppData\Local\Android\Sdk
```

```
PATH

%JAVA_HOME%\bin
%JAVA_HOME%\jre\bin

%ANDROID_HOME%
%ANDROID_HOME%\tools
%ANDROID_HOME%\platform-tools
%ANDROID_HOME%\build-tools\33.0.1
```

### 文件替换

- 解压 `sdk-tools-windows` 文件，将 `tools` 放入SDK目录

- 解压 `commandlinetools-win` 文件，将 `cmdline-tools\bin\apkanalyzer.bat` 文件复制到 `Sdk\platform-tools` 目录

### 安装Python模块

```bash
pip install selenium
pip install appium-python-client
```

### 检测appium环境

> 安装检测模块

命令行运行

```bash
npm install -g appium-doctor
```

### 连接夜审模拟器

- 将 `Sdk\platform-tools\adb.exe` 复制到桌面
- 将 `Sdk\build-tools\33.0.1\apt.exe` 复制到桌面
- 将两个文件复制到夜神模拟器安装目录
- 将 `adb.exe` 重命名为 `nox_adb.exe` 并移动到夜神模拟器安装目录
- 重启电脑
- 使用命令 `adb connect 127.0.0.1:62001` 连接夜神模拟器
- 使用命令 `adb devices -l` 查看设备连接状态
- 启动Appium-Server
- 使用脚本测试

### 使用真机测试

开发者模式打开以下开关
- 打开USB调试
- USB安装
- USB调试（安全设置）

使用数据线连接电脑，在手机上同意调试



### 获取软件包名

```bash
adb shell dumpsys activity recents | find "intent={"
```

```
cmp=com.android.browser/.BrowserActivity}
```
- 包名：`com.android.browser`
- Activity：`.BrowserActivity`

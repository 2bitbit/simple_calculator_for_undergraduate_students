pyinstaller --onedir `
  --add-data "resources/:resources/" `
  --add-data "frontend/html_template.py:frontend/" `
  --add-data "D:\\Software\\Anaconda\\envs\\appdev\\Lib\\site-packages\\matplotlib\\mpl-data:matplotlib/mpl-data" `
  --icon=resources/images/icon.ico `
  main.py
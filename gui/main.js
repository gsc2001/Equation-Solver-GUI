
const {app, BrowserWindow} = require('electron')
const path = require('path')
function createWindow () {

  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    icon: path.join(__dirname, 'icon/icon.jpg')
  })
  mainWindow.loadFile('index.html')
}

app.whenReady().then(createWindow)


app.on('window-all-closed', function () {

  if (process.platform !== 'darwin') app.quit()
})

app.on('activate', function () {

  if (BrowserWindow.getAllWindows().length === 0) createWindow()
})

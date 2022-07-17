## Install
```
npm i
```

## Run
```
npm start 
```

### Automatic run setup
Create link to `spotlight_wallpapers.vbs` script in Windows Startup folder to extract Spotlight pictures on system startup. It's path should look like the following: 
```
C:\Users\<User>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\spotlight_wallpapers - Shortcut
``` 

Create link to `run_spotlight_upload.vbs` script in Windows Startup folder to upload extracted pictures on system startup. 
```
C:\Users\<User>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\run_spotlight_upload - Shortcut
``` 


These two scripts are not guaranteed to run one after another.

## Todos
* Move uploaded image to the archive, delete original
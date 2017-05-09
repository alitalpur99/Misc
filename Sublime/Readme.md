# "How to install SublimeREPL (interactive mode)"
### Video instructions on this [youtube](https://www.youtube.com/watch?v=wM2LbXCkLDI) link
1. Install latest Sublime-text version
2. Paste the following text in sublime-text console (use Ctrl+~) or from menu (View->show console. Note that the text is also available on https://packagecontrol.io/installation.

`
import urllib.request,os,hashlib; h = 'df21e130d211cfc94d9b0905775a7c0f' + '1e3d39e33b79698005270310898eea76'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
`

3. Open the pallete (Ctrl+Shift+P), and search "Package control: Install package"
4. Enter "SublimeREPL" and hit enter to install the package
5. Goto Preference-> Browse packages -> SublimeREPL -> config -> python and open "Main.sublime-menu" file in sublime-text
6. edit the file in "Python - RUN current file" para. Change

` "cmd": ["python", "-u", "$file_basename"], ` 
to 
` "cmd": ["python", "-u", "-i", "$file_basename"], `
i.e. add ` "-i", `

7. Goto Tools-> BuildSystems-> NewBuildSystem and enter following text in the file

`{ "target": "run_existing_window_command", `

` "id": "repl_python_run",`

`"file": "config/Python/Main.sublime-menu" }`
 and save file as `SublimeREPL-python.sublime-build` and close the sublime-text editor.
 
 8. Open sublime-text. From Tools menue, select BuildSystem as `SublimeREPL-python` 
 
 9. Open your python (.py) file and run it (Ctrl+B).
 

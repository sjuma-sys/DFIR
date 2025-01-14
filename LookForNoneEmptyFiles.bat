:: A way to find none empty files, forfiles is more powerful as it can do it in a time range
forfiles /P J:\MichealCasey\V10 /M *.* /S /D +"01/01/1970" /C "cmd /c if @fsize gtr 0 echo @path @fsize @fdate @ftime" | findstr /r "\.emlx \.pdf \.docx \.xlsx \.doc"

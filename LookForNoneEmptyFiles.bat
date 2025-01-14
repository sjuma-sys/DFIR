:: A way to find none empty files within files, forfiles is more powerful as it can do it in a time range, also you can change the findstr to look for other file extensions
forfiles /P J:\Foldername /M *.* /S /D +"01/01/1970" /C "cmd /c if @fsize gtr 0 echo @path @fsize @fdate @ftime" | findstr /r "\.emlx \.pdf \.docx \.xlsx \.doc"

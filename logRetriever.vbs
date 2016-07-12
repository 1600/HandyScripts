Function generateEXEdictionary()
	
	
	Dim oExec, sResults, temparray
	Set shellObj = CreateObject("WScript.Shell")
	Set oExec = shellObj.Exec("wmic process get ExecutablePath")
	
	sResults = oExec.Stdout.ReadAll
	temparray = split(sResults,chr(13)&chr(10))
	
	Dim exeDict : Set exeDict = WSH.CreateObject("Scripting.Dictionary")
	
	For Each i in temparray
		i = replace(i," ","")
		if len(i)>=2 Then 					'过滤无效内容
			if NOT exeDict.Exists(getEXEname(i)) Then
				exeDict.Add getEXEname(i),getPATHname(i)
			end if
		End if
	Next
	
	Set generateEXEdictionary = exeDict
End function

Sub serverTypeGetter(procdict)
	Dim exePool : Set exePool = WSH.CreateObject("Scripting.Dictionary")
	httpdlist = array("httpd.exe","httpd2.exe")
	tomcatlist = array("tomcat.exe")
	iislist = array("w3wp.exe","explorer.exe","wmic.exe")
	
	exePool.add "httpd",httpdlist
	exePool.add "tomcat",tomcatlist
	exePool.add "test",iislist
	
	For Each currentProcess in procdict
		For Each serverType in exePool
			For i = 0 to Ubound(exePool.item(serverType))
				if UCase(currentProcess)= UCase(exePool.item(serverType)(i)) Then
					
					WScript.Echo "currentProcess is "+ currentProcess + "    tested against "+ exePool.item(serverType)(i) + ", Type - "+TypeName(exePool.item(serverType)(i))+" Result: SUCCESSFUL!!..Dispatching..."
					WScript.Echo "Dispatching to ServerType: "+ ServerType
					WScript.Echo TypeName(ServerType)
					LogTypeDispatcher(serverType)
				else
					WScript.Echo "Result: Failed."
				End if
			Next
		
		Next
	Next
End Sub



Function getEXEname(string)
	Dim re
	Set re = New RegExp
	re.Pattern = "[^\\]+$"
	Set Matches = re.Execute(string)
	For Each i in Matches
		getEXEname = Left(i,len(i)-1)
	Next
End Function


Function getPATHname(string)
	Dim re
	Set re = New RegExp
	re.Pattern = "^(.*[\\])"
	Set Matches = re.Execute(string)
	For Each i in Matches
		getPATHname = i
	Next
End Function

Sub LogTypeDispatcher(serverType)

End Sub


serverTypeGetter(generateEXEdictionary())